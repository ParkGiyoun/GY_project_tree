from django.urls import path
from . import views

urlpatterns = [
    path('', views.LinkList.as_view()),

]