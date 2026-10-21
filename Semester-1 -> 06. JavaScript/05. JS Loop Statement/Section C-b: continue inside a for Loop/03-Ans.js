let str = "Hello World";
for (let i = 0; i < str.length; i++) {
    if (str[i] === " ") {
        continue;
    }
    console.log(str[i]);
}

// H
// e
// l
// l
// o
// W
// o
// r
// l
// d