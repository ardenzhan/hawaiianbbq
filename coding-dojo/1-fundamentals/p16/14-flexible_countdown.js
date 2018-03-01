// Flexible Countdown
// Given lowNum, highNum, mult
// print multiples of mult from highNum down to lowNum
// use a FOR
// (2, 9, 3) prints 9 6 3 (successive lines)

function countdown(lowNum, highNum, mult){
    for (var x = highNum; x >= lowNum; x -= mult){
        console.log(x);
    }
}

countdown(2, 9, 3);