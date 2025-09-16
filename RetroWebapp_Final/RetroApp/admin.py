from django.contrib import admin
from .models import Book, LibraryEntry

admin.site.register(Book)
admin.site.register(LibraryEntry)