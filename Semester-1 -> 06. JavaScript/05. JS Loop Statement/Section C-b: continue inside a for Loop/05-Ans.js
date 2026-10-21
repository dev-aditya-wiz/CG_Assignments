let ages = [12, 18, 25, 15, 30, 17, 22];
for (let i = 0; i < ages.length; i++) {
    if (ages[i] < 18) {
        continue;
    }
    console.log(ages[i]);
}

// 18
// 25
// 30
// 22