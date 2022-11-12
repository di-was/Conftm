
let submitbutton = document.querySelector("#signup");

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


submitbutton.addEventListener("click", (e) => {
    e.preventDefault();
    let appname = document.querySelector("#name").value;
    let accesstoken = document.querySelector("#email").value;
    let pageId = document.querySelector("#pass").value;

    data = {"name": appname, "AccessToken": accesstoken, "pageId": pageId}

    let token = getCookie('csrftoken')

    var url = "https://127.0.0.1:8000/app/creation/";

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);

    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.setRequestHeader("X-CSRFToken", token)

    xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
    if (xhr.status == 200) {
        window.location = 'https://127.0.0.1:8000/';
    }
}};
    xhr.send(JSON.stringify(data));
})