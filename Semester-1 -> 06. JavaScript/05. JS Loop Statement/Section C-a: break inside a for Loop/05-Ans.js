// Create a for loop that prints numbers from 1 to 50. 
// Stop completely (break) as soon as you encounter a number that is 
// both a perfect square and greater than 20.

for (let i = 1; i <= 50; i++) {
    let sqRoot = i ** (1/2);
    if (i > 20 && sqRoot % 1 === 0) {
        console.log(i);
        break;
    }
}

// 25