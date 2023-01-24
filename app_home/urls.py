from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('doctors/', views.doctors, name='doctors'),
    path('specialities/', views.specialities, name='specialities'),
    path('booking/', views.booking, name='booking'),
    # path('booking_insert/', views.booking_insert),
    path('callback_insert/', views.callback_insert,),

] 
