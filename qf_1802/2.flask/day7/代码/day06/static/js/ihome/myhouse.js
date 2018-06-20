$(document).ready(function(){
    $(".auth-warn").show();
})

$.get('/user/auths/', function(msg){
    if(msg.code == '200'){
        if(msg.data.id_name){
            $('.auth-warn').hide()
            $('#houses-list').show()
        }else{
            $('.auth-warn').show()
            $('#houses-list').hide()
        }
    }
});
