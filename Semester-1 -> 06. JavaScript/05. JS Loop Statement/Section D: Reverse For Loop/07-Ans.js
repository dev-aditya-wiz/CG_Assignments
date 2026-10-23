let temperatures = [32, 28, 41, 19, 35, 27, 38];
let count = 0;
for (let i = temperatures.length - 1; i >= 0; i--) {
    if (temperatures[i] < 30) {
        count++;
    }
}
console.log(count);

// 3