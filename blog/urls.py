from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), # '' means root and home page is views.post_list
]