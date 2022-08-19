from rest_framework.routers import DefaultRouter
from .import views

# 路由列表
router = DefaultRouter() #可以处理视图的路由器
router.register('students2', views.StudentViewSet, basename='students2') # 向路由器注册视图集

urlpatterns = [] + router.urls #将路由器的路由信息追加到django的路由列表中