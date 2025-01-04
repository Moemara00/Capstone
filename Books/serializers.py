from .models import Book, CheckOut
from rest_framework import serializers
from django.contrib.auth.models import User











class BookUserSerializer(serializers.ModelSerializer):
    available_copies = serializers.IntegerField(read_only = True)
    
    class Meta: 
        model = Book
        fields = [
                'id',
                'title',
                'author',
                'published_date',
                'ISBN',
                'available_copies',
              
               
                ]



class BookAdminSerializer(serializers.ModelSerializer):
    available_copies = serializers.IntegerField(read_only = True)
    class Meta: 
        model = Book
        fields = [
                'id',
                 'title',
                'author',
                'published_date',
                'ISBN',
                'available_copies',
                'links'
                ]


# class CheckOutSerializer(serializers.ModelSerializer):

#     return_date = serializers.SerializerMethodField(read_only=True)
#     user = serializers.SerializerMethodField(read_only=True)
#     class Meta:
#         model = CheckOut
#         fields = ['book','check_out_date','return_date','user']


#     def create(self, validated_data):
       
    
#         instance = CheckOut.objects.create(**validated_data)

#         # Return the created instance
#         return instance


#     def get_return_date(self,obj):
#         return obj.return_date
#     def get_user(self,obj):
#         return obj.user.username

class CheckOutSerializer(serializers.ModelSerializer):

    
    # book = serializers.SerializerMethodField(read_only = True)
    book_link = serializers.SerializerMethodField(read_only=True)
    Check_id  = serializers.SerializerMethodField(read_only= True)
    class Meta:  
        model = CheckOut
        
        fields = ['check_out_date','return_date','book','book_link','Check_id']
        read_only_fields = ['check_out_date','return_date','book_link','Check_id']

   
    # def get_book(self,obj):
    #         return obj.book.title
    
    def get_book_link(self,obj):
         if obj.return_date:
              return False
         return obj.book.links
    

    def get_Check_id(self,obj):
        return obj.id
    
    def create(self, validated_data):
        return super().create(validated_data)