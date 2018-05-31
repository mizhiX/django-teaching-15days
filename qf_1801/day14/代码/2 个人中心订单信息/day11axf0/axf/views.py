
from datetime import datetime, timedelta

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from axf.models import MainMustBuy, MainNav, MainShop, \
    MainShow, MainWheel, UserModel, UserTicketModel, \
    OrderModel, FoodType, Goods, CartModel, OrderGoodsModel

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


def user_market(request):

    return HttpResponseRedirect(reverse('axf:marketparams', args=('104749', '0', '0')))


def user_market_params(request, typeid, cid, sort_id):
    if request.method == 'GET':
        data = {}
        # 获取类型
        foodtypes = FoodType.objects.all()

        # 获取商品
        if cid == '0':
            goods_types = Goods.objects.filter(categoryid=typeid)
        else:
            goods_types = Goods.objects.filter(categoryid=typeid,
                                               childcid=cid)
        # 商品的分类：
        if sort_id == '0':
            pass
        elif sort_id == '1':
            goods_types = goods_types.order_by('productnum')
        elif sort_id == '2':
            goods_types = goods_types.order_by('-price')
        elif sort_id == '3':
            goods_types = goods_types.order_by('price')

        # 获取分类的全部类型
        foodtypes_childnames = FoodType.objects.filter(typeid=typeid).first()

        childtypenames = foodtypes_childnames.childtypenames

        childtypenames_list = childtypenames.split('#')

        child_types_list = []
        for childtypename in childtypenames_list:

            child_types_list.append(childtypename.split(':'))

        data['foodtypes'] = foodtypes
        data['typeid'] = typeid
        data['cid'] = cid
        data['goods_types'] = goods_types
        data['child_types_list'] = child_types_list
        return render(request, 'market/market.html', data)


def add_goods(request):

    if request.method == 'POST':

        data = {
            'msg': '请求成功',
            'code': '200'
        }

        user = request.user
        if user and user.id:
            goods_id = request.POST.get('goods_id')
            # 获取购物车信息
            user_carts = CartModel.objects.filter(user=user, goods_id=goods_id).first()
            # 如果用户选了商品
            if user_carts:
                user_carts.c_num += 1
                user_carts.save()
                data['c_num'] = user_carts.c_num
            else:
                # 如果用户没选商品，就创建
                CartModel.objects.create(user=user,
                                         goods_id=goods_id,
                                         c_num=1)
                data['c_num'] = 1
        return JsonResponse(data)


def sub_goods(request):

    if request.method == 'POST':
        data = {
            'code':'200',
            'msg': '请求成功'
        }
        user = request.user
        goods_id = request.POST.get('goods_id')

        if user and user.id:
            # 查看当前商品是否已经在购物中
            user_carts = CartModel.objects.filter(user=user,
                                                  goods_id=goods_id).first()
            # 如果存在，则减一
            if user_carts:
                # 如果商品的数量为1，则删除
                if user_carts.c_num == 1:
                    user_carts.delete()
                    data['c_num'] = 0
                else:
                    # 如果商品数量不为一，则减一
                    user_carts.c_num -= 1
                    user_carts.save()
                    data['c_num'] = user_carts.c_num
        return JsonResponse(data)


def user_cart(request):

    if request.method == 'GET':

        user = request.user

        if user and user.id:
            # 如果用户已经登录，则加载购物车的数据
            carts = CartModel.objects.filter(user=user)

            return render(request, 'cart/cart.html', {'carts':carts})
        else:
            return HttpResponseRedirect(reverse('axf:login'))


def user_change_select(request):

    if request.method == 'POST':

        cart_id = request.POST.get('cart_id')
        user = request.user
        data = {
            'code': '200',
            'msg': '请求成功'
        }

        if user and user.id:

            cart = CartModel.objects.filter(pk=cart_id).first()
            if cart.is_select:
                cart.is_select = False
            else:
                cart.is_select = True
            cart.save()
            data['is_select'] = cart.is_select
        return JsonResponse(data)


def user_generate_order(request):

    if request.method == 'GET':

        user = request.user
        if user and user.id:
            # 先查询is_select为True的购物车的数据
            carts_goods = CartModel.objects.filter(is_select=True)

            # 创建订单, 0为付款  1已付款
            order = OrderModel.objects.create(user=user, o_status=0)

            # 创建订单详情信息
            for carts in carts_goods:

                OrderGoodsModel.objects.create(goods=carts.goods,
                                               order=order,
                                               goods_num=carts.c_num)
                carts.delete()
            # carts_goods.delete()

            return HttpResponseRedirect(reverse('axf:user_pay_order', args=(str(order.id),)))


def user_pay_order(request, order_id):

    if request.method == 'GET':

        orders = OrderModel.objects.filter(pk=order_id).first()
        data = {
            'order_id': order_id,
            'orders': orders
        }
        return render(request, 'order/order_info.html', data)

def order_pay(request, order_id):
    # 修改订单的付款状态 o_status=1
    if request.method == 'GET':

        OrderModel.objects.filter(pk=order_id).update(o_status=1)

        return HttpResponseRedirect(reverse('axf:mine'))


def order_wait_pay(request):

    if request.method == 'GET':

        user =request.user

        if user and user.id:

            orders = OrderModel.objects.filter(user=user, o_status=0)

            return render(request, 'order/order_list_wait_pay.html', {'orders': orders})


def order_wait_shouhuo(request):

    if request.method == 'GET':

        user = request.user

        if user and user.id:

            orders = OrderModel.objects.filter(user=user, o_status=1)

            return render(request, 'order/order_list_payed.html', {'orders':orders})
