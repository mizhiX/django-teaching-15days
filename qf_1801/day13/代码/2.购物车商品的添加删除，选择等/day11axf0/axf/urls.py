from django.conf.urls import url

from axf import views
urlpatterns = [
    # 首页
    url(r'^home/', views.home, name='home'),
    # 个人中心
    url(r'^mine/', views.mine, name='mine'),
    url(r'^userregister/', views.user_register, name='user_register'),
    url(r'^userlogout/', views.user_logout, name='user_logout'),
    url(r'^userlogin/', views.user_login, name="user_login"),

    # 闪购
    url(r'^market/$', views.user_market, name='market'),
    url(r'^market/(\d+)/(\d+)/(\d+)/', views.user_market_params, name='marketparams'),

    # 添加购物车
    url(r'^addgoods/', views.add_goods, name='addgoods'),
    url(r'^subgoods/', views.sub_goods, name='subgoods'),

    # 购物车
    url(r'^cart/', views.user_cart, name='cart'),
    # 修改购物车商品的选择
    url(r'^changeCartSelect/', views.user_change_select, name='change_select')
]