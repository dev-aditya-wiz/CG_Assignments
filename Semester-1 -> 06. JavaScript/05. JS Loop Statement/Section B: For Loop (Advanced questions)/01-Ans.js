let temp = [28, 32, 25, 40, 18, 35];
let count = 0;
for (let i = 0; i <= temp.length - 1; i++) {
    if (temp[i] > 30) {
        count++;
    }
}
console.log("Hot days =", count);

// Hot days = 3