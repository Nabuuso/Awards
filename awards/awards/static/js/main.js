$(document).ready(function(){
    //REGISTER USER
    $("#registerBtn").click(function(e){
        e.preventDefault();
        let body = {
            full_name: $("#fullName").val(),
            email: $("#email").val(),
            password: $("#password").val(),
            username: $("#username").val(),
        }
        $.ajax({
            method:'POST',
            url:'register',
            data:body,
            success:function(response){
                console.log(response)
                console.log(JSON.stringify(response))
                if(response.status == 201){
                    $("#fullName").val("")
                    $("#email").val("")
                    $("#password").val("")
                    $("#username").val("")
                    alert(response.message)
                }else{
                    // alert(response.message)
                    alert(response.error)
                    // $("#register-alert").html(response.error)
                }
            },
            error:function(response){
                // $("#register-alert").html(JSON.stringify(response).error)
                alert(response.error)
            }
        })
    })
})