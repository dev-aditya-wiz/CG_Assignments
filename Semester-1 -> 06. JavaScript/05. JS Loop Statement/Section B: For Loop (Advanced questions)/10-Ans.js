// Write a for loop that converts a decimal number to its binary representation (without using built-in methods like toString(2)).

// METHOD - 1 //
// 49/2 = 110001 to convert it into binary number
let num = 49;
let binary = ""
for (let i=1; num!=0; i++) {
    let remainder = num % 2;
    binary += remainder;
    num = Math.floor(num/2);
};
let ans = ""
for (let i=binary.length-1; i>=0; i--) {
    ans += binary[i]
}
console.log(ans)
// 110001



// METHOD - 2 //
// 81/2 = 1010001 to convert it into binary number 
let num$ = 81;
let binary$ = ""
for (let i=1; num$ != 0; i++) {
    let remainder = num$ % 2;
    binary$ = remainder + binary$;
    num$ = Math.floor(num$/2);
};
console.log(binary$)
// 1010001