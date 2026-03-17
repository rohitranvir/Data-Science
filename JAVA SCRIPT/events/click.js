// let h1 = document.querySelector("h1")
// console.log(h1);

// ! First method ONCLICK()
// let clickbt = () => {
//     h1.style.color = "red"
// }
// h1.onclick = clickbt()


// ! Second Method
// let clickbt = () => {
//     h1.style.color = "red"
// }
// h1.onclick = clickbt
// let changebgccolor = () => {
//     h1.style.backgroundColor = "green"
// }
// h1.ondblclick = changebgccolor


// ! Third method



// let body = document.querySelector("body")
// let arr = ["red", "yellow", "pink", "blue"]
// let btn = document.querySelector("button")
// btn.addEventListener("click", () => {
//     let index = Math.floor(Math.random() * arr.length)
//     body.style.backgroundColor = arr[index]
// })



// let btn = document.querySelector("button")
// btn.addEventListener("click", () => {
//     alert("You clicked button")
// })


let genraterandomval = () => {
    return Math.random() * 255
}
let button = document.querySelector("button")
let body = document.querySelector("body")
button.addEventListener("click", () => {
    body.style.backgroundColor = `rgb(${genraterandomval()},${genraterandomval()},${genraterandomval()})`
})
button.addEventListener("click", () => {
    button.style.backgroundColor = `rgb(${genraterandomval()},${genraterandomval()},${genraterandomval()})`
    button.style.color = `rgb(${genraterandomval()},${genraterandomval()},${genraterandomval()})`
})
