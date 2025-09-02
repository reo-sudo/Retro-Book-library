from django.urls import path
from . import views
from django.views.generic import RedirectView

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', RedirectView.as_view(url='login/'), name='root'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('home/', views.home_view, name='home'),
    path('user/', views.user_view, name='user'),
    path('register/', views.register_views, name='register'),
    path('Library/', views.Library_view, name='Library'),
    path('search-books/', views.search_books, name='search_books'),
    path('add-book/', views.add_book, name='add_book'),
    path('delete-book/<int:entry_id>/', views.delete_book, name='delete_book'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]


