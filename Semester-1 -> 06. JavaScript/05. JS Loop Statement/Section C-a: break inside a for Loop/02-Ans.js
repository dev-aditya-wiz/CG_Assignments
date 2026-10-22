let correctPassword = "1234";
let password = "1111";
for (let i = 1; i <= 5; i++) {
    if (password === correctPassword) {
        console.log("Access granted");
        break;
    }
    if (i === 5) {
        console.log("Account locked");
    }
}
// Account locked