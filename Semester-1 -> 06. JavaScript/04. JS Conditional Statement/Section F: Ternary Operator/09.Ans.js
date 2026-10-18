// 09. Convert the following decision tree into one single nested ternary expression:
// if (role === "admin") {
//   if (action === "delete") → "Admin Delete"
//   else if (action === "edit") → "Admin Edit"
//   else → "Admin Other"
// } else if (role === "user") {
//   if (action === "view") → "User View"
//   else → "User Restricted"
// } else {
//   → "Invalid Role"
// }

let role = "admin";
let action = "edit";

let result = role === "admin"
    ? (action === "delete" ? "Admin Delete" : action === "edit" ? "Admin Edit" : "Admin Other")
    : role === "user" ? (action === "view" ? "User View" : "User Restricted") : "Invalid Role";

console.log(result);

// Admin Edit