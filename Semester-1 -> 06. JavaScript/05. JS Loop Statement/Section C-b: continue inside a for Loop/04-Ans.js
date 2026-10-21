for (let i = 1; i <= 12; i++) {
    let result = 6 * i;
    if (result % 5 === 0) {
        continue;
    }
    console.log("6 x " + i + " = " + result);
}

// 6 x 1 = 6
// 6 x 2 = 12
// 6 x 3 = 18
// 6 x 4 = 24
// 6 x 6 = 36
// 6 x 7 = 42
// 6 x 8 = 48
// 6 x 9 = 54
// 6 x 11 = 66
// 6 x 12 = 72