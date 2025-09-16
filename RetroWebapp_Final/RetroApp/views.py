from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .models import Book, LibraryEntry
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
from django.db.models import Q
import random
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
import requests
from django.utils import timezone
from datetime import timedelta

def login_view(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                messages.error(request, 'Invalid Login')
        return render(request, 'login.html')
    except Exception as e:
        messages.error(request , f'Error during login: {str(e)}')
        return render(request , 'login.html')


@login_required
def home_view(request):
    keywords = ['science', 'maths', 'codeing', 'fantasy', 'history', 'health']
    query = random.choice(keywords)

    picks = []
    try:
        url = f'https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=10'
        response = requests.get(url)
        data = response.json()

        if 'items' in data:
            for item in data['items']:
                info = item['volumeInfo']
                picks.append({
                    'title': info.get('title', 'No title'),
                    'authors': ', '.join(info.get('authors', [])),
                    'thumbnail': info.get('imageLinks', {}).get('thumbnail', ''),
                    'description': info.get('description', 'No description'),
                    'google_id': item.get('id', ''),
                })
    except Exception as e:
        print("API Error:",)


    return render(request, 'home.html', {
        'username': request.user.username,
        'picks': picks,
    })



@login_required
def Library_view(request):
    print("Library Entries:", request.user.library_entries.all())
    return render(request, 'Library.html', {
        'username': request.user.username,
        'library_entries': request.user.library_entries.all()
    })

@login_required
def user_view(request):
    library_count = LibraryEntry.objects.filter(user=request.user).count()
    is_admin = request.user.is_superuser or request.user.is_staff
    join_date = request.user.date_joined.strftime('%Y-%m-%d')
    level_books = { library_count < 5: 'beginner',  5 <= library_count < 15: 'intermediate',  15 <= library_count < 30: 'advanced',  library_count >= 30: 'master' }
    
    return render(request, 'user.html', {
    'username': request.user.username,
    'library_count': library_count,
    'is_admin': is_admin,
    'join_date': join_date,
    'level': next((level for condition, level in level_books.items() if condition), 'unknown'),
    
    
    
    

    })

def register_views(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #basic checks
        if len(password) < 6:
            messages.error(request ,'password must be at least 6 characters long')
            return redirect('register')
        
        elif not any(char.isdigit() for char in password):
            messages.error(request, 'password must contain at least one number')
            return redirect('register')
        
        try:
            validate_password(password, user=None)
        except ValidationError as e:
            for error in e.messages:
                messages.error(request, error)
            return redirect('register')
        
       
       

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'User Account Created, Please Log in')
            return redirect('login')
        
    return render(request, 'register.html')
        
@login_required
def search_books(request):
    query = request.GET.get('q', '')
    results = []

    if query:

        local_books = Book.objects.filter(
            Q(title__icontains=query) | Q(authors__icontains=query)
        )

        for book in local_books:
            results.append({
                'source': 'local',
                'title': book.title,
                'authors': book.authors,
                'description': book.description,
                'thumbnail': book.thumbnail,
                'google_id': book.google_id,

            })

        try:
            url = f'https://www.googleapis.com/books/v1/volumes?q={query}'
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if 'items' in data:
                for item in data['items']:
                    google_id = item['id']
                    if Book.objects.filter(google_id=google_id).exists():
                        continue
                    
                    info = item['volumeInfo']
                    results.append({
                        'source': 'google',
                        'title': info.get('title', 'No Title'),
                        'authors': ','.join(info.get('authors', [])),
                        'description': info.get('description','No description available.'),
                        'thumbnail': info.get('imageLinks', {}).get('thumbnail',''),
                        'google_id': item['id'],
                    })
        except Exception as e:
            print(e)
    
    return JsonResponse({'items': results})




   


@csrf_exempt
@login_required
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        authors = request.POST.get('authors', '')
        description = request.POST.get('description', '')
        thumbnail = request.POST.get('thumbnail', '')
        google_id = request.POST.get('google_id')
        

        if not title or not google_id:
            messages.error(request, 'Title or Google ID is Required.')
            return redirect('home')

   

        existing_book = Book.objects.filter(google_id=google_id).first()
        

        if not existing_book:   
            try:
                existing_book = Book.objects.create(
                    title=title,
                    authors=authors,
                    description=description,
                    thumbnail=thumbnail,
                    google_id=google_id,
                )
            except Exception as e:
                messages.error(request, f'Error createing book:{str(e)}')
                return redirect('home')
            
        if LibraryEntry.objects.filter(user=request.user, book=existing_book).exists():
            messages.warning(request, 'Book already exists in your Library.')
        else:
                try:
                    LibraryEntry.objects.create(
                        user=request.user,
                        book=existing_book,
                    )
                    messages.success(request, 'Book added successfully.')
                except Exception as e:
                    messages.error(request, f'Error adding book to library: {str(e)}')
            
                return redirect('home')
        
        return redirect('home')

                
                
         
    

def is_admin(user):
    return user.username == "Admin"

@user_passes_test(is_admin)
@login_required
def admin_dashboard(request):
   all_users = User.objects.all()
   user_library_map = {}

   for user in all_users:
       entries = LibraryEntry.objects.filter(user=user)
       user_library_map[user.username] = entries

   return render(request, 'admin_dashboard.html', {
       'total_users': all_users.count(),
       'user_library_map': user_library_map,
   })


@login_required
def delete_book(request, entry_id):
    try:
        entry = get_object_or_404(LibraryEntry, id=entry_id, user=request.user)
        book = entry.book
        entry.delete()

        if not LibraryEntry.objects.filter(book=book, user=request.user).exists():
            book.delete()
        messages.success(request, 'Book deleted for Library.')
    except LibraryEntry.DoesNotExist:
        messages.error(request, 'Book not Fount in your Library')
    return redirect('Library')
        


        