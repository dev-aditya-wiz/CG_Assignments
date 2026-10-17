let category = "veg";
let item = "paneer";
let size = "full";
let price = 0;

switch (category) {
  case "veg":
    switch (item) {
      case "paneer":
        switch (size) {
          case "half":
            price = 120;
            break;
          case "full":
            price = 220;
            break;
          default:
            console.log("Invalid size");
        }
        break;

      case "burger":
        switch (size) {
          case "half":
            price = 60;
            break;
          case "full":
            price = 100;
            break;
          default:
            console.log("Invalid size");
        }
        break;

      default:
        console.log("Invalid vegetarian item");
    }
    break;

  case "nonveg":
    switch (item) {
      case "chicken":
        switch (size) {
          case "half":
            price = 180;
            break;
          case "full":
            price = 320;
            break;
          default:
            console.log("Invalid size");
        }
        break;

      case "egg":
        switch (size) {
          case "half":
            price = 70;
            break;
          case "full":
            price = 120;
            break;
          default:
            console.log("Invalid size");
        }
        break;

      default:
        console.log("Invalid non-vegetarian item");
    }
    break;

  default:
    console.log("Invalid category");
}

if (price > 0) {
  console.log("Order Summary");
  console.log("Category:", category);
  console.log("Item:", item);
  console.log("Size:", size);
  console.log("Price: ₹" + price);
}