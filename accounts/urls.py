from django.urls import path
from . import views 

urlpatterns = [
    path('registerUser/', views.registeruser, name="registerUser"),
    path('registerVendor/', views.registerVendor, name="registerVendor"),
]