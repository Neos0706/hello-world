from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


from stuapi.models import Student
from .serializer import StudentModelSerializer



"""
GET /demo/students/ 
POST /demo/students/

GET /demo/students/<pk>
PUT /demo/students/<pk>
DELETE /demo/students/<pk>

"""

"""APIView基本视图类"""
class StudentAPIView(APIView):
    def get(self,request):
        # 1 从数据库获取数据模型
        student_list = Student.objects.all()
        # 2  实例化序列器，获取序列化对象
        serializer = StudentModelSerializer(instance=student_list, many=True)
        # 3  转换数据，并返回给客户端
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        # 1获取客户端数据， 实例化序列器 ，生成序列化对象
        serializer = StudentModelSerializer(data=request.data)
        # 2 反序列化[数据验证,并保存到数据库]
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 返回结果
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)


class StudentInfoAPIView(APIView):
    """对单条数据进行操作"""
    def get(self, request, pk):
        # 1 从数据库获取数据模型
        instance = get_object_or_404(Student, pk=pk)
        # 2  实例化序列器，获取序列化对象
        serializer = StudentModelSerializer(instance=instance)
        # 3  转换数据，并返回给客户端
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        # 1 从数据库获取数据模型
        instance = get_object_or_404(Student, pk=pk)
        # 2  实例化序列器，获取序列化对象,并提供数据修改
        serializer = StudentModelSerializer(instance=instance, data=request.data)
        # 3 数据验证并保存
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 4   转换数据，并返回给客户端
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def delete(self,request,pk):
        # 1从数据库获取数据并删除
        get_object_or_404(Student, pk=pk).delete()
        # 2 返回
        return Response(status=status.HTTP_204_NO_CONTENT)


