"""
URL configuration for watchshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import Home,About,Upload,login_user,signup_user,logout_user,show_product,addtowish,show_wishlist,removewish,show_cart,addtocart,removecart
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   path('',Home,name="home"),
    path('about',About, name="about"),
    path('upload',Upload, name="upload"),
    path('login', login_user , name='login'),
    path('signup', signup_user , name='signup'),
    path('logout', logout_user , name='logout'),
    path('product/<int:id>', show_product , name='product'),
    path('addtowish/<int:id>', addtowish, name ='addtowish'),
    path('show_wishlist', show_wishlist, name ='show_wishlist'),
    path('removewish/<int:id>',removewish, name="removewish"),
    path('show_cart',show_cart, name="show_cart"),
    path('addtocart/<int:id>', addtocart, name ='addtocart'),
    path('removecart/<int:id>',removecart,name="removecart"),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)