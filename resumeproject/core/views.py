from django.shortcuts import render

# Create your views here.

# Home page
def home(request):
    context={'home':'active'}
    return render(request,'tmcore/home.html',context)

# Skills 
def skills(request):
    context={'skills':'active'}
    return render(request,'tmcore/skills.html',context)

# Contacts
def contact(request):
    context={'contact':'active'}
    return render(request,'tmcore/contact.html',context)


