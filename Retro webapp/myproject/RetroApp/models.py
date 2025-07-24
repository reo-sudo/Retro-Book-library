from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    thumbnail = models.URLField(blank=True)
    google_id = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class LibraryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="library_entries")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}' copy of {self.book.title}"
    

