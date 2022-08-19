from rest_framework import serializers
from stuapi.models import Student
"""
serializers 是drf提供给开发者调用的序列化器模块
Serializer 序列化器基类
ModelSerializer 模型序列化器基类
"""

class Student1Serializer(serializers.Serializer):
    """学生信息序列化器"""
    # 1转换的字端声明
    # 字段 = serializers.字段类型(选项=选项值)
    id = serializers.IntegerField()
    name = serializers.CharField()
    sex = serializers.BooleanField()
    age = serializers.IntegerField()
    description = serializers.CharField()

def check_classmate(data):
    """外部验证函数"""
    if len(data) != 3:
        raise serializers.ValidationError(detail="班级编号不正确", code="check_classmate")
    return data


class Student2Serializer(serializers.Serializer):
    """学生信息序列化器"""
    # 1转换的字端声明
    # 字段 = serializers.字段类型(选项=选项值)
    id = serializers.IntegerField(read_only=True)  # read_only=True在客户端提交数据（反序列化阶段不会要求id字段）
    name = serializers.CharField(required=True)   # required=True 反序列化必填
    sex = serializers.BooleanField(default=True)
    age = serializers.IntegerField(max_value=100, min_value=0, error_messages={"min_value": "值必须大于等于0"})
    classmate = serializers.CharField(validators=[check_classmate])
    description = serializers.CharField(allow_null=True, allow_blank=True)

    # 2 如果当前序列化器继承的是ModelSerializer ,则需要声明调用的模型信息
    # class Meta:
    #     model = 模型
    #     fields = ["字段1","字段2",...]
    # 3 验证代码的对象方法
    def validate(self, attrs): # validate是固定的
        """
        验证来自client的所有数据
        """
        if attrs['classmate'] == "307" and attrs["sex"]:
            raise serializers.ValidationError(detail="307只能进去小姐姐", code="validate")
        return attrs

    def validate_name(self, data):
        """验证单个字符
        方法名的格式必须以validtae_<字段名>为名称，否则序列化不识别
        validtae开头的方法，会自动被is_valid 调用的
        """
        if data in ["python", "django"]:
            raise serializers.ValidationError(detail="学生姓名不能为python",code="validate_name")
        # 验证成功后必须返回数据
        return data

    # 4  模型操作的方法
    def create(self, validated_data):
        """
        添加数据
        添加数据操作方法，方法名固定为create ，固定参数validated_data 就是验证成功以后的结果
        添加数据以后，就自动实现了从字典变成模型对象的过程
        """
        student = Student.objects.create(**validated_data)
        return student

    def update(self, instance, validated_data): # 更新数据操作，更新数据以后，就自动实现了从字典变成模型对象的过程
        """
         更新数据操作，
         方法名固定为update
         固定参数instance 实例化序列器对象时，必须传入的模型对象
         固定参数validated_data 就是验证成功以后的结果
         更新数据以后，就自动实现了从字典变成模型对象的过程
        """
        instance.name = validated_data["name"]
        instance.age = validated_data["age"]
        instance.sex = validated_data["sex"]
        instance.classmate = validated_data["classmate"]
        instance.description = validated_data["description"]
        instance.save() # 调用模型对象的save(),和视图中serializer.save()不是同一个类的方法
        return instance


class StudentModelSerializer(serializers.ModelSerializer):
    """学生信息序列化器"""
    # 1转换的字端声明
    # 可以增加模型里没有的字段
    nickname = serializers.CharField(read_only=True)
    # 2 如果当前序列化器继承的是ModelSerializer ,则需要声明调用的模型信息
    class Meta:
        model = Student
        fields = ['id','name','sex','age','nickname']   # 必填  字符串和列表，元祖 '__all__'
        # exclude = ['description']    # 选填 排除那些字段 与fields互斥
        # read_only_fields = []   # 选填  这里设置的字段只会在序列化阶段采用
        extra_kwargs = { # 选填 字段额外选项声明
            "age": {
                "max_value": 20,
                "min_value":5,
                "error_messages": {
                        "max_value": "年龄的最大值必须小于20",
                },
            }

        } # 选填 字段额外选项声明
    # 3 验证代码的对象方法
    # 4  模型操作的方法
