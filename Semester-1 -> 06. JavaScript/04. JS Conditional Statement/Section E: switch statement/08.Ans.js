let a = 10;
let b = 3;
let operator = "**";

switch (operator) {
  case "+":
    console.log("Result:", a + b);
    break;

  case "-":
    console.log("Result:", a - b);
    break;

  case "*":
    console.log("Result:", a * b);
    break;

  case "/":
    if (b === 0) {
      console.log("Error: Division by zero is not allowed");
    } else {
      console.log("Result:", a / b);
    }
    break;

  case "%":
    if (b === 0) {
      console.log("Error: Modulo by zero is not allowed");
    } else {
      console.log("Result:", a % b);
    }
    break;

  case "**":
    console.log("Result:", a ** b);
    break;

  default:
    console.log("Invalid operator");
}