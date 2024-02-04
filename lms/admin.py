from django.contrib import admin

from .models import *
# Register your models here.

@admin.register(LibraryRule)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ("amount_fine", "description" )


@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("category", "auther", "title")

@admin.register(BookBorrower)
class BookBorrowerAdmin(admin.ModelAdmin):
    list_display = ("book", "borrow_user", "issue_datetime", "return_datetime" )
    
# @admin.register(BookReturn)
# class BookReturnAdmin(admin.ModelAdmin):
#     list_display = ("user", "book")
    
    