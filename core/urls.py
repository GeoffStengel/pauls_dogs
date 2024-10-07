from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home-home'),
    path('contact/', views.contact, name='home-contact'),
    path('about/', views.about, name='home-about'),
    path('pets/', views.pets, name='home-pets'),
    path('privacy/', views.privacy, name='home-privacy'),
    path('terms/', views.terms, name='home-terms'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()