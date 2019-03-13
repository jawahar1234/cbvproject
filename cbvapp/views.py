
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView
from .models import book


# Create your views here.
class book_listview(ListView):
    model = book
    template_name = 'cbvapp/info.html'
    context_object_name = 'books'
class book_detail(DetailView):
    model = book
    template_name = 'cbvapp/detail.html'

class book_create(CreateView):
    model = book
    fields = ('title','author','pages')
class book_update(UpdateView):
    model = book
    fields = ('pages',)



