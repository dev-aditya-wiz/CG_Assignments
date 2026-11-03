// Q9. Check a Palindrome Number
let originalNum = 121;
let temp = originalNum;
let reversedTemp = 0;

while (temp > 0) {
  reversedTemp = (reversedTemp * 10) + (temp % 10);
  temp = Math.floor(temp / 10);
}

if (originalNum === reversedTemp) {
  console.log("Palindrome number");
} else {
  console.log("Not a palindrome number");
}
