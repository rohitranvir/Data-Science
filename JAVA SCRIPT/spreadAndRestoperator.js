// !Spread Operators
// ! => It spread values 
// let arr1 = [1, 2, 3, 4, 5, 6, 7]
// let arr2 = [1, 2, 3, 4, 5, 6, 7]
// let arr = [...arr1, ...arr2]
// console.log(arr);


// let obj1 = {
//     'name': 'rohit'
// }
// let obj2 = {
//     'Father': 'Santosh'
// }
// let obj3 = {
//     ...obj1,
//     ...obj2,
//     ...arr1
// }
// console.log(obj3);



// ! It stores the extra values in the Form of array
function rohit(a, b, ...c) {
    console.log(a, b, c);

}
rohit(10, 20)
rohit(10, 20, 30, 40)