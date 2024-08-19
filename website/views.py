from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Blog,Pictures
from django import forms

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Pictures
        fields = ['description','image']

def galleryView(request):
    pictures = Pictures.objects.all()
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = GalleryForm()
    
    context = {
        'pictures': pictures,
        'form': form
    }
    return render(request, 'gallery.html', context)

def deletePicture(request, id):
    picture = Pictures.objects.get(id=id)
    picture.delete()
    return redirect('gallery')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after sign up
            return redirect('home')  # Redirect to a homepage or other page after sign up
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def home_view(request):
    return render(request,'home.html')

def objective_view(request):
    return render(request,'objectives.html')

def contact_view(request):
    return render(request,'contact.html')

def blog_view(request):
    pass

def gallery_view(request):
    pass