"""GenericAPIView基本视图类"""
class StudentGenericAPIView(GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    def get(self,request):
        # 1 从数据库获取数据模型
        queryset = self.get_queryset()   # GenericAPIView提供
        # 2 序列化
        serializer = self.get_serializer(instance=queryset,many=True)
        # 3  转换数据，并返回给客户端
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        # 1获取客户端数据， 实例化序列器 ，生成序列化对象
        serializer = self.get_serializer(data=request.data)
        # 2 反序列化[数据验证,并保存到数据库]
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 返回结果
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class StudentInfoGenericAPIView(GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request, pk):
        # 1 从数据库获取数据模型
        instance = self.get_object()  # 内部已经实现get_object_or_404()
        # 2  实例化序列器，获取序列化对象
        serializer = self.get_serializer(instance=instance)
        # 3  转换数据，并返回给客户端
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        # 1 从数据库获取数据模型
        instance = self.get_object()
        # 2  实例化序列器，获取序列化对象,并提供数据修改
        serializer = self.get_serializer(instance=instance, data=request.data)
        # 3 数据验证并保存
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 4   转换数据，并返回给客户端
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def delete(self,request,pk):
        # 1从数据库获取数据并删除
        self.get_object().delete()
        # 2 返回
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
使用drf内置的模型拓展类[混入类]结合GenericAPIView 实现通用视图方法的简写
from rest_framework.mixins import ListModelMixin  #  获取多条数据，返回响应结果   list 
from rest_framework.mixins import CreateModelMixin   #  添加一条数据，返回响应结果  create
from rest_framework.mixins import RetrieveModelMixin  #  获取一条数据，返回响应结果  retrie
from rest_framework.mixins import UpdateModelMixin   #  更新一条数据，返回响应结果  update(更新全部字段)
from rest_framework.mixins import DestroyModelMixin  #  销毁一条数据，返回响应结果  destory
"""

from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

class StudentMixinView(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    def get(self,request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class StudentInfoMixinView(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    def get(self, request,pk):
        return self.retrieve(request,pk=pk)

    def put(self,request, pk):
        return self.update(request,pk=pk)

    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


"""
视图子类是通用视图类和模型拓展类的子类
视图子类，提供了各种的视图方法调用minxins操作

    ListAPIView = GenericAPIView + ListModelMixin   获取多条数据的视图方法
    CreateAPIView = GenericAPIView + CreateModelMixin   添加一条数据的视图方法
    RetrieveAPIView = GenericAPIView + RetrieveModelMixin   获取一条数据的视图方法
    UpdateAPIView = GenericAPIView + UpdateModelMixin   更新一条数据的视图方法
    DestroyAPIView = GenericAPIView + DestroyModelMixin   销毁一条数据的视图方法
组合视图子类
    ListCreateAPIView = ListAPIView + CreateAPIView
    RetrieveUpdateAPIView = RetrieveAPIView + UpdateAPIView
    RetrieveDestroyAPIView = RetrieveAPIView + DestroyAPIView 
    RetrieveUpdateDestroyAPIView = RetrieveAPIView + UpdateAPIView + DestroyAPIView 
"""

from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,RetrieveUpdateDestroyAPIView
class StudentView(ListAPIView,CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


# class StudentInfoView(RetrieveAPIView, UpdateAPIView, DestroyAPIView ):
class StudentInfoView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


"""
考虑路由问题
get重复问题

ViewSet  -->  基本视图集APIView中的代码重复问题
GenericViewSet -->通用视图集 基本视图集APIView中的代码重复问题,同时让代码更加通用
"""

class StudentViewSet(ViewSet):
    def get_list(self,request):
        # 1 从数据库获取数据模型
        student_list = Student.objects.all()
        # 2  实例化序列器，获取序列化对象
        serializer = StudentModelSerializer(instance=student_list, many=True)
        # 3  转换数据，并返回给客户端
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        # 1获取客户端数据， 实例化序列器 ，生成序列化对象
        serializer = StudentModelSerializer(data=request.data)
        # 2 反序列化[数据验证,并保存到数据库]
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 返回结果
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get_student_info(self,request ,pk):
        # 1 从数据库获取数据模型
        instance = get_object_or_404(Student, pk=pk)
        # 2  实例化序列器，获取序列化对象
        serializer = StudentModelSerializer(instance=instance)
        # 3  转换数据，并返回给客户端
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def update(self,request,pk):
        # 1 从数据库获取数据模型
        instance = get_object_or_404(Student, pk=pk)
        # 2  实例化序列器，获取序列化对象,并提供数据修改
        serializer = StudentModelSerializer(instance=instance, data=request.data)
        # 3 数据验证并保存
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 4   转换数据，并返回给客户端
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def delete(self,request,pk):
        # 1从数据库获取数据并删除
        get_object_or_404(Student, pk=pk).delete()
        # 2 返回
        return Response(status=status.HTTP_204_NO_CONTENT)



"""GenericViewSet 通用视图集"""
from rest_framework.viewsets import GenericViewSet
class StudentGenericViewSet(GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def list(self,request):
        # 1 从数据库获取数据模型
        queryset = self.get_queryset()  # GenericAPIView提供
        # 2 序列化
        serializer = self.get_serializer(instance=queryset, many=True)
        # 3  转换数据，并返回给客户端
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self,request):
        # 1获取客户端数据， 实例化序列器 ，生成序列化对象
        serializer = self.get_serializer(data=request.data)
        # 2 反序列化[数据验证,并保存到数据库]
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 返回结果
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self,request,pk):
        # 1 从数据库获取数据模型
        instance = self.get_object()  # 内部已经实现get_object_or_404()
        # 2  实例化序列器，获取序列化对象
        serializer = self.get_serializer(instance=instance)
        # 3  转换数据，并返回给客户端
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def update(self,request,pk):
        # 1 从数据库获取数据模型
        instance = self.get_object()
        # 2  实例化序列器，获取序列化对象,并提供数据修改
        serializer = self.get_serializer(instance=instance, data=request.data)
        # 3 数据验证并保存
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 4   转换数据，并返回给客户端
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self,request,pk):
        # 1从数据库获取数据并删除
        self.get_object().delete()
        # 2 返回
        return Response(status=status.HTTP_204_NO_CONTENT)


"""GenericViewSet 通用视图集 + 混入类"""
class StudentMixinViewSet(GenericViewSet,ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin ):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


"""
上面的借口类继承的父类太多
可以合并视图集让视图继承
ReadOnlyModelViewSet = GenericViewSet + ListModelMixin + RetrieveModelMixin
ModelViewSet = ReadOnlyModelViewSet + CreateModelMixin+ UpdateModelMixin+ DestroyModelMixin
"""
from  rest_framework.viewsets import ReadOnlyModelViewSet

class StudentReadonlyMixinViewSet(ReadOnlyModelViewSet, CreateModelMixin, UpdateModelMixin,DestroyModelMixin ):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    #路由对象给视图集生成路由信息时，只会生成5个基本的api接口，这主要是router只识别5个混入类的原因
    # 而自定义的视图方法，路由对象不会自动生成路由信息
    # 必须通过action装饰器
    @action(methods=['get'], detail=False)
    def login(self,request):
        """登录视图"""
        #可以通过self.method 获取http请求
        # 可以通过self.action 获取本次客户端请求的视图方法名[viewSet提供的]
        print(self.action)
        return Response({"msg":"登录成功"})
