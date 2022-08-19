from rest_framework import serializers
from stuapi.models import Student

# 声明序列器类，回头会在视图中调用
class StudentModelSerializer(serializers.ModelSerializer):

    class Meta:
        # 声明该序列化器处理的数据字段从模型参考生成
        model = Student
        #声明该序列化器包含模型类中的哪些数据字段
        fields = "__all__"