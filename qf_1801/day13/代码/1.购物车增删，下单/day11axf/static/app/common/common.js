
function addShop(goodsid){
    csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        type:'POST',
        url: '/axf/addcart/',
        data: {'goods_id': goodsid},
        dataType: 'json',
        headers:{'X-CSRFToken': csrf},
        success: function(msg){
            $('#num_'+goodsid).html(msg.c_num)
        },
        error: function(msg){
            alert(msg)
        }
    });
};

function subShop(goodsid){
    csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        type:'POST',
        url: '/axf/subcart/',
        data: {'goods_id': goodsid},
        dataType: 'json',
        headers:{'X-CSRFToken': csrf},
        success: function(msg){
            $('#num_'+goodsid).html(msg.c_num)
        },
        error: function(msg){
            alert(msg)
        }
    });
};


function changeCartSelect(cart_id, s_status){
    alert('1')
    csrf = $('input[name="csrfmiddlewaretoken"]').val()
    alert(cart_id)
    alert(s_status)
    $.ajax({
        type:'POST',
        url: '/axf/changecartselect/',
        data:{'cart_id':cart_id, 's_status':s_status},
        dataType:'json',
        headers:{'X-CSRFToken':csrf},
        success: function(msg){
            console.log(msg)
            if(msg.is_select){
                s = '<span onclick="changeCartSelect(' +  msg.cart_id + ',' + '0)">√</span>'
            }else{
                s = '<span onclick="changeCartSelect(' + msg.cart_id + ',' + '1)">x</span>'
            }
            console.log(msg.cart_id)
            $('#changecartselect_'+ msg.cart_id).html(s)

        },
        error:function(msg){
            alert(msg)
        }
    });
}
