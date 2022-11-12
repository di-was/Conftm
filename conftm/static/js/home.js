let button = document.querySelectorAll("#detail");


button.forEach(element => {
    element.addEventListener("click", (e) => {
        parent = element.parentNode.parentNode
        pageId = parent.children[0].children[0].innerText;
        console.log(pageId)
        window.location = "https://127.0.0.1:8000/confession/view/" + pageId + "/"
    })

})



