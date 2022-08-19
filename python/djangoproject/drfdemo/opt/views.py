import json
from django.views import View
from rest_framework.authentication import SessionAuthentication,BaseAuthentication
from rest_framework.views import APIView
from drfdemo.permissions import IsXiaoMingPermission
from rest_framework.response import Response
import os
# Create your views here.

class ExampleView(APIView):
    authentication_classes = [SessionAuthentication]

    def get(self,request):
        print(request.user)
        if request.user.id:
            print("通过认证")
        else:
            print("未通过认证")
        return Response({"msg":"ok"})


from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
class HomeInfoAPIView(APIView):
    # 内置权限
    # permission_classes = [IsAuthenticatedOrReadOnly]  # 只能看
    #
    permission_classes = [IsXiaoMingPermission]
    def get(self,request):
        return Response({"msg": "ok"})

    def post(self, request):
        return Response({"msg": "ok"})


from rest_framework.viewsets import ModelViewSet
from stuapi.models import Student
from students.serializers import StudentModelSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class Demo4APIView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    filter_backends = [OrderingFilter,DjangoFilterBackend]
    filter_fields = ["sex", "classmate"]
    ordering_fields = ['id','age']


from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
class Demo5APIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    # 局部分页
    pagination_class = PageNumberPagination

class Demo6APIView(APIView):
    def get(self,request):
        os.system("python3 --version")
        os.system("pip3 list | grep drf")
        return Response({"msg":"ok"})


from drfdemo import settings
class TestSetting(View):
    def get(self,request):
        print(settings.REST_FRAMEWORK)
        return json.dumps({"msg":"ok"})