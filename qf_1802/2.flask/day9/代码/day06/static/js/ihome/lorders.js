//模态框居中的控制
function centerModals(){
    $('.modal').each(function(i){   //遍历每一个模态框
        var $clone = $(this).clone().css('display', 'block').appendTo('body');    
        var top = Math.round(($clone.height() - $clone.find('.modal-content').height()) / 2);
        top = top > 0 ? top : 0;
        $clone.remove();
        $(this).find('.modal-content').css("margin-top", top-30);  //修正原先已经有的30个像素
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    $('.modal').on('show.bs.modal', centerModals);      //当模态框出现的时候
    $(window).on('resize', centerModals);

    $('.modal-accept').click(function(){
        var order_id = $(this).attr('order-id')
        var status = 'WAIT_PAYMENT'

        $.ajax({
            url:'/order/orders/',
            type:'PATCH',
            data:{'order_id': order_id, 'status': status},
            dataType:'json',
            success:function(msg){
                location.href = '/order/lorders/'
            },
            error: function(msg){
                alert('请求失败')
            }
        });
    });

    $('.modal-reject').click(function(){
        var order_id = $(this).attr('order-id')
        var status = 'REJECTED'
        var comment = $('#reject-reason').val()

        $.ajax({
            url:'/order/orders/',
            type:'PATCH',
            data:{'order_id': order_id, 'status': status, 'comment':comment},
            dataType:'json',
            success:function(msg){
                location.href = '/order/lorders/'
            },
            error: function(msg){
                alert('请求失败')
            }
        });

    });
});

$.get('/order/user_lorders/', function(msg){
    if(msg.code == '200'){
        var lorder_html = template('lorder_list_temp', {olist: msg.orders_info})
        $('.orders-list').html(lorder_html)

        $(".order-accept").on("click", function(){
            var orderId = $(this).parents("li").attr("order-id");
            $(".modal-accept").attr("order-id", orderId);
        });
        $(".order-reject").on("click", function(){
            var orderId = $(this).parents("li").attr("order-id");
            $(".modal-reject").attr("order-id", orderId);
        });
    }
});



