from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views
from .forms import LoginForm

urlpatterns = [
    path('', views.home, name='home-home'),
    path('contact/', views.contact, name='home-contact'),
    path('about/', views.about, name='home-about'),
    path('pets/', views.pets, name='home-pets'),
    path('privacy/', views.privacy, name='home-privacy'),
    path('terms/', views.terms, name='home-terms'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()