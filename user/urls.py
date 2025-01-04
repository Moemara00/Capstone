from django.urls import path
from django.contrib.auth.views import LoginView
from .views import RegisterView,log_out
urlpatterns = [

    path('login/',LoginView.as_view(),name='login'),
    path('logout/',log_out,name='logout'),
    path('register/',RegisterView.as_view(),name='register'),

]
