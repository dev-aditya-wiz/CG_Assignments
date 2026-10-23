let arr = [12, 45, 7, 23, 56, 89, 34];
let largest = -Infinity;
for (let i = arr.length - 1; i >= 0; i--) {
    if (arr[i] < 50 && arr[i] > largest) {
        largest = arr[i];
    }
}
console.log(largest === -Infinity ? "Not found" : largest);

// 45