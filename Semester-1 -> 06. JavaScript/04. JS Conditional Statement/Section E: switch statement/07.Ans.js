let value = "0";

switch (value) {
  case 0:
    console.log("Number zero");
    break;

  case "0":
    console.log("String zero");
    break;

  case false:
    console.log("Boolean false");
    break;

  case null:
    console.log("Null value");
    break;

  case undefined:
    console.log("Undefined value");
    break;

  default:
    console.log("Other value");
}