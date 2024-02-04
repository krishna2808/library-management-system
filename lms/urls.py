from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    path('book-borrow/', book_borrow, name="book-borrow"),
    path('book/', BookAPI.as_view(), name="signup"),
    path('user-book-request/', UserBookRequest.as_view(), name="user-book-request"),
    path('user-book-return/', UserBookReturnList.as_view(), name="user-book-return"),
    path('staff-user-book-borrower/', StaffUserBookBorrower.as_view(), name="staff-user-user-book-borrower"),
    path('staff-user-book-return/', StaffUserBookReturnList.as_view(), name="staff-useruser-book-return"),
]