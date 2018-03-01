// Print and Count
// Print all integer multiples of 5, from 512 to 4096.
// Afterward, also log how many there were.

function mult5(min, max){
    var count = 0;
    for (var x = min; x <= max; x++){
        if (x % 5 == 0){
            count++;
            console.log(x);
            x += 4;
        }
    }
    console.log(`There were ${count} integer multiples of 5 between ${min} and ${max}`);
}

mult5(512, 596);
