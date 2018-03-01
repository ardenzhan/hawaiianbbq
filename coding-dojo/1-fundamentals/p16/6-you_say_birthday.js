// You Say It's Your Birthday
// If 2 given numbers represent your birth month and day in either order,
// log "How did you know?"
// else log "Just another day..."

const BIRTH_MONTH = 8;
const BIRTH_DAY = 3;

var givenMonth = 3;
var givenDay = 8;

function checkBDay(month, day){
    if ((month == BIRTH_MONTH && day == BIRTH_DAY) || (month == BIRTH_DAY && day == BIRTH_MONTH)){
        console.log("How did you know?");
    }
    else {
        console.log("Just another day...");
    }
}

checkBDay(givenMonth, givenDay);