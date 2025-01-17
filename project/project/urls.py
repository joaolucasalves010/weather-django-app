from django.contrib import admin
from django.urls import path
from weather import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('get_city', views.get_city, name="get_city"),
]
