from django.contrib import admin

from cbvapp.models import book

class book_admin(admin.ModelAdmin):
    list_display = ['title','author','pages']


admin.site.register(book,book_admin)
# Register your models here.
