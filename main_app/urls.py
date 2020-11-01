from django.urls import path
from . import views
from .views import contactView, successView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('data/', views.get_data, name='data'),
    path('email/', contactView, name='email'),
    path('success/', successView, name='success'),
    path('addresserror/', views.addresserror, name='addresserror'),
]