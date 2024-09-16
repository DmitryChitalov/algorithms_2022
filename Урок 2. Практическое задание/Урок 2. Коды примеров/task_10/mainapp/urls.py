from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.products, name='index'),
    path('page/<int:page>/', views.products, name='page'),
    path('<str:category_slug>/',
         views.products,
         name='category'),
    path('product/<str:slug>/',
         views.product_detail,
         name='details'),
]