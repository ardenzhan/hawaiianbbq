// Setting and Swapping
// Set myNumber to 42. Set myName to your name.
// Now swap myNumber into myName & vice versa.

var myNumber = 42;
var myName = 'Arden';

var temp = myName;
myName = myNumber;
myNumber = temp;

console.log(myNumber, myName);