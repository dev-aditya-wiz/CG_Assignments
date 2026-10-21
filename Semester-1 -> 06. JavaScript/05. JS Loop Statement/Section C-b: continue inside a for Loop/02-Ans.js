let arr = [10, -5, 20, -3, 7, -8];
let sum = 0;
for (let i = 0; i < arr.length; i++) {
    if (arr[i] <= 0) {
        continue;
    }
    sum = sum + arr[i];
}
console.log(sum);

// 37