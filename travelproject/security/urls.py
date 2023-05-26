
from . import views

from django.urls import path
app_name='security'

urlpatterns = [

    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]
