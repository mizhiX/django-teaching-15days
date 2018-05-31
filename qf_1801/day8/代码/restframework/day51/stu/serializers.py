
from rest_framework import serializers

from stu.models import Student


class StudentSerializer(serializers.ModelSerializer):

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

