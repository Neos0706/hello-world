from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from .models import Course
from .serializer import CourseModelSerializer

# Create your views here.

class CourseAPIView(APIView):
    def get(self,request):
        instance = Course.objects.all()
        serializer = CourseModelSerializer(instance=instance,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
