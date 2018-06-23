function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    $('#form-avatar').submit(function(){
        $(this).ajaxSubmit({
            url:'/user/profile/',
            type:'PATCH',
            dataType:'json',
            success:function(msg){
                $('#user-avatar').attr('src', '/static/' + msg.image_url)
            },
            error: function(msg){
                alert('请求失败')
            }
        })
        return false;
    });

    $('#form-name').submit(function(){

        var name = $('#user-name').val()
        $.ajax({
            url:'/user/proname/',
            type:'PATCH',
            dataType:'json',
            data:{'name': name},
            success:function(msg){
                if(msg.code == '1008'){
                    $('.error-msg').html('<i class="fa fa-exclamation-circle"></i>' + msg.msg)
                    $('.error-msg').show()
                }
            },
            error: function(msg){
                alert('请求错误')
            }
        })
        return false;
    });

});


function delete_msg(){
    $('.error-msg').hide()
}
