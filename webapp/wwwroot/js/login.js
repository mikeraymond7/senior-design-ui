function authorize() {
    var uname = document.getElementById("uname");
    var pwd = document.getElementById("pwd");
    if (uname.value == "me" && pwd.value == "you") {
        console.log("Passed");
        window.location.replace("http://localhost/downloads");
    }
    else {
        console.log("Failed");
    }
}