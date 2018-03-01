// https://www.hackerrank.com/challenges/the-power-sum/problem

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

function powerSum(x, sol = []){
    if (x == 0) return;

    // let base = Math.floor(Math.pow(x, 1/n));
    let base = x;
 
    for (let i = base; i >= 1; i--){
        sol.push(i);
        if (i == 1) console.log(sol);
        powerSum(i-1, sol.slice(x-i, i+1));
        
    }
}

powerSum(4);