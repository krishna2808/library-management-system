from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status


from .serializers import * 
from .models import * 
from copy import copy
from datetime import datetime
# Create your views here.
def dashboard(request):
    if request.user.is_staff == True:
        return render(request, "lms/staff_dashboard.html")
    return render(request, "lms/user_dashboard.html")

def book_borrow(request):
    return render(request, "lms/book_borrow.html")

def users_book_status(request):
    return render(request, "lms/users_book_status.html")
        

class BookAPI(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.filter(is_approved = True)
    serializer_class = BookSerializer
    
    def get_user(self):
        try:
            user = self.request.user 
            print("this user", user )
        except Exception as e:
            raise Http404("User not found")
        print("user ---------------  ")
        return user

    # def get_queryset(self):
    #     return Book.objects.filter(auther = self.get_user())

    def get_object(self):
        try:
            book_object =  Book.objects.get(id = self.request.data["id"])
        except:
            raise Http404("Book not found")
        return book_object  

    def get_serializer_class(self):
        self.request.data["auther"] = self.get_user().id
        return BookSerializer

class StaffUserBookRequest(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BookBorrower.objects.all()
    serializer_class = BookBorrowerSerializer  
    
    def get_queryset(self):
        return BookBorrower.objects.filter(is_return = False)
    def get_object(self):
        try:
            book_borrower_object = BookBorrower.objects.get(id = self.request.data.get("book_borrower_id"))
        except Exception as e:
            raise Http404("Book Borrower not found")
        return book_borrower_object
        
 
class StaffUserBookReturn(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BookBorrower.objects.all()
    serializer_class = BookBorrowerSerializer  
    
    def get_queryset(self):
        return BookBorrower.objects.filter(is_return = True)

    def get_object(self):
        try:
            book_borrower_object = BookBorrower.objects.get(id = self.request.data.get("book_borrower_id"))
        except Exception as e:
            raise Http404("Book return not found")
        return book_borrower_object
        

class UserBookRequest(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView ):
    permission_classes = [IsAuthenticated]
    queryset = BookBorrower.objects.all()
    serializer_class = BookBorrowerSerializer  
    
    def get_queryset(self):
        return BookBorrower.objects.filter(borrow_user= self.request.user, is_return = False)
    def get_object(self):
        try:
            book_borrower_object = BookBorrower.objects.get(id = self.request.data.get("book_borrower_id"))
        except Exception as e:
            raise Http404("Book return not found")
        return book_borrower_object
    # def get_serializer_class(self):
    #     book = self.request.data.get("book_id")
    #     borrow_user = self.request.user.id
    #     issue_datetime = self.request.data.get("issue_datetime")
    #     return_datetime = self.request.data.get("return_datetime")
    #     print("issue_datetime -- ", issue_datetime,'return_datetime -------- '  ,  return_datetime )
    #     mutable_data = copy(self.request.data)
    #     mutable_data["book"] = book 
    #     # mutable_data["amount_fine"] = 0 
    #     mutable_data['borrow_user'] = borrow_user
    #     mutable_data["issue_datetime"] = datetime.strptime(issue_datetime, "%Y-%m-%dT%H:%M")
    #     mutable_data["return_datetime"] = datetime.strptime(return_datetime, "%Y-%m-%dT%H:%M")
    #     print("issue_datetime -- ", issue_datetime,'return_datetime -------- '  ,  return_datetime )
    #     return BookBorrowerSerializer
    

    def post(self, request, format=None):
        book = request.data.get("book_id")
        borrow_user = request.user.id
        issue_datetime = request.data.get("issue_datetime")
        return_datetime = request.data.get("return_datetime")
        print("issue_datetime -- ", issue_datetime,'return_datetime -------- '  ,  return_datetime )
        mutable_data = copy(request.data)
        mutable_data["book"] = book 
        mutable_data['borrow_user'] = borrow_user
        mutable_data["issue_datetime"] = datetime.strptime(issue_datetime, "%Y-%m-%dT%H:%M")
        mutable_data["return_datetime"] = datetime.strptime(return_datetime, "%Y-%m-%dT%H:%M")
        serializer = BookBorrowerSerializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserBookReturnList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BookBorrower.objects.all()
    serializer_class = BookBorrowerSerializer  
    
    def get_queryset(self):
        return BookBorrower.objects.filter(borrow_user= self.request.user, is_return = True)
    