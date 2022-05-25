from django.urls import path
from . import views 

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name ='hello'),
    path('users/',views.UserView.as_view()),
    path('login/',views.UserLoginView.as_view()),
    path('drivers/',views.DriverView.as_view()),
    path('register/',views.UserRegistrationView.as_view()),
    path('driverregister/',views.DriverRegistrationView.as_view()),
]