// Given the string "JavaScript", use a for loop to create a new string that contains only the consonants (remove vowels).

// JvScrpt
let str = "JavaScript";
let newStr = ""
for (let i=0; i<=str.length-1; i++) {
    // console.log(str[i])
    if (str[i]!="a" && str[i]!="e" && str[i]!="i" && str[i]!="o" && str[i]!="u") {
        newStr += str[i];
    }
}
console.log(newStr)

// JvScrpt