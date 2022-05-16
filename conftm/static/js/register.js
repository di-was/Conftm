let name = document.querySelector("#name");
let password = document.querySelector("#pass")
let signup = document.querySelector("#signup")



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


signup.addEventListener("click", (e) => {
    e.preventDefault()

    data = {'username': name.value, 'password': password.value}
    let token = getCookie('csrftoken')

    var url = "https://conftm.herokuapp.com/register/";

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);

    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.setRequestHeader("X-CSRFToken", token)

    xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
    if (xhr.status == 200) {
        window.location = "https://conftm.herokuapp.com/InOut/0";
    }
    console.log(xhr.responseText)
    console.log(xhr.status);
    console.log(xhr.responseText);
}};

    xhr.send(JSON.stringify(data));

})