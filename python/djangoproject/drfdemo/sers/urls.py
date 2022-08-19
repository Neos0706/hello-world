from django.urls import path,re_path

from . import views

urlpatterns =[
    path("students/", views.StudentView.as_view()),

]