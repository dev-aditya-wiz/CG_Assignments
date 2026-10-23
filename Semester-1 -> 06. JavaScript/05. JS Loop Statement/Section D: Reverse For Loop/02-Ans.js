let num = 4729;
let product = 1;
let found = false;
for (let n = num; n > 0; n = Math.floor(n / 10)) {
    let digit = n % 10;
    if (digit % 2 !== 0) {
        product *= digit;
        found = true;
    }
}
console.log(found ? product : 0);

// 63