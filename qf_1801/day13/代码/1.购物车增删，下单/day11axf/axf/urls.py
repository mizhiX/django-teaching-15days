from django.conf.urls import url

from axf import views
urlpatterns = [

    url(r'^home/', views.home, name='home'),
    # 注册
    url(r'^userregister/', views.user_register, name='register'),
    url(r'^userlogin/', views.user_login, name='login'),
    url(r'^userlogout/', views.user_logout, name='logout'),
    # 个人中心
    url(r'^mine/', views.user_mine, name='mine'),

    # 购物车
    url(r'^cart/', views.user_cart, name='cart'),

    # 闪购
    url(r'^market/$', views.user_market, name='market'),
    url(r'^market/(\d+)/(\d+)/(\d+)/', views.user_market_params, name='marketparams'),

    # 添加删除商品
    url(r'^subcart/', views.sub_cart, name='sub_cart'),
    url(r'^addcart/', views.add_cart, name='add_cart'),

    # 改变购物车中商品的状态
    url(r'^changecartselect/', views.change_cart_select, name='change_cart_select'),

    # 下单
    url(r'^generateorder/', views.generate_order, name="generate_order"),

]