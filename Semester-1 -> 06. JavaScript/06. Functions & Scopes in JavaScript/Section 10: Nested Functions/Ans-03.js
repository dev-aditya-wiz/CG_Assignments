// Q3. Write a function studentStatus(name, marks) containing an inner function getGrade.
//  The inner function returns "A" if marks ≥ 80, "B" if marks ≥ 60, otherwise "C".
//  Return a final sentence using the name and grade.
function studentStatus(name, marks) {

    function getGrade() {
        if (marks >= 80) {
            return "A";
        } else if (marks >= 60) {
            return "B";
        } else {
            return "C";
        }
    }

    return name + " has received grade " + getGrade();
}

console.log(studentStatus("Aarav", 85));
