from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    path('book-borrow/', book_borrow, name="book-borrow"),
    path('users-book-status/', users_book_status, name="users-book-status"),
    
    path('book/', BookAPI.as_view(), name="signup"),
    path('user-book-request/', UserBookRequest.as_view(), name="user-book-request"),
    path('user-book-return/', UserBookReturnList.as_view(), name="user-book-return"),
    path('staff-user-book-request/', StaffUserBookRequest.as_view(), name="staff-user-book-request"),
    path('staff-user-book-return/', StaffUserBookReturn.as_view(), name="staff-user-book-return"),
]