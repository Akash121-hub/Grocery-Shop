from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('index/', views.index, name='index'),
    path('add/', views.add_products, name='add'),
    path('update/<int:order_id>/', views.upadte_item, name='update'),
    path('update-and-save/<int:pk>/', views.upadte_item_and_save, name='update_and_save'),
    path('delete/<int:pk>/', views.delete_item, name='delete'),
    path('search/', views.search, name='search'),
]