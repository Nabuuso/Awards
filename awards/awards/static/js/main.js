$(document).ready(function(){
    //REGISTER USER
    $("#registerBtn").click(function(e){
        e.preventDefault();
        let body = {
            full_name: $("#fullName").val(),
            email: $("#email").val(),
            password: $("#password").val(),
            username: $("#username").val(),
            bio:$("#bio").val()
        }
        console.log(body)
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
    //UPLOAD IMAGE
    $("#upload-img-btn").click(function(e){
        var data = new FormData()
        data.append("image",$("#imageFile")[0].files[0])
        data.append("image_name",$("#imageName").val())
        data.append("image_caption",$("#imageCaption").val())
        data.append("profile",$("#user").val())
        data.append("csrfmiddlewaretoken","{{ csrf_token }}")
        $.ajax({
            method:'POST',
            url:'blog-images',
            data:data,
            processData:false,
            contentType:false,
            mimeType:"multipart/form-data",
            success: function(response){
                location.reload()
            },
            error: function(response){
                alert(response.error)
            }
        })
    })
})