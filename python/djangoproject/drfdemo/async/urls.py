from django.urls import path
from . import views
urlpatterns = [
    path('s1/', views.home1),
    path('s2/',views.home2),
    path('s3/', views.home3),
    path('s4/', views.home4),

]