from rest_framework import serializers
from school.models import Teacher,Student,Achievement,Course


class TeacherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class AchievementModelSerializer(serializers.ModelSerializer):
    # course = CourseModelSerializer()
    course_name = serializers.CharField(source="course.name")
    class Meta:
        model = Achievement
        fields = ["id","course_name", "score","create_dtime"]




class StudentModelSerializer(serializers.ModelSerializer):
    # s_achievement = AchievementModelSerializer(many=True)  # 模型中声明的外键字段，非外键字段不能指定序列化器
    class Meta:
        model = Student
        # 默认情况下，模型经过序列化器的数据转换，对于外键的信息，仅仅把数据库里面的外键id返回
        fields = ["id","name","achievement"]