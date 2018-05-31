# -*- coding:utf-8 -*—
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render

from stu.models import Student, StudentInfo, GoodsUser, Goods
from grade.models import Grade

def addStu(request):
    if request.method == 'GET':
        return render(request, 'addstu.html')

    if request.method == 'POST':
        # 创建学生信息
        stu_name = request.POST.get('name')
        if request.POST.get('sex') == '男':
            stu_sex = 1
        else:
            stu_sex = 0
        stu_birth = request.POST.get('birth')
        stu_yuwen = request.POST.get('yuwen')
        stu_shuxue = request.POST.get('shuxue')
        Student.objects.create(
            stu_name = stu_name,
            stu_sex = stu_sex,
            stu_birth = stu_birth,
            stu_yuwen = stu_yuwen,
            stu_shuxue = stu_shuxue
        )
        return render(request, 'addstu.html')

def selStu(request):
    # 通过扩展表学生的地址去查找学生的信息
    # 查找addr = 成都天府新区的学生信息
    # 方法1
    # stus = StudentInfo.objects.filter(stu_addr='成都天府新区111号')
    # stu = stus[0]
    # selstu = Student.objects.filter(id=stu.id)
    # 方法2
    # stus = StudentInfo.objects.filter(stu_addr__contains='成都天府新区')
    # stu = stus[0]
    # selstu = stu.stu

    # 通过学生表去查找学生拓展表的信息
    # 查找stu_name=狄仁杰的学生的家庭住址
    # 方法1
    """
    select * from studentinfo s1 join
     (select i_d from student where stu_name='狄仁杰') t1
     on s1.stu_id = t1.id
    """
    # stu = Student.objects.filter(stu_name='大乔').first()
    # selstu = StudentInfo.objects.filter(stu_id=stu.id)

    # 方法2
    # stu = Student.objects.filter(stu_name='狄仁杰').first()
    # selstu = stu.studentinfo
    # selstu = stu.stu_info

    # 查询语文成绩小于80分的学生的地址信息

    # 查询80后的学生的所有的信息


    # 查询语文成绩小于80分的学生的所有信息

    selstu = Student.objects.all()

    return render(request, 'selstu.html', {'selstu':selstu})

def fselStu(request):

    # 查询python班级下的学生
    # 方法1
    # g = Grade.objects.get(g_name='python')
    # stus = Student.objects.filter(g_id=g.id)
    # 方法2
    # g = Grade.objects.get(g_name='python')
    # stus = g.student_set.all()

    # 查询叫李白的同学的班级信息
    # stu = Student.objects.get(stu_name='李白')
    # gs = stu.g

    # 查询python班下语文成绩大于80分的学生
    g = Grade.objects.get(g_name='python')
    stus = g.student_set.filter(stu_yuwen__gte=80)

    # 查询python班级中出生在80后的男生的信息
    g = Grade.objects.get(g_name='python')
    g.student_set.filter(stu_birth__gte='1980-01-01',
                         stu_birth_lt='1990-01-01',
                         stu_sex=True)

    # 查询python班级下语文成绩超过数学成绩10分的男同学信息
    g = Grade.objects.get(g_name='python')
    g.student_set.filter(stu_yuwen__gte=F('stu_shuxue') + 10)


    return render(request, 'selgrade.html', {'stus':stus})


def manyGoods(request):

    # 获取小乔购买的商品
    u = GoodsUser.objects.filter(u_name='小乔')[0]
    goods = u.goods_set.all()

    # 获取购买娃哈哈用户的信息
    g = Goods.objects.get(g_name='娃哈哈')
    users = g.g_user.all()

    return render(request, 'goods.html',
                  {'goods':goods, 'users': users})

def allStudent(request):

    # stus = Student.objects.filter(id=100)
    stus = Student.objects.all()
    return render(request, 'all_stus.html',
                  {'stus': stus}
                  )