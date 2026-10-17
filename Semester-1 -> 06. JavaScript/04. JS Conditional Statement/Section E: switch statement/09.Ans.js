let day = 15;

switch (true) {
  case day >= 1 && day <= 10:
    console.log("Beginning of the month");
    break;

  case day >= 11 && day <= 20:
    console.log("Middle of the month");
    break;

  case day >= 21 && day <= 31:
    console.log("End of the month");
    break;

  default:
    console.log("Invalid day");
}