from django.shortcuts import render

from grade.models import Student


def AllStu(request, g_id):

    stus = Student.objects.filter(g_id=g_id)

    return render(request, 'students.html', {'stus': stus})
