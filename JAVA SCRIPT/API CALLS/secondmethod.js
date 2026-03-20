let btn = document.getElementById("btn")
let body = document.querySelector("body")
let product = async () => {
    let data = await fetch('https://fakestoreapi.com/products')
    return await data.json()
}
function randomval(l, h) {
    return Math.floor(Math.random() * (h - l + 1)) + l
}
let getdata = async () => {
    let data = await product()
    return data[randomval(0, 19)].image
}
// getdata()
let img = document.createElement("img")
let p = document.createElement("p")
btn.addEventListener("click", async () => {
    let imgurl = await getdata()
    p.innerHTML = `<img src="${imgurl}" alt="Image Not found"></img > `
    body.appendChild(p)
})