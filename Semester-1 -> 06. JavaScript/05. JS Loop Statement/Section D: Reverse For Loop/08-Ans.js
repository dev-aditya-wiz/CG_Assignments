let num = 13;
let binary = "";
if (num === 0) {
    binary = "0";
}
for (let n = num; n > 0; n = Math.floor(n / 2)) {
    let remainder = n % 2;
    binary += remainder;
}
console.log(binary);

// 1011