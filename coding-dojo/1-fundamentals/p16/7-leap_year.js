// Leap Year
// Write a function that determines whether a given year is a leap year.
// If a year is divisible by four, it is a leap year,
// Unless it is divisible by 100.
// However, if it is divisible by 400, then it is.

function isLeapYear(year){
    if (year % 400 == 0){
        return true;
    }
    else if (year % 100 == 0){
        return false;
    }
    else if (year % 4 == 0){
        return true;
    }
    else {
        return false;
    }
}

console.log(isLeapYear(2400));