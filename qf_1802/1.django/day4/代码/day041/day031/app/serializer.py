
from rest_framework import serializers

from app.models import Student


class StudentSerializer(serializers.ModelSerializer):

    s_name = serializers.CharField(max_length=20, error_messages={
        'blank': '姓名字段不能为空'
    })

    class Meta:
        model = Student
        fields = ['s_name', 's_yuwen', 'g', 'id']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['g_name'] = instance.g.g_name

        return data


