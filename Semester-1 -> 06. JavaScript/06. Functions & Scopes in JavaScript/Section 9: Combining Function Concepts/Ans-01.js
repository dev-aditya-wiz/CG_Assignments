// Q1. Write a function generateMessage(name, score) that calculates whether the student has passed (score ≥ 40) and returns a complete sentence like: "Aarav has scored 65 and the result is Pass".
function generateMessage(name, score) {
    let result;
    if (score >= 40) {
        result = "Pass";
    } else {
        result = "Fail";
    }
    return name + " has scored " + score + " and the result is " + result;
}
console.log(generateMessage("Aarav", 65));
