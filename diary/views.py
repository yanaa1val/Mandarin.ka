from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import DiaryEntry
from .forms import DiaryEntryForm, UserProfileForm

def home(request):
    latest_entries = DiaryEntry.objects.order_by('-date')[:5]
    return render(request, 'diary/home.html', {'latest_entries': latest_entries})

@login_required
def diary_list(request):
    entries = DiaryEntry.objects.filter(user=request.user).order_by('-date')
    return render(request, 'diary/diary_list.html', {'entries': entries})

@login_required
def add_entry(request):
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('diary_list')
    else:
        form = DiaryEntryForm()
    return render(request, 'diary/add_entry.html', {'form': form})

@login_required
def edit_entry(request, entry_id):
    entry = get_object_or_404(DiaryEntry, id=entry_id, user=request.user)
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('diary_list')
    else:
        form = DiaryEntryForm(instance=entry)
    return render(request, 'diary/edit_entry.html', {'form': form})

@login_required
def search_entries(request):
    query = request.GET.get('q')
    if query:
        entries = DiaryEntry.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query),
            user=request.user
        ).order_by('-date')
    else:
        entries = DiaryEntry.objects.filter(user=request.user).order_by('-date')
    return render(request, 'diary/search_entries.html', {'entries': entries, 'query': query})

@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'diary/user_profile.html', {'form': form})
