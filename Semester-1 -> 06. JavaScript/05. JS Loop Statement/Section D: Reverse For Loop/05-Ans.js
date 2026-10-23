let num = 12321;
let original = num;
let reversed = 0;
for (let n = num; n > 0; n = Math.floor(n / 10)) {
    let digit = n % 10;
    reversed = reversed * 10 + digit;
}
if (original === reversed) {
    console.log("Palindrome");
} else {
    console.log("Not a palindrome");
}

// Palindrome