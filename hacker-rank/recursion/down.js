// Find the number of ways that a given integer x
// can be expressed as the sum of the nth powers of unique, natural numbers.

// Example 1
// (100, 2) => 3
// 1. 10^2 = 100
// 2. 8^2 + 6^2 = 100
// 3. 7^2 + 5^2 + 4^2 + 3^2 + 1^2 = 100

// Example 2
// (100, 3) => 1
// 1. 4^3 + 3^3 + 2^3 + 1^3 = 100

function powerSum(x, n){
    let solutions = 0;

    // Base will be n root of x
    let base = Math.floor(Math.pow(x, 1/n));


   	for (var i = base; i > 0; i--){
        console.log(i);

        powerSum(i-1, n);
    }
}


        // let remainder = x - Math.pow(i, n);
        // let remainSum = remaindingSum(i-1, n);

        // let nextBase = Math.floor(Math.pow(remainder, 1/n));

        // if (remainSum < remainder) {
        //     arr = [];
        //     break;
        // }

        // if (remainder == 0) {
        //     solutions++;
        //     console.log(arr);
        //     arr = [];
        // }
        // else {
        //     solutions += powerSum(remainder, n, i);
        // }

//     }
//     // return solutions;
// }

// function remaindingSum(number, power){
//     let total = 0;
//     for (let i = number; i > 0; i--){
//         total += Math.pow(i, power);
//     }
//     return total;
// }

console.log(powerSum(4, 1));
// => 3

// console.log(powerSum(8,1));

// console.log(powerSum(25, 2));
// => 2
// 5^2
// 4^2 + 3^2



// x, n

// 25, 2
// base = 5, remainder = 0, solution += 1
// i = 4, remainder = 9
// 	9, 2
// 	base = 3, remainder = 0, solution +=1
// 	i = 2, remainder = 5
// 		5, 2
// 		base = 2, remainder = 1, solution +=1
// 		i = 1, remainder = 4
		
			
// i = 3, remainder = 16


// 1, 4, 9, 16, 25, 36, 49, 64, 81