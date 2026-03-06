
from django.contrib import admin
from django.urls import path

from women.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/womenlist/', WomenAPIList.as_view()),
    path('api/v1/womenlist/<int:pk>/', WomenAPIUpdate.as_view()), # Мы пишем .as_view потому что Django ожидает увидеть функцию в вьювсах, а мы пишем классы (.as_view позволяет подружить классы с django)
    path('api/v1/womendetail/<int:pk>/', WomenAPIDetailView.as_view()),
]