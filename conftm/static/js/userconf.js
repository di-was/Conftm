let button = document.querySelector('.button')

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


button.addEventListener("click", (e) => {
    let span = document.querySelector(".inpspan").innerText;
    let token = getCookie('csrftoken')
    var url = window.location;

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);

    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.setRequestHeader("X-CSRFToken", token)

    xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
        if(xhr.status == 200) {
            document.querySelector(".success").style.opacity = "initial";
        }
       }};
    xhr.send(JSON.stringify({'content': span}));

})