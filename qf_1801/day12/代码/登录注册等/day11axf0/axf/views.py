
from datetime import datetime, timedelta

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from axf.models import MainMustBuy, MainNav, MainShop, \
    MainShow, MainWheel, UserModel, UserTicketModel, \
    OrderModel

from django.core.urlresolvers import reverse

from utils.functions import get_ticket


def home(request):

    mustbuys = MainMustBuy.objects.all()

    mainnavs = MainNav.objects.all()

    mainwheels = MainWheel.objects.all()

    mainshops = MainShop.objects.all()

    mainshows = MainShow.objects.all()

    data = {
        'mustbuys': mustbuys,
        'mainnavs': mainnavs,
        'mainwheels': mainwheels,
        'mainshops': mainshops,
        'mainshows': mainshows
    }
    return render(request, 'home/home.html', data)


def user_register(request):

    if request.method == 'GET':

        return render(request, 'user/user_register.html')

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        icon = request.FILES.get("icon")

        password = make_password(password)
        user = UserModel.objects.create(
                username=username,
                password=password,
                email=email,
                icon=icon
            )

        return HttpResponseRedirect(reverse('axf:login'))


def mine(request):

    if request.method == 'GET':

        user = request.user
        if user.username:
            orders = user.ordermodel_set.all()

            wait_pay, payed = 0, 0

            for order in orders:
                if order.o_status == 0:
                    wait_pay += 1
                elif order.o_status == 1:
                    payed += 1
                elif order.o_status ==2:
                    pass
            data = {
                'wait_pay': wait_pay,
                'payed': payed
            }
            return render(request, 'mine/mine.html', data)
        return render(request, 'mine/mine.html')


def user_logout(request):

    if request.method == 'GET':
        response = HttpResponseRedirect(reverse('axf:home'))
        ticket = request.COOKIES.get('ticket')
        response.delete_cookie('ticket')

        UserTicketModel.objects.filter(ticket=ticket).delete()

        return response


def user_login(request):
    if request.method == "GET":

        return render(request, 'user/user_login.html')

    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        users = UserModel.objects.filter(username=username)

        if users.exists():
            user = users.first()
            if check_password(password, user.password):
                ticket = get_ticket()
                out_time = datetime.now() + timedelta(days=1)

                response = HttpResponseRedirect(reverse("axf:mine"))
                response.set_cookie('ticket', ticket, expires=out_time)
                return response

        return HttpResponseRedirect(reverse("axf:user_login"))





