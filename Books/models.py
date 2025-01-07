from django.db import models

# Create your models here.

from django.contrib.auth.models import User



class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    ISBN = models.IntegerField(unique=True)
    available_copies = models.PositiveIntegerField(default=1)
    links = models.URLField(null=True)
    

    def check_out(self):

        if self.available_copies > 0: # check if there are available books 
            self.available_copies -=1  # decrement one 
            self.save()  # save this in model Book 


        else: # incase there are no copies at all 
           raise ValueError ("There are no longer available copies")


    def return_book(self):

        if self.available_copies >= 0: # condition that get us True
            self.available_copies +=1 # decrement the copies by one
            self.save()
        
    def __str__(self):
        return self.title



class CheckOut(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    check_out_date = models.DateTimeField(auto_now_add=True,null=True)
    return_date = models.DateTimeField(null=True,blank=True)
    
    class Meta:
        unique_together = ('user','book') # check that one user can check out one copy of each book 



class BookWaitlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    notified = models.BooleanField(default=False)