
from rest_framework import serializers

from app.models import Student, Grade


class StudentSerializer(serializers.ModelSerializer):

    s_name = serializers.CharField(max_length=20, error_messages={
        'blank': '姓名字段不能为空'
    })

    class Meta:
        model = Student
        fields = ['s_name', 's_yuwen', 'g', 'id', 's_shuxue']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['g_name'] = instance.g.g_name

        return data


class GradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grade
        fields = ['id', 'g_name']

    def do_update(self, instance, validated_data):

        instance.g_name = validated_data['g_name']
        instance.save()
        data = self.to_representation(instance)

        return data
