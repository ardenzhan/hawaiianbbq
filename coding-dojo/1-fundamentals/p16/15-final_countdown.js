// The Final Countdown
// Based on flexible countdown
// given 4 params, param1, param2, param3, param4
// print multiples of param1
// starting at param2, extending to param2
// if multiple is equal to param4, then skip
// use WHILE
// (3, 5, 17, 9) prints 6, 12, 15

function finalCountdown(mult, start, end, skip){
    var x = start;
    while (x <= end){
        if (x % mult == 0 && x != skip){
            console.log(x);
            x += mult;
        }
        else {
            x++;
        }
    }
}

finalCountdown(3, 5, 17, 9);