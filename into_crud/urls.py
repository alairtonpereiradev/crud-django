from django.urls import path

from . import views

urlpatterns = [
    path('book-list', views.booklist, name='book-list'),
    path('book-create', views.bookCreate, name='book-create'),
    path('book-update/<int:id>', views.bookUpdate, name='book-update'),
    path('book-delete/<int:id>', views.bookDelete, name='book-delete'),
]
