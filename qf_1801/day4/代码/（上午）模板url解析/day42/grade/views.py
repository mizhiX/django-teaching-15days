from django.shortcuts import render

from grade.models import Grade


def AllGrade(request):

    gs = Grade.objects.all()

    return render(request, 'grade.html', {'gs':gs})
