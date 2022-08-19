from rest_framework.views import APIView
from rest_framework.response import Response
from django.views import View
from django.http.response import HttpResponse
from rest_framework import status

# Create your views here.

class StudentView(View):
    def get(self,request):
        print(f"request={request}") #request=<WSGIRequest: GET '/req/students1/'> ->父类 --> django.http.request.HttpRequest
        return HttpResponse({"msg": "ok"})

class StudentAPIView(APIView):
    def get(self, request):
        print(f"drg.request={request}") #request=<rest_framework.request.Request: GET '/req/students11/'> 属于drf单独声明的请求处理对象，与django的Httprequest无继承关系
        print(f"django.request={request._request}") #WSGIRequest
        # print(f"request.data={request.data}")
        # print(f"request.query_params={request.query_params}")
        return Response({"msg": "ok"}, status=status.HTTP_201_CREATED)

    def post(self,request):
        """获取请求体数据"""
        # 客户端提供的json数据  request.data={'name': 'xoap'}
        #  客户端提供的表单数据 request.data=<QueryDict: {'name': ['xiaoming']}>
        print(f"request.data={request.data}")

        """获取查询字符串"""
        print(f"request.query_params={request.query_params}")
        return Response({"msg": "ok"})

    def put(self, request):
        # 获取请求体数据
        return Response({"msg": "ok"})

    def patch(self, request):
        # 更新部分数据
        return Response({"msg": "ok"})

    def delete(self, request):
        # 删除操作
        return Response({"msg": "ok"})