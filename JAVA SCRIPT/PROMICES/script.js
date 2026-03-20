// ! Promises


// let promics = new Promise((resolve, reject) => {
//     let study = false
//     if (study) {
//         resolve("You are doing study")
//     }
//     else {
//         reject("You are not doing study")
//     }
// })
// console.log(promics);



// ! Promises Handalig methods

// let promics = new Promise((resolve, reject) => {
//     let study = false
//     if (study) {
//         resolve("You are doing study")
//     }
//     else {
//         reject("You are not doing study")
//     }
// })
// promics.then((res) => {
//     console.log(res);
// })
// promics.catch((res) => {
//     console.log(res);
// })

// ! Getting response from web using API

fetchproduct = () => {
    let data = fetch('https://fakestoreapi.com/products')
    // console.log(data);
    return data
}
fetchproduct()
    .then((value) => value.json())
    .then((value) => console.log(value))
// .then((value) => console.log(value))



