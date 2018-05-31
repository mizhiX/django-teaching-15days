from django.shortcuts import render

def showGrades(request):

    return render(request, 'index.html')