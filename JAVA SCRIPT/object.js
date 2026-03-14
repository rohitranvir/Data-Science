//  ! Literal way
// let a = {
//     name: "Rohit",
//     age: 22
// }
// console.log(a.name);


// * Constructor way

// let data = new Object()
// data.name = "Rohit"
// data.age = 22
// console.log(data.name);


// ? Functional way

// function userdetails(name, age) {
//     this.name = name,
//         this.age = age
//     // return this.name
// }
// data = new userdetails("Rohit", 22)
// console.log(data);



class Studentdetails {
    constructor(name, age) {
        this.name = name
        this.age = age
    }
}
let details = new Studentdetails("Rohit", 24)
console.log(details)

