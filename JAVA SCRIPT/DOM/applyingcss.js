
// h1.style.setProperty("color", "blue")
// h1.style.setProperty("background-color", "red")


let h1 = document.createElement("h1")
h1.innerText = "This is applying csss"
let body = document.querySelector("body")
body.appendChild(h1)


// h1.style.backgroundColor = "pink"
// h1.style.color = "red"


// h1.style.cssText = "background-color:red; color:pink   ; font-size:100px"


let val = true
if (val === true) {
    h1.style.color = "red"
    h1.innerHTML = "Data fetched successfully"
}
else {
    h1.style.color = "blue"
    h1.innerText = "data not fetched"
}

// ! Getting the property value
console.log(h1.style.getPropertyValue("color"));

// ! Removing the property

h1.style.removeProperty("color")
