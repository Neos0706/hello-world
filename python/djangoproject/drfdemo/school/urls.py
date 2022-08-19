from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('students',views.StudentModelViewSet,basename='students')
router.register('achievements',views.AchievementModelViewSet,basename='achievements')
router.register('courses',views.CourseModelViewSet,basename='courses')
urlpatterns=[

] + router.urls