
//!b    Function names should follow camelCase convention

// function demo() {
//     s = "Hiii i am rohit"
//     return s
// }
// s = demo()
// console.log(s);


// function demo() {
//     for (let i = 1; i <= 100; i++) {
//         let count = 0;
//         for (let j = 1; j <= i; j++) {
//             if (i % j == 0) {
//                 count++;
//             }
//         }
//         if (count == 2) {
//             console.log(i);
//         }
//     }
// }
// demo();


// let annonomus = function () {
//     console.log("Hii i am rohit")
//     // return "Hii"
// }
// console.log(annonomus());

(
    function () {
        for (let i = 1; i <= 100; i++) {
            let count = 0
            for (let j = 1; j <= i; j++) {
                if (i % j == 0) {
                    count++
                }
            }
            if (count == 2) {
                console.log("Prime : ", i);
            }
        }
    }
)()