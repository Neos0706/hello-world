from django.urls import path,re_path
from . import views

urlpatterns = [
    # APIView
    path('students/', views.StudentAPIView.as_view()),
    re_path('^students/(?P<pk>\\d+)/$', views.StudentInfoAPIView.as_view()),
    # GenericAPIView
    path('students2/', views.StudentGenericAPIView.as_view()),
    re_path('^students2/(?P<pk>\\d+)/$', views.StudentInfoGenericAPIView.as_view()),
    # GenericAPIView + mixin
    path('students3/', views.StudentMixinView.as_view()),
    re_path('^students3/(?P<pk>\\d+)/$', views.StudentInfoMixinView.as_view()),
    # 视图子类
    path('students4/', views.StudentView.as_view()),
    re_path('^students4/(?P<pk>\\d+)/$', views.StudentInfoView.as_view()),
    #视图集 viewSet
    path('students5/', views.StudentViewSet.as_view({
        "get":"get_list",
        "post":"post", # 视图类方法，可以是原来的http请求，也可以是自定义的方法名
    })),
    re_path('^students5/(?P<pk>\\d+)/$', views.StudentViewSet.as_view({
        "get":"get_student_info",
        "put":"update",
        "delete":"delete"
    })),
    # 通用视图集 GenericViewSet
    path('students6/', views.StudentGenericViewSet.as_view({
        "get":"list",
        "post":"create", # 视图类方法，可以是原来的http请求，也可以是自定义的方法名
    })),
    re_path('^students6/(?P<pk>\\d+)/$', views.StudentGenericViewSet.as_view({
        "get":"retrieve",
        "put":"update",
        "delete":"destroy"
    })),
    # 视图集 全部添加
    path('students7/', views.StudentMixinViewSet.as_view({
        "get":"list",
        "post":"create", # 视图类方法，可以是原来的http请求，也可以是自定义的方法名
    })),
re_path('^students7/(?P<pk>\\d+)/$', views.StudentMixinViewSet.as_view({
        "get":"retrieve",
        "put":"update",
        "delete":"destroy"
    })),
    path('students8/', views.StudentReadonlyMixinViewSet.as_view({
        "get":"list",
        "post":"create", # 视图类方法，可以是原来的http请求，也可以是自定义的方法名
    })),
    re_path('^students7/(?P<pk>\\d+)/$', views.StudentReadonlyMixinViewSet.as_view({
        "get":"retrieve",
        "put":"update",
        "delete":"destroy"
    })),
]

# 自动生成路由信息[和视图集配合]
from rest_framework.routers import SimpleRouter, DefaultRouter
# 1 实例化路由类
router = DefaultRouter()

# 2 给路由注册路由集
router.register("student9",views.StudentModelViewSet,basename="student9")

# 3 把生成的路由列表 和urlpatterns进行拼接
print(router.urls)
urlpatterns += router.urls
