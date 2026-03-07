let a = 10;
var b = 20;
const c = 30;
console.log('I am global')
function demo() {
    let d = 40;
    let e = 50;
    let f = 60;
    console.log("i am local scope")
    console.log(a)
    console.log(b)
    console.log(c)
    console.log(d)
    console.log(e)
    console.log(f)
}
demo()
{
    console.log("i am black scope")
    console.log(a)
    console.log(b)
    console.log(c)
}