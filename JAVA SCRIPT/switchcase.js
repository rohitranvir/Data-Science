let a = 200000
switch (true) {
    case (a > 5000 && a <= 10000): {
        console.log("Silver")
        break;
    }
    case (a > 10000 && a < 20000): {
        console.log("golden")
        break

    }
    case (a > 20000 && a <= 100000): {
        console.log("Diamond");
        break

    }
    default: {
        console.log("THis is invalid")
        break;
    }
}