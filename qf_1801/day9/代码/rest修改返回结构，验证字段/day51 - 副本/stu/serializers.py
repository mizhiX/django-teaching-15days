
from rest_framework import serializers

from stu.models import Student


class StudentSerializer(serializers.ModelSerializer):

    s_name = serializers.CharField(error_messages={
        'blank': '用户名不能为空',
        'max_length': '用户名不能超过10个字符串'
    }, max_length=10)
    s_tel = serializers.CharField(error_messages={
        'blank': '电话不能为空'
    })

    class Meta:
        model = Student
        fields = ['id', 's_name', 's_tel']

    def to_representation(self, instance):

        data = super().to_representation(instance)
        try:
            data['s_addr'] = instance.studentinfo.i_addr
        except Exception as e:
            data['s_addr'] = ''
        return data

