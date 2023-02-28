// login username and password

function validate_login()
{
    let status = 1;
    username = document.getElementById("username");
    password = document.getElementById("userpassword");
    if (username.value == "") {
        username.style.borderColor = "#FF0000";
        status = 0;
    } else {
        username.style.borderColor = "#ced4da"
        status = 1;
    }
    if (password.value == "") {
        password.style.borderColor = "#FF0000";
        status = 0;
    } else {
        password.style.borderColor = "#ced4da";
        status = 1;
    }
    if (status == 0) {
        return false;
    }

}


//Remove resubmit form while refresh
if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}