from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register,name='register'),
    path('createcustomer/',views.create_customer,name='createcustomer')
]