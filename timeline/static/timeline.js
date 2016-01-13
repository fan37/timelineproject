var baseUrl = 'http://127.0.0.1:8000/';
var username;
var password;

var doJoin = function(){
    var name = $("#name").val();
    var username = $("#username").val();
    var password= $("#password").val();
    $.ajax({
        type : 'post',
        url: baseUrl + 'api/user/create/',
        data: {
            username: username,
            name: name,
            password: password
        },
        success: function(){
            alert("OK");
            location.href = "login.html";
        },
        error: function(msg){
            alert("Error.");
        },
    });
}
