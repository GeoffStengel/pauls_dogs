from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views
from .forms import LoginForm
 
app_name = 'core'

urlpatterns = [
    path('', views.home, name='home-home'),
    path('contact/', views.contact, name='home-contact'),
    path('about/', views.about, name='home-about'),
    path('pets/', views.pets, name='home-pets'),
    path('privacy/', views.privacy, name='home-privacy'),
    path('terms/', views.terms, name='home-terms'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    #path('logout/',views.custom_logout, name='logout'),
    path('logout/', auth_views.LogoutView.as_view(next_page='core:home-home'), name='logout'),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)