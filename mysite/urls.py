from django.contrib import admin
from django.urls import path
from .views import index
from users.views import login_view, register_view, logout_view

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
