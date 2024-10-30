from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .models import HomePage, PetProfile, AboutPage, PrivacyPage, TermsPage
from item.models import Category, Item
from .forms import SignupForm
from django.contrib.auth import logout


def home(request):
    items = Item.objects.filter(is_sold=False)[0:8]
    categories = Category.objects.all()

    homepage_info =HomePage.objects.first()
    # Fetch all HomePage objects
    all_banner_info = HomePage.objects.all()
    # Fetch all PetProfile objects
    all_pet_profiles = PetProfile.objects.all()
    # Fetch all PetProfile objects
    six_pet_prof = PetProfile.objects.all()[:8]
    # Fetch all PetProfile objects

    context = {
        'homepage': homepage_info,
        'all': all_banner_info,
        'pets': all_pet_profiles,
        'six_pets': six_pet_prof,
        'categories': categories,
        'items': items,
    }

    return render(request, 'core/index.html', context)


def pets(request):
    all_pet_profiles = PetProfile.objects.all()
    
    context = {
        'pets': all_pet_profiles
    }    
    
    return render(request, 'core/pets.html', context )


def about(request):
    #about_description = AboutPage.objects.all()
    about_page = AboutPage.objects.first()

    context = {
        'about_page': about_page

    }   

    return render(request, 'core/about.html', context )  


def contact(request):
    return render(request, 'core/contact.html')


def privacy(request):
    privacy_text = PrivacyPage.objects.first()

    context = {
        'privacy_text': privacy_text

    }

    return render(request, 'core/privacy.html', context)

def terms(request):
    terms_text = TermsPage.objects.first()

    context = {
        'terms_text': terms_text
    }

    return render(request, 'core/terms_of_use.html', context)


 
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Success! Account Created! Please log in, {username}')
            return redirect('core:login')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

