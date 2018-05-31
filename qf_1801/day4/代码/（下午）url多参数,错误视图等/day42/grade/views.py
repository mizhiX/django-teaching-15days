from django.shortcuts import render

from grade.models import Grade

def AllGrade(request):

    gs = Grade.objects.all()

    return render(request, 'grade.html', {'gs':gs})


def page_not_found(request):

    return render(request, '404.html')

def server_error(request):

    return render(request, '500.html')
