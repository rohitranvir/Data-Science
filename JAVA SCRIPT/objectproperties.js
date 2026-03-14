// ! Object.asign()

let obj1 = {
    name: "Rohit",
    age: 22
}
let details = Object.assign(obj1)
// console.log(details);
details.name = "santosh"
details.age = 50
// console.log(details);

// console.log(Object.values(obj1));
// console.log(Object.entries(obj1));


// console.log(Object.hasOwn(obj1, "name"));
// console.log();



// let obj2 = {
//     name: "Rohit",
//     age: 22,
//     place: "Delhi"
// }
// Object.seal(obj2)
// // Object.freeze(obj2)
// console.log(obj2);
// delete obj2.place
// console.log(obj2);
// obj2.name = "Santosh"
// console.log(obj2);
// obj2.place = "Delhi"
// console.log(obj2);
// console.log(Object.freeze(obj2));



// let a = [10, 5, 2, 98, 2, .5, 56.9]
// console.log(Math.min(...a));
// console.log(Math.max(...a));
// console.log(Math.ceil(56.9));
// console.log(Math.floor(56.9));
// console.log(Math.trunc(56.9));
// console.log(Math.round(...a));  //! it accept only one value
// console.log(Math.floor(Math.random() * 10000));



// ! Date object

let date = new Date()
console.log(date.getDate());
console.log(date.getMonth());
console.log(date.getFullYear());




