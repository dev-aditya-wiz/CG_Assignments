let sum = 0;
for (let i = 1; i <= 100; i++) {
    sum = sum + i;
    if (sum > 100) {
        console.log("Last number added =", i);
        console.log("Sum =", sum);
        break;
    }
}

// Last number added = 14
// Sum = 105