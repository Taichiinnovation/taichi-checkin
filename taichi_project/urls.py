from django.contrib import admin
from django.urls import path
from checkin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('checkin/room1', views.checkin, name='checkin'),
    path('coach/room1', views.coach, name='coach'),
]