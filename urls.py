from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('explore',views.explore,name="explore"),
    path('explore/arrays',views.arrays,name="array"),
    path('arrays/intro',views.intro,name="intro"),
    path('arrays/operations',views.basic,name="basic"),
    path('arrays/types',views.types,name="types"),
    path('arrays/initialize',views.initialize,name="initialize"),
    path('arrays/prosandcons',views.prosandcons,name="prosandcons")
]