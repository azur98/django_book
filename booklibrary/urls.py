from django.urls import path
from .views import BookListView
from .views import BookListView, BookDetailView

urlpatterns = [
    path('list/', BookListView.as_view(), name='list'), 
    path('detail/<int:pk>/', BookDetailView.as_view()),  
]