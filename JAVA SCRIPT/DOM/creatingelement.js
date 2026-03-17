



// let par = document.createElement("p")
// par.innerText = "This Paragraph is created by js"
// document.getElementById("hi").appendChild(par)

// let btn = document.createElement("button")
// btn.innerText = "click me"
// document.querySelector("h1").appendChild(btn)


// let el = document.getElementById("hi")
// el.innerHTML = "<h1>THis is Inner html</h1>"


let el = document.createElement("p")
let h1 = document.createElement("h1")
el.textContent = "This is text content";
h1.innerHTML = ""
document.getElementsByClassName("hi")[0].appendChild(el)