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
        data.append("name",$("#siteName").val())
        data.append("description",$("#description").val())
        data.append("profile",$("#user").val())
        data.append("csrfmiddlewaretoken","{{ csrf_token }}")
        data.append("link",$("#link").val())
        $.ajax({
            method:'POST',
            url:'projects',
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
    //SLIDERS
    $("#design").slider();
    $("#design").on("slide", function(slideEvt) {
        $("#designSliderVal").text(slideEvt.value);
    });
    //USABILITY
    $("#usability").slider();
    $("#usability").on("slide", function(slideEvt) {
        $("#usabilitySliderVal").text(slideEvt.value);
    });
    //CONTENT
    $("#content").slider();
    $("#content").on("slide", function(slideEvt) {
        $("#contentSliderVal").text(slideEvt.value);
    });
    //DISPLAY MODAL
    $(".vote-btn").click(function(e){
        e.preventDefault()
        let profile = $(this).data("user")
        let project = $(this).data("project")
        $("#project-id").val(project)
        $("#profile-id").val(profile)
        $("#voteModal").modal('show')
    })
    //RATE WEBSITE
    $("#rate-site-btn").click(function(e){
        e.preventDefault();
        let body = {
            profile:$("#profile-id").val(),
            project:$("#project-id").val(),
            content:$("#content").val(),
            design:$("#design").val(),
            usability:$("#usability").val()
        }
        $.ajax({
            method:'POST',
            url:'rating',
            data:body,
            success:function(response){
                alert('Site rated successfully')
                location.reload()
            }
        })
    })
    $(".not-logged-in").click(function(e){
        alert("Login to continue")
    })
})