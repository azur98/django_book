from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import BookModel   

class BookListView(ListView):   
    model = BookModel   
    template_name = "booklibrary/book_list.html"    

class BookDetailView(DetailView): 
    model = BookModel   
    template_name = "booklibrary/book_detail.html"    
