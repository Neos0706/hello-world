from rest_framework import serializers
from stuapi.models import Student

class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        extra_kwargs = {
            "age": {
                "max_value": 20,
                "min_value": 5,
                "error_messages": {
                    "max_value": "年龄的最大值必须小于20，最大值大于5",
                }
            }
        }