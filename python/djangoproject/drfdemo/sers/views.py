import json
from django.views import View
from .serializer import Student1Serializer, Student2Serializer,StudentModelSerializer
from django.http.response import JsonResponse
from stuapi.models import Student
from django.shortcuts import get_object_or_404
# Create your views here.

class Student1View(View):

    def get1(self,request):
        """序列化器-序列化阶段的调用"""
        # 1 获取一条数据
        instance = Student.objects.first()

        # 2 实例化序列化器，得到序列化对象
        serializer = Student1Serializer(instance=instance)
        # 3 调用序列化对象的data属性方法获取转换后的数据
        data = serializer.data
        # 4 响应数据
        return JsonResponse(data=data, status=200, safe=False)

    def getAll(self,request):
        """序列化器-序列化阶段的调用"""
        # 1 获取数据集
        student_list = Student.objects.all()

        # 2 实例化序列化器，得到序列化对象  多个模型对象必须为many=True
        serializer = Student1Serializer(instance=student_list,  many=True)
        # 3 调用序列化对象的data属性方法获取转换后的数据
        data = serializer.data
        # 4 响应数据
        return JsonResponse(data=data, status=200, safe=False)

    def get2(self, request):
        """反序列化-采用字段选项来验证数据(不抛出异常)"""

        # 1 接收客户端提交的数据
        # data = json.dumps(request.body)
        data = {
            "name":'小黑',
            "age": 30,
            "sex": True,
            "classmate": "301",
            "description":"yyyyy"
        }
        # 1。1 实例化序列器，获取序列化对象
        serializer = Student2Serializer(data=data)
        # 1。2  调用序列化器进行数据验证
        # 不抛出异常
        ret = serializer.is_valid()
        # # 抛出异常
        # ret = serializer.is_valid(raise_exception=True)
        # 1。3 获取验证以后的结果
        if ret:
            return JsonResponse(dict(serializer.validated_data))
        else:
            return JsonResponse(dict(serializer.errors))
        # 2 操作数据库
        # 3 返回结果

    def get3(self,request):
        """反序列化-采用字段选项来验证数据(抛出异常)"""

        # 1 接收客户端提交的数据
        # data = json.dumps(request.body)
        data = {
            "name": 'pn',
            "age": 30,
            "sex": True,
            "classmate": "309",
            "description":"yyyyy"
        }
        # 1。1 实例化序列器，获取序列化对象
        serializer = Student2Serializer(data=data)
        # 1。2  调用序列化器进行数据验证
        # # 抛出异常
        serializer.is_valid(raise_exception=True)
        # 1。3 获取验证以后的结果
        # 2 操作数据库
        # 3 返回结果
        return JsonResponse(dict(serializer.validated_data))

    def get4(self, request):
        """反序列化-添加数据入库"""

        # 1 接收客户端提交的数据
        # data = json.dumps(request.body)
        data = {
            "name": 'pn',
            "age": 30,
            "sex": True,
            "classmate": "309",
            "description":"yyyyy"
        }
        # 1。1 实例化序列器，获取序列化对象
        # 反序列化 json-> 模型字段
        serializer = Student2Serializer(data=data)
        # 1。2  调用序列化器进行数据验证
        # # 抛出异常
        serializer.is_valid(raise_exception=True)
        # 2 获取验证以后的结果,操作数据库
        serializer.save() #会根据实例化序列器的时候，是否传入instance 来调用create 或者update方法，没传入，调用create，传入instance，调用update

        # 3 返回结果
        return JsonResponse(serializer.data,status=201)

    def get(self,request):
        """反序列化-更新数据入库"""
        # 1 根据client访问的url地址中 获取pk值
        pk = 5
        student = get_object_or_404(Student, pk=pk)
        # 接受客户端提交的修改数据
        data = {
            "name": 'pnsss',
            "age": 30,
            "sex": True,
            "classmate": "309",
            "description": "yyyyy"
        }

        # 3 修改操作中的实例化序列器对象
        serializer = Student2Serializer(instance=student,data=data)
        # 4 验证数据
        serializer.is_valid(raise_exception=True)
        # 5 入库
        serializer.save()
        # 6 返回结果
        return JsonResponse(serializer.data, status=201)

