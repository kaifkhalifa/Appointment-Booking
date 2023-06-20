from django.contrib import admin
from django.urls import path, include
from appointment.views import appointment_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', appointment_list, name='appointment_list'),
]


