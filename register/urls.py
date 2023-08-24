from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import signupPage,loginPage ,homePage,logoutPage
# from .views import home  , register , login_user, logout_user
# urlpatterns = [
#     path('home/',home, name='home'),

#     path('register/',register, name='register'),
#     path('login/',login_user, name='login_user'),
#     path('login/',logout_user, name='logout_user'),

# ]

urlpatterns = [

path('',signupPage,name='signup'),
path('login/',loginPage,name='login'),
path('home/',homePage,name='home'),
path('logout/',logoutPage,name='logout'),
]