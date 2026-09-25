from django.urls import path
from .views import contact_view, success, book_create, book_success


urlpatterns = [
    path('', contact_view, name='contact'),
    path('success/', success, name='success'),
    path('book/create/', book_create, name = 'book_create') ,
    path('/book/success/' , book_success, name = 'book_success')
]