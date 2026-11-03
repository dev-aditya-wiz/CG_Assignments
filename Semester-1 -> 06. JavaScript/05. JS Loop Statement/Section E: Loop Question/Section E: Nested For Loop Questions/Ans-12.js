let rows12 = 5;
for (let i = rows12; i >= 1; i--) {
  let rowStr = "";
  for (let j = 1; j <= i; j++) {
    if (i === rows12 || j === 1 || j === i) {
      rowStr += "* ";
    } else {
      rowStr += "  ";
    }
  }
  console.log(rowStr.trimEnd());
}