class StudentView(View):

    def get1(self, request):
        """序列化器-序列化阶段的调用"""
        # 1 获取一条数据
        instance = Student.objects.first()
        instance.nickname = "xiaossss"

        # 2 实例化序列化器，得到序列化对象
        serializer = StudentModelSerializer(instance=instance)
        # 3 调用序列化对象的data属性方法获取转换后的数据
        data = serializer.data
        # 4 响应数据
        return JsonResponse(data=data, status=200, safe=False)

    def get2(self, request):
        """序列化器-序列化阶段的调用"""
        # 1 获取数据集
        student_list = Student.objects.all()

        # 2 实例化序列化器，得到序列化对象  多个模型对象必须为many=True
        serializer = StudentModelSerializer(student_list, many=True)
        # 3 调用序列化对象的data属性方法获取转换后的数据
        data = serializer.data
        # 4 响应数据
        return JsonResponse(data=data, status=200, safe=False)

    def get3(self, request):
        """反序列化-采用字段选项来验证数据(不抛出异常)"""

        # 1 接收客户端提交的数据
        # data = json.dumps(request.body)
        data = {
            "name": '小黑',
            "age": 117,
            "sex": True,
            "classmate": "301",
            "description": "yyyyy"
        }
        # 1。1 实例化序列器，获取序列化对象
        serializer = StudentModelSerializer(data=data)
        # 1。2  调用序列化器进行数据验证
        # 不抛出异常
        ret = serializer.is_valid()
        # # 抛出异常
        # ret = serializer.is_valid(raise_exception=True)
        # 1。3 获取验证以后的结果
        if ret:
            return JsonResponse(dict(serializer.validated_data))
        else:
            return JsonResponse(dict(serializer.errors))
        # 2 操作数据库
        # 3 返回结果

    def get4(self, request):
        """反序列化-采用字段选项来验证数据(抛出异常)"""

        # 1 接收客户端提交的数据
        # data = json.dumps(request.body)
        data = {
            "name": 'pn',
            "age": 30,
            "sex": True,
            "classmate": "309",
            "description": "yyyyy"
        }
        # 1。1 实例化序列器，获取序列化对象
        serializer = Student2Serializer(data=data)
        # 1。2  调用序列化器进行数据验证
        # # 抛出异常
        serializer.is_valid(raise_exception=True)
        # 1。3 获取验证以后的结果
        # 2 操作数据库
        # 3 返回结果
        return JsonResponse(dict(serializer.validated_data))

    def get5(self, request):
        """反序列化-添加数据入库"""

        # 1 接收客户端提交的数据
        # data = json.dumps(request.body)
        data = {
            "name": 'pn',
            "age": 19,
            "sex": True,
            "classmate": "309",
            "description": "yyyyy"
        }
        # 1。1 实例化序列器，获取序列化对象
        # 反序列化 json-> 模型字段
        serializer = StudentModelSerializer(data=data)
        # 1。2  调用序列化器进行数据验证
        # # 抛出异常
        serializer.is_valid(raise_exception=True)
        # 2 获取验证以后的结果,操作数据库
        serializer.save()  # 会根据实例化序列器的时候，是否传入instance 来调用create 或者update方法，没传入，调用create，传入instance，调用update

        # 3 返回结果
        return JsonResponse(serializer.data, status=201)

    def get(self, request):
        """反序列化-更新数据入库"""
        # 1 根据client访问的url地址中 获取pk值
        pk = 5
        student = get_object_or_404(Student, pk=pk)
        # 接受客户端提交的修改数据
        data = {
            "name": 'xiaobai',
            "age": 20,
            "sex": True,
            "classmate": "309",
            "description": "yyyyy"
        }

        # 3 修改操作中的实例化序列器对象
        serializer = StudentModelSerializer(instance=student, data=data)
        # 4 验证数据
        serializer.is_valid(raise_exception=True)
        # 5 入库
        serializer.save()
        # 6 返回结果
        return JsonResponse(serializer.data, status=201)
