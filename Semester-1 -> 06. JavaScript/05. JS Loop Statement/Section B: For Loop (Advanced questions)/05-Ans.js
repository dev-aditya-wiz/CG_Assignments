let arr = [12, 45, 7, 89, 23, 56];
let largest = arr[0];
for (let i = 1; i < arr.length; i++) {
    if (arr[i] > largest) {
        largest = arr[i];
    }
}
console.log("Largest =", largest);

// Largest = 89