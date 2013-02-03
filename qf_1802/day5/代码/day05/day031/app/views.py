from django.contrib.auth.models import User
from django.core.paginator import Paginator
from rest_framework.response import Response
from django.db.models import F, Q
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect

from django.core.urlresolvers import reverse
from rest_framework import mixins, viewsets

from app.filters import StudentFilter
from app.models import Grade, Student
from app.serializer import StudentSerializer, GradeSerializer
from day010.settings import PAGE_NUMBERS
from user.models import Users
from utils.functions import is_login

'''
首页
'''
def index(request):

    if request.method == 'GET':
        return render(request, 'index.html')

'''
左侧菜单栏
'''
def left(request):
    if request.method == 'GET':
        return render(request, 'left.html')

'''
班级列表
'''
def grade(request):
    if request.method == 'GET':
        # page_num = request.GET.get('page_num', 1)
        # grades = Grade.objects.all()
        # paginator = Paginator(grades, PAGE_NUMBERS)
        # pages = paginator.page(int(page_num))
        # return render(request, 'grade.html', {'grades':grades, 'pages':pages})
        return render(request, 'grade.html')


'''
添加班级页面
'''
def addgrade(request):
    if request.method == 'GET':
        return render(request, 'addgrade.html')

    if request.method == 'POST':
        # 创建班级信息
        g_name = request.POST.get('grade_name')
        g = Grade()
        g.g_name = g_name
        g.save()
        return HttpResponseRedirect(reverse('app:grade'))



'''
头部页面
'''
def head(request):
    if request.method == 'GET':
        return render(request, 'head.html')

'''
学生列表
'''
def students(request):
    if request.method == 'GET':
        # page_num = request.GET.get('page_num', 1)
        # stus = Student.objects.all().filter(delete=False)
        # paginator = Paginator(stus, PAGE_NUMBERS)
        # pages = paginator.page(int(page_num))
        # return render(request, 'student.html', {'stus':stus, 'pages':pages})
        return render(request, 'student.html')
'''
添加学生信息
'''
def addstu(request):
    if request.method == 'GET':
        grades = Grade.objects.all()
        return render(request, 'addstu.html', {'grades':grades})

    if request.method == 'POST':

        s_name = request.POST.get('s_name')
        g_id = request.POST.get('g_id')

        s_img = request.FILES.get('s_img')
        #  获取班级信息
        grade = Grade.objects.filter(id=g_id).first()
        # 创建学生信息
        # Student.objects.create(s_name=s_name, g_id=grade.id)/
        Student.objects.create(s_name=s_name,
                               g=grade,
                               s_img=s_img)

        # stu = Student(s_name=s_name, g=grade)
        # stu.save()
        return HttpResponseRedirect(reverse('app:student'))


'''
删除学生
'''
def delstu(request):
    if request.method == 'GET':
        s_id = request.GET.get('s_id')
        Student.objects.filter(id=s_id).delete()

        return HttpResponseRedirect(reverse('app:student'))

'''
编辑班级信息
'''
def editgrade(request):

    if request.method == 'GET':
        grade_id = request.GET.get('grade_id')
        return render(request, 'addgrade.html', {'grade_id':grade_id})

    if request.method == 'POST':

        grade_id = request.POST.get('grade_id')
        grade_name = request.POST.get('grade_name')

        g = Grade.objects.filter(pk=grade_id).first()
        g.g_name = grade_name
        g.save()

        return HttpResponseRedirect(reverse('app:grade'))


def selectstu(request):

    # 查询python班下语文成绩超过数学成绩10分的学生
    # grade = Grade.objects.filter(g_name='python').first()
    # students = grade.student_set.all()
    #
    # stu = students.filter(s_yuwen__gt= F('s_shuxue') + 10)

    # 查询python班语文大于等于80或者数学小于等于80的学生
    grade = Grade.objects.filter(g_name='python').first()
    students = grade.student_set.all()

    stu = students.filter(Q(s_yuwen__gte=80) | Q(s_shuxue__lte=80))

    # 查询python班语文小于80并且数学小于等于80的学生
    stu = students.filter(~Q(s_yuwen__gte=80) & Q(s_shuxue__lte=80))

    return HttpResponse('123')


class api_student(mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):

    # 学生的所有信息
    queryset = Student.objects.all().filter(delete=False)
    # 序列化学生的所有信息
    serializer_class = StudentSerializer
    # 过滤
    filter_class = StudentFilter

    def get_queryset(self):

        # query = self.queryset
        # s_name = self.request.query_params.get('s_name')
        # s_yuwen = self.request.query_params.get('s_yuwen')
        # return query.filter(s_name__contains=s_name,
        #                     s_yuwen__gte=s_yuwen)
        return self.queryset.order_by('-id')


    # /app/api/student/[id]/  DELETE
    def perform_destroy(self, instance):
        instance.delete = True
        instance.save()


class api_grade(mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                viewsets.GenericViewSet):

    queryset = Grade.objects.all()

    serializer_class = GradeSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, request.data)
        serializer.is_valid(raise_exception=True)

        serializer.do_update(instance, request.data)
        data = serializer.data
        data['code'] = 200
        data['msg'] = '修改班级成功'
        return Response(data)



def editgradebyapi(request):
    if request.method == 'GET':

        return render(request, 'addgrade.html')