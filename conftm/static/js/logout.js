let logout = document.querySelector(".nav-link")

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

logout.addEventListener("click", (e) => {
    e.preventDefault()
    let token = getCookie('csrftoken')

    var url = "https://127.0.0.1:8000/InOut/1";

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);

    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.setRequestHeader("X-CSRFToken", token)

    xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
        window.location = "https://127.0.0.1:8000/"
       }};
    xhr.send(JSON.stringify({"username": "ignore", "password": "ignore"}));
})
