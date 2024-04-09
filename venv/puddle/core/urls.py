from django.urls import path,include
from django.contrib.auth  import views as auth_views
from.import views

from.forms import LoginForm

app_name='core'

urlpatterns = [
    
    path("",views.index),
    path("contact/",views.contact,name="contact"),
    path("signup",views.signup,name="signup"),
    # path("login",auth_views.LoginView.as_view(authentication_form=LoginForm), name="login"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path("/Logout", views.logout, name="logout"),
    ]