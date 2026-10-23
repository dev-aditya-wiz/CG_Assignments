let fib = [0, 1];
for (let i = 2; i < 15; i++) {
    fib[i] = fib[i - 1] + fib[i - 2];
}
for (let i = 14; i >= 0; i--) {
    console.log(fib[i]);
}

// 377
// 233
// 144
// 89
// 55
// 34
// 21
// 13
// 8
// 5
// 3
// 2
// 1
// 1
// 0