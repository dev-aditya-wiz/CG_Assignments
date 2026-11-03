// Q3.Write a function performanceReport(student, m1, m2, m3) that calculates total and average,
//    then returns a formatted string containing name, total, average and a remark("Excellent"
//    if average ≥ 80, otherwise "Keep Improving").
function performanceReport(student, m1, m2, m3) {
    let total = m1 + m2 + m3;
    let average = total / 3;
    let remark;

    if (average >= 80) {
        remark = "Excellent";
    } else {
        remark = "Keep Improving";
    }

    return `Name: ${student}, Total: ${total}, Average: ${average.toFixed(2)}, Remark: ${remark}`;
}

console.log(performanceReport("Aarav", 90, 85, 95));
