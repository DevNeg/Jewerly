from django.contrib import admin
from django.urls import path, include
from base import views

urlpatterns = [
    path('',views.home),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('base/', include ('base.urls')),
]
