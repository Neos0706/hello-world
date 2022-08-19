from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
router = DefaultRouter() #可以处理视图的路由器
router.register('demo4', views.Demo4APIView, basename='demo4') # 向路由器注册视图集
urlpatterns = [
    path('example/',views.ExampleView.as_view()),
    path('home/info/',views.HomeInfoAPIView.as_view()),
    path('demo5/', views.Demo5APIView.as_view()),
    path('test/',views.TestSetting.as_view()),
    path('demo6/', views.Demo6APIView.as_view()),
] + router.urls