const URL = "https://dog.ceo/api/breeds/image/random"
let p = document.querySelector("#p")
let btn = document.querySelector("#btn")
const container = document.querySelector("#container");
// const getfacts = async () => {
//     console.log("Getting Data");
//     let response = await fetch(URL)
//     let data = await response.json()
//     p.innerHTML = `<img src="${data.message}">`

//     // p.textContent = data.country[0].country_id
// }
// btn.addEventListener("click", getfacts)



// function fetchdata() {
//     fetch(URL).then((response) => {
//         return response.json()
//     }).then((response) => {
//         p.innerHTML = `<img src="${response.message}">`

//     })
// }
// btn.addEventListener("click", fetchdata)

console.log("Start");
let fetchProducts = () => {
    let data = fetch("https://fakestoreapi.com/products");
    console.log(data);
    return data;
};
function ind(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
btn.addEventListener("click", () => {
    fetchProducts()
        .then((value) => {
            // console.log(value.json())
            return value.json()
        }).then((res) => {
            // p.innerHTML = `<img src="${res[ind(1, 19)].image}"></img>`
            res.map((r) => {
                // p.innerText = r.image
                let container = document.createElement("article")
                let btn = document.createElement("button")
                let p = document.createElement("p")
                let img = document.createElement("img")
                // p.innerHTML = `<img src="${r.image}">`
                p.textContent = r.title
                img.src = r.image
                btn.innerText = "add to cart"
                container.append(img, p, btn)
                document.body.append(container)

            })
        })
})
