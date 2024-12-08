from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('diary/', views.diary_list, name='diary_list'),
    path('diary/add/', views.add_entry, name='add_entry'),
    path('diary/edit/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('diary/search/', views.search_entries, name='search_entries'),
    path('profile/', views.user_profile, name='user_profile'),
]
