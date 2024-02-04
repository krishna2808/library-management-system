from rest_framework import serializers
from .models import * 
from .models import User


class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = "__all__"

class BookBorrowerSerializer(serializers.ModelSerializer):
    book_title = serializers.StringRelatedField(source="book.title", read_only=True)
    borrow_username = serializers.StringRelatedField(source="borrow_user.username", read_only=True)  
    class Meta:
        model = BookBorrower
        fields = ("book_title", "book", "borrow_username", "borrow_user", "issue_datetime", "return_datetime", "is_return", "modified_datetime", "created_datetime")       
        # fields = ( "book",  "borrow_user", "issue_datetime", "return_datetime")       