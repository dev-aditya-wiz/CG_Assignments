// Q8. Check a Palindrome Number
let num_do8 = 1221;
let temp_do8 = num_do8;
let rev_do8 = 0;
do {
  rev_do8 = (rev_do8 * 10) + (temp_do8 % 10);
  temp_do8 = Math.floor(temp_do8 / 10);
} while (temp_do8 > 0);
console.log(num_do8 === rev_do8 ? "Palindrome number" : "Not a palindrome number");
