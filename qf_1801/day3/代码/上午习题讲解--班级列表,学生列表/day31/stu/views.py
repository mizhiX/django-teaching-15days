from django.shortcuts import render

# Create your views here.
from stu.models import Student

def allstu(request):
    g_id = request.GET.get('g_id')
    stus = Student.objects.exclude(g_id=g_id)

    return render(request, 'students.html', {'stus':stus})

