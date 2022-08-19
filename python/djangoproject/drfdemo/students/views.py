from rest_framework.viewsets import ModelViewSet
from stuapi.models import Student
from .serializers import StudentModelSerializer


# Create your views here.

class StudentViewSet(ModelViewSet):
    # 指明该视图集在查询数据使用的查询集
    queryset = Student.objects.all()
    # 指明该视图在进行序列化或反序列化时使用的序列化器
    serializer_class = StudentModelSerializer
