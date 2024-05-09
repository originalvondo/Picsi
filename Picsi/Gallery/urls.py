from django.urls import path 
from . import views

app_name = "Gallery"

urlpatterns = [
    path('', views.index, name="home"),
    path('pic/<int:id>', views.pic, name="pic"),
    path('pic/<int:id>/delete', views.delete_pic, name="delete"),
    path('create_pic/', views.CreatePic.as_view(), name="create")
]