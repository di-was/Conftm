let button = document.querySelectorAll("#detail");


button.forEach(element => {
    element.addEventListener("click", (e) => {
        parent = element.parentNode.parentNode
        pageId = parent.children[0].children[0].innerText;
        console.log(pageId)
        window.location = "https://conftm.herokuapp.com/confession/view/" + pageId + "/"
    })

})



