let str = "Programming";
let result = "";
for (let i = str.length - 1; i >= 0; i--) {
    let ch = str[i].toLowerCase();
    if (ch !== "a" && ch !== "e" && ch !== "i" && ch !== "o" && ch !== "u") {
        result += str[i];
    }
}
console.log(result);

// gnmmrgrP