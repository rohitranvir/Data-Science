// for (let i = 1; i <= 5; i++) {
//     console.log(i);
// }
// let a = 1;
// while (a <= 10) {
//     console.log(a);
//     a++
// }


// let a = 8
// let count = 0
// for (let i = 1; i <= a; i++) {
//     if (a % i == 0) {
//         count++
//     }
// }
// if (count == 2) {
//     console.log("This is prime number");

// }
// else {
//     console.log("This is not prime number");

// }


for (let i = 2; i <= 100; i++) {
    let count = 0
    for (let j = 1; j <= i; j++) {
        if (i % j == 0) {
            count++
        }
    }
    if (count == 2) {
        console.log("This is prime number : ", i);
    }
    // else {
    //     // console.log("This is not Prime number : ", i);
    // }
}