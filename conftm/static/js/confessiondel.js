let trash = document.querySelectorAll(".fa-trash");
let deleteb = document.querySelector(".delete-b");
let post = document.querySelectorAll(".fa-check");

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


trash.forEach(element => {

element.addEventListener("click", (e) => {
    id = element.children[0].innerText;
    var url = "https://conftm.herokuapp.com/confession/delete/" + id + '/';
    let token = getCookie('csrftoken')
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);

    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.setRequestHeader("X-CSRFToken", token)

    xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
    if (xhr.status == 200) {
         let target = element.parentNode.parentNode.parentNode.parentNode.parentNode
         target.remove()
    }
}};
    xhr.send(JSON.stringify("ok"));
})


})

deleteb.addEventListener("click", (e) => {

    var url = window.location + 'deleteAp/'
    let token = getCookie('csrftoken')
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);

    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.setRequestHeader("X-CSRFToken", token)

    xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
    if (xhr.status == 200) {
         window.location = "https://conftm.herokuapp.com/";
    }
}};
    xhr.send(JSON.stringify("ok"));
})

post.forEach(element => () {

    element.addEventListener("click", (e) => {
    let url = window.location  + 'pso/'
    let token = getCookie('csrftoken')
    htmlelement = document.querySelector(".fa-check")
    data = {"id": htmlelement.parentNode.parentNode.parentNode.parentNode.parentNode.children[1].children[0].children[0].children[0].children[0].innerText}
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);
    console.log(data)
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.setRequestHeader("X-CSRFToken", token)

    xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
    if (xhr.status == 200) {
         let target = htmlelement.parentNode.parentNode.parentNode.parentNode.parentNode
         target.remove()
    }
}};
    xhr.send(JSON.stringify(data));

})
})