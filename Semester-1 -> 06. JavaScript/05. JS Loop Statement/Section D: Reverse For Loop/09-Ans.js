let scores = [90, 85, 70, 95, 60, 88, 75];
for (let i = scores.length - 1; i >= 0; i--) {
    if (scores[i] > 80) {
        console.log("Score:", scores[i]);
        console.log("Index:", i);
        break;
    }
}

// Score: 88
// Index: 5