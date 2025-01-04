from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, CheckOut
from .serializers import BookAdminSerializer, CheckOutSerializer,BookUserSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import BasePermission
from django.utils import timezone
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status , filters
from django.urls import reverse_lazy
from rest_framework.exceptions import PermissionDenied
import datetime
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView , RetrieveAPIView
# Create your views here.



# def get_unchecked_out_books_for_user(user):
#     checked_out_books = CheckOut.objects.filter(user=user)
#     unchecked_out_books = Book.objects.filter(available_copies__gt=0).exclude(id__in=checked_out_books)
#     return unchecked_out_books






# list the books that available


class DetailUserView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookUserSerializer
    def get_queryset(self,pk=None):
        CheckOut.objects.filter(pk=pk)
        return super().get_queryset()


class ListAvailableBooks(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']


    def get_queryset(self):
    
        return Book.objects.exclude(available_copies=0)

class BooksViewsetAdmin(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookAdminSerializer
    permission_classes = [permissions.IsAdminUser]
   
   
    
    
    def perform_create(self, serializer):
        user = self.request.user
        if user.is_superuser:
            publish_date= serializer.validated_data['published_date']

            current_date = datetime.date.today()
        
            if publish_date > current_date:
                raise ValidationError("Sorry ,This is a future year !!")
            
            serializer.save()



class CheckOutView(viewsets.ModelViewSet,LoginRequiredMixin):

    queryset = CheckOut.objects.all()
    serializer_class = CheckOutSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return CheckOut.objects.filter(user=user)
        
    



    def perform_create(self, serializer): # serializer == the model CheckOut
        
        user = self.request.user
        book = serializer.validated_data['book'] # Model Book



        # Check if the book is available or not 

        if book.available_copies <= 0:
            raise ValidationError("This book is not available")
        
        # Check if the book already checked out

        # the book is checked out and returned 
        check_out = CheckOut.objects.filter(user=user,book=book,return_date__isnull=False).first()

        if check_out:
                # raise ValidationError("You checked and returned the book , please choose another item !")
                book.check_out() # reduce one from available copies in the Book model 
                serializer.save(user=user) # save the records in the CheckOut model 

        if CheckOut.objects.filter(user=user,book=book,return_date__isnull=True).exists():
            raise ValidationError("You already checked the book out")



      
        
      



class UnCheckOutView(viewsets.ModelViewSet,LoginRequiredMixin):

    queryset = CheckOut.objects.all()
    serializer_class = CheckOutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # we want to return unchecked out book 
        return CheckOut.objects.filter(return_date__isnull=True)
    def perform_create(self, serializer):
        
        book = serializer.validated_data['book']
        user = self.request.user
         
        # sample of checked out book
        checked_out = CheckOut.objects.filter(user=user,book=book,return_date__isnull=True).first()
        # sample of returned book
        returned_book = CheckOut.objects.filter(user=user,book=book,return_date__isnull=False).first()



        # make sure the book can't return more than once

        if returned_book:
            raise ValidationError("You did return the book before !!")
        

        # make sure the book already checked out 

        if not checked_out:
            raise ValidationError("You didn't check the book yet!")
        
        # if the book checked out 
            # 1- increase the number of copies using the check_out func and save this in book model
            # 2- update the return date in the CheckOut model to be like the timezone and save this
        if checked_out:
            book.return_book()
            return_date = timezone.now()
            checked_out.return_date = return_date
            checked_out.save()