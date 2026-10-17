let marks = 82;

switch (true) {
  case marks >= 75:
    console.log("Distinction");
    break;

  case marks >= 60:
    console.log("1st class");
    break;

  case marks >= 50:
    console.log("2nd class");
    break;

  case marks >= 35:
    console.log("3rd class");
    break;

  default:
    console.log("Failed");
}