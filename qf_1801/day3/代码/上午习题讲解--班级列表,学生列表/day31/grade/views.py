from django.shortcuts import render

# Create your views here.

from grade.models import Grade

def allgrade(request):
    grages = Grade.objects.all()

    return render(request, 'grades.html', {'grages':grages})
