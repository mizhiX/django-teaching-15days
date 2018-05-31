
from datetime import datetime, timedelta

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse

from axf.models import MainMustBuy, MainNav, MainShop, \
    MainShow, MainWheel, UserModel, UserTicketModel, \
    FoodType, Goods, CartModel, OrderModel, OrderGoodsModel

from utils.functions import get_ticket

def home(request):

    mustbuys = MainMustBuy.objects.all()

    mainnavs = MainNav.objects.all()

    mainwheels = MainWheel.objects.all()

    mainshops = MainShop.objects.all()

    data = {
        'mustbuys': mustbuys,
        'mainnavs': mainnavs,
        'mainwheels': mainwheels,
        'mainshops': mainshops
    }
    return render(request, 'home/home.html', data)


def user_register(request):

    if request.method == 'GET':

        return render(request, 'user/user_register.html')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        icon = request.FILES.get('icon')

        password = make_password(password)

        UserModel.objects.create(username=username,
                                 password=password,
                                 email=email,
                                 icon=icon)

        return HttpResponseRedirect(reverse('axf:login'))
        # return render(request, 'user/user_login.html')


def user_login(request):

    if request.method == 'GET':

        return render(request, 'user/user_login.html')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        # 验证用户是否存在
        users = UserModel.objects.filter(username=username)
        if users:
            # 教验密码
            if check_password(password, users[0].password):

                # 设置cookie
                response = HttpResponseRedirect(reverse('axf:mine'))
                ticket = get_ticket()
                out_time = datetime.now() + timedelta(days=1)
                response.set_cookie('ticket', ticket, expires=out_time)

                # 服务端存时间
                UserTicketModel.objects.create(user=users[0],
                                               ticket=ticket,
                                               out_time=out_time)
                return response
        else:
            return render(request, 'user/user_login.html')


def user_mine(request):

    if request.method == 'GET':

        user = request.user
        data = {}
        # annoyUser  id='' username=''   django_session, django_auth


        if user and user.id:
            orders = user.ordermodel_set.all()

            wait_pay, payed = 0, 0

            for order in orders:

                if order.o_status == 0:
                    wait_pay += 1
                elif order.o_status == 1:
                    payed += 1

            data['wait_pay'] = wait_pay
            data['payed'] = payed

        return render(request, 'mine/mine.html', data)


def user_logout(request):

    if request.method == 'GET':
        # 删除cookie
        response = HttpResponseRedirect(reverse('axf:home'))
        response.delete_cookie('ticket')
        # 删除user_ticket
        ticket = request.COOKIES.get('ticket')
        UserTicketModel.objects.filter(ticket=ticket).delete()

        return response


def user_cart(request):

    if request.method == 'GET':

        user = request.user
        if user and user.id:

            carts = CartModel.objects.filter(user=user)

            data = {
                'carts': carts
            }

            return render(request, 'cart/cart.html', data)
        else:
            return HttpResponseRedirect(reverse('axf:login'))


def user_market(request):

    if request.method == 'GET':

        return HttpResponseRedirect(reverse('axf:marketparams', args=("104749", "0","0")))


def user_market_params(request, typeid, cid, sort_rule):

    if request.method == 'GET':

        foodtypes = FoodType.objects.all()

        foodtypes_current = FoodType.objects.filter(typeid=typeid).first()

        if foodtypes_current:
            childtypes = foodtypes_current.childtypenames

            childtypenames = childtypes.split('#')

            child_type_list = []
            for childtypename in childtypenames:
                child_type_info = childtypename.split(':')
                child_type_list.append(child_type_info)

        if cid == '0':
            goods_list = Goods.objects.filter(categoryid=typeid)
        else:
            goods_list = Goods.objects.filter(categoryid=typeid,
                                              childcid=cid)

        if sort_rule == '0':
            pass
        elif sort_rule == '1':
            goods_list = goods_list.order_by('productnum')
        elif sort_rule == '2':
            goods_list = goods_list.order_by('-price')
        elif sort_rule == '3':
            goods_list = goods_list.order_by('price')

        data = {
            'foodtypes': foodtypes,
            'typeid': typeid,
            'child_type_list': child_type_list,
            'goods_list': goods_list,
            'cid': cid
        }
        return render(request, 'market/market.html', data)


def sub_cart(request):

    if request.method == 'POST':
        user = request.user
        goods_id = request.POST.get('goods_id')

        carts = CartModel.objects.filter(goods_id=goods_id, user=user).first()
        data = {
            'msg': 'ok',
            'status': '200'
        }
        if carts:
            if carts.c_num == 1:
                carts.delete()
                data['c_num'] = 0
            else:
                carts.c_num -= 1
                carts.save()
                data['c_num'] = carts.c_num

        return JsonResponse(data)


def add_cart(request):

    if request.method == 'POST':

        user = request.user
        goods_id = request.POST.get('goods_id')

        data = {
            'msg': 'ok',
            'status': '200'
        }

        if user and user.id:

            carts = CartModel.objects.filter(goods_id=goods_id, user=user).first()
            if carts:
                carts.c_num += 1
                carts.save()
                data['c_num'] = carts.c_num
            else:
                CartModel.objects.create(user=user,
                                         goods_id=goods_id,
                                         c_num=1)
                data['c_num'] = 1
        return JsonResponse(data)


def change_cart_select(request):

    if request.method == 'POST':
        data = {
            'msg': 'ok',
            'status': '200'
        }

        cart_id = request.POST.get('cart_id')
        s_status = request.POST.get('s_status')

        CartModel.objects.filter(id=cart_id).update(is_select=s_status)

        cart = CartModel.objects.filter(id=cart_id).first()
        data['cart_id'] = cart.id
        data['is_select'] = cart.is_select
        return JsonResponse(data)


def generate_order(request):

    if request.method == 'GET':

        user = request.user
        if user and user.id:

            carts = CartModel.objects.filter(user=user, is_select=True)
            # 创建订单
            order = OrderModel.objects.create(user=user, o_status=0)
            # 创建订单的详细信息
            for cart in carts:
                OrderGoodsModel.objects.create(order=order, goods=cart.goods, goods_num=cart.c_num)

                carts.delete()
        return HttpResponseRedirect(reverse('axf:mine'))





