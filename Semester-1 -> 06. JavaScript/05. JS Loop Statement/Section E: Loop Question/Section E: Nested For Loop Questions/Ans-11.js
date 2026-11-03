let rows11 = 5;
let count11 = 15;
for (let i = rows11; i >= 1; i--) {
  let rowStr = "";
  for (let j = 1; j <= i; j++) {
    let numStr = count11 < 10 ? " " + count11 : count11;
    rowStr += numStr + " ";
    count11--;
  }
  console.log(rowStr.trimEnd());
}
