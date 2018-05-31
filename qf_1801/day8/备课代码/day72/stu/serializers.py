
from rest_framework import serializers

from stu.models import Student

# 获取学生表里面的信息
class StuSerializers(serializers.ModelSerializer):

    class Meta:
        # 指定数据库
        model = Student
        # 指定返回给用户的具体表中的哪些字段
        fields = ['s_name', 's_tel']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            data['i_adddr'] = instance.studentinfo.i_addr
        except Exception as e:
            data['i_adddr'] = ''
        return data
