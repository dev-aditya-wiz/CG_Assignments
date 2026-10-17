let role = "admin";
let action = "create";

switch (role) {
  case "admin":
    switch (action) {
      case "create":
        console.log("Admin can create");
        break;

      case "edit":
        console.log("Admin can edit");
        break;

      case "delete":
        console.log("Admin can delete");
        break;

      default:
        console.log("Invalid action");
    }
    break;

  case "user":
    console.log("Limited Access");
    break;

  default:
    console.log("Invalid role");
}