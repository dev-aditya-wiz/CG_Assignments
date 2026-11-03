let rows4 = 4;
for (let i = 1; i <= rows4; i++) {
  let rowStr = "";
  for (let j = 1; j <= rows4; j++) {
    if (i === 1 || i === rows4 || j === 1 || j === rows4) {
      rowStr += "* ";
    } else {
      rowStr += "  ";
    }
  }
  console.log(rowStr.trimEnd());
}
