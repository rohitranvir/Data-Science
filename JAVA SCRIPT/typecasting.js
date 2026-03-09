// IMPORTANT: Converting one data type to another is called as typecasting

// NOTE: There are two types of type casting
// 1. Implicit casting


// 1. Implicit type casting - it is done internally, no need to do it externally

// TODO: Test implicit casting with different data types
// let a = "abc"
// let b = 20
// console.log(a + b)  // abc20 - This is done by internally

// console.log(10 > 8 > 2)    // False
// console.log(1 > 8 < 1)  // True
// NOTE: Truthy values - number, "any string", 1, [], {}
// BUG: Falsy values should include "", 0, undefined, null, false, 1, [], {}
// ! False value : - "",0, undefined, null

// let a = null;
// console.log(Boolean(a))

// IMPORTANT: Logical operators behavior - know the difference!
// console.log(4&&5)   // both true means return next value ==> 5
// console.log(0 && null)  // both false means return previous value ==> 0

// TODO: Understand the || operator behavior
// console.log(0 || 8) // if one true and one false means return true value



//  TODO : 2. Explicit type casting - done manually by programmer
//! 1. Number()
//! 2. parseInt()   : It will extract only integer
//! 3.parseFloat()   : It will extract Float values only
// let num = "123"
// console.log(typeof (num))
// let number = Number(num)
// console.log(number)

// let a = "1542rohit"
// let b = parseInt(a)
// console.log(b)

// let c = "15.250rohit"
// let d = parseFloat(c)
// console.log(d)

// ! tostring()   => it is used to convert to string
// let a = 123
// let strdata = a.toString()
// console.log(strdata) //123
// console.log(typeof (strdata)) //string