let submitLogin = document.querySelector("#signin")

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


submitLogin.addEventListener("click", (e) => {
    e.preventDefault();
    usernameInput = document.querySelector("#your_name").value
    passwordInput = document.querySelector("#your_pass").value
    data = {"username": usernameInput,
    "password": passwordInput}

    let token = getCookie('csrftoken')

    var url = "http://127.0.0.1:8000/InOut/0";

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);

    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.setRequestHeader("X-CSRFToken", token)

    xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
    if (xhr.status == 400) {
        error = document.querySelector(".error")
        error.style.display = "initial";
        error.innerHTML = xhr.responseText;
    }
    if (xhr.status == 200) {
         error = document.querySelector(".error")
        error.style.display = "none";
        window.location = xhr.responseText;
    }
}};
    xhr.send(JSON.stringify(data));
})