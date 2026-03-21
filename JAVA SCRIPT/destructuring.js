//note  : Array destructiong 

//BUG  Extracting  values from arrays, And Objects

// let arr = [10, 20, 30, 40]
// let [a, b, c, d, f] = arr
// console.log(b); //BUG 20

// ! Second method
// let arr = [10, 20, 30, 40, 50]
// let [, , , , f] = arr
// console.log(f); //BUG 20



// Note: Object Destructiong 

// let details = {
//     name: 'rohit',
//     age: 25
// }
// let { name, age } = details
// console.log(name);


// Note: Fetching data from web 
// let products = async () => {
//     let res = await fetch('https://fakestoreapi.com/products')
//     let data = await res.json()
//     // console.log(data);
//     data.forEach((element) => {
//         let { title, price } = element
//         console.log(title, price);

//     });
// }
// products()
// products().then((value) => {
//     console.log(value[0].title)
// })


// Note: How to deconstruct onject inside object

let details = {
    name: "Rohit",
    father: "Santosh",
    address: {
        village: "kali",
        post: {
            pin: "445204"
        }
    }
}
let { address: { post: { pin } } } = details
console.log(pin);

// let { village, post } = address
// let { pin } = post
// console.log(pin);


