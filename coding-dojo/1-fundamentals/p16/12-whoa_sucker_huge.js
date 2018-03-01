// Whoa, That Sucker's Huge...
// Add odd integers from -300,000 to 300,000
// console.log the final sum
// Is there a shortcut?

function addOdd(min, max){
    var sum = 0;
    if ((min + max) != 0) {
        for (var x = min; x <= max; x++){
            // javascript modulo of negative nubmer gives negative remainder
            if (x % 2 != 0){
                sum += x;
                x++;
            }
        }
    }
    console.log(sum);
}
addOdd(-303, 303);