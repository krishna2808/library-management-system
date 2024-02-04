from django.db import models
from account.models import User
from datetime import datetime
# Create your models here.

class LibraryRule(models.Model):
    description = models.CharField(max_length = 300)
    amount_fine = models.IntegerField()
    


class BookCategory(models.Model):
    category_name = models.CharField(max_length = 100, null=True, blank=True)
    modifed_datetime  = models.DateTimeField(auto_now = True)
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

class Book(models.Model):
    category = models.ForeignKey(BookCategory, related_name='book_category', on_delete=models.CASCADE)
    auther = models.ForeignKey(User, related_name="book_auther", on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    image = models.ImageField(null=True, blank=True, upload_to = f"images/lms/{str(datetime.now())}/")
    description = models.CharField(max_length = 300)
    total = models.IntegerField(null=True)
    is_approved = models.BooleanField(default = False)
    data_of_publish  = models.DateTimeField(auto_now = True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ('-data_of_publish', )
    
class BookBorrower(models.Model):
    book = models.ForeignKey(Book, related_name= "book_borrower", on_delete = models.DO_NOTHING)
    borrow_user = models.ForeignKey(User, related_name= "book_borrower_user", on_delete = models.DO_NOTHING)
    issue_datetime = models.DateTimeField()
    return_datetime = models.DateTimeField()
    is_return = models.BooleanField(default = False)
    # amount_fine = models.ForeignKey(LibraryRule, related_name="library_rule_book", on_delete = models.DO_NOTHING)
    modified_datetime  = models.DateTimeField(auto_now = True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-modified_datetime', )
    def __str__(self):
        return self.book.title + " " + self.borrow_user.username

# class BookReturn(models.Model):
#     user = models.ForeignKey(User, related_name= "book_return_user", on_delete = models.DO_NOTHING)
#     book = models.ForeignKey(Book, related_name= "book_return", on_delete = models.DO_NOTHING)
#     modified_datetime  = models.DateTimeField(auto_now = True)
#     created_datetime = models.DateTimeField(auto_now_add=True)


    
    
    
	
