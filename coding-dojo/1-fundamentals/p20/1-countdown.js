// Countdown
// Create a function that accepts a number as an input. Return a new array that counts down by one, from the number (as array's 'zeroth' element) down to 0 (as the last element). How long is this array?

function countdown(num){
    var arr = [];
    while (num >= 0){
        arr.push(num);
        num--;
    }
    return arr;
}

console.log(countdown(5), ", length:", countdown(5).length);
