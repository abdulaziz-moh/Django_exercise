from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # pass
    list_display = ('title','author','publication_year')
    search_fields = ('title', 'author')

admin.site.register(Book,BookAdmin)
