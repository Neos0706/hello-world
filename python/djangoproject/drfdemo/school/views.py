from rest_framework.viewsets import ModelViewSet
from .models import Student,Achievement,Course
from .serializer import StudentModelSerializer,AchievementModelSerializer,CourseModelSerializer
# Create your views here.


class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

class AchievementModelViewSet(ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementModelSerializer


class CourseModelViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer