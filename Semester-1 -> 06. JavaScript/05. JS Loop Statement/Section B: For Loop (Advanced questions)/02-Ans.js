let num = 4729;
let numstr = String(num);
let sum = 0;
for (let i=1; i<=numstr.length; i++) {
    let lastDigit = num%10;
    // console.log(lastDigit);
    sum += lastDigit
    num = Math.floor(num/10)
}
console.log(sum)

// 22