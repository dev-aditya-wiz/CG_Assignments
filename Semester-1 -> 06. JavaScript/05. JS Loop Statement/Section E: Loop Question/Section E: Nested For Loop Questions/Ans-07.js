let rows7 = 5;
for (let i = 1; i <= rows7; i++) {
  let rowStr = "";
  for (let j = 1; j <= i; j++) {
    if (j === 1 || j === i || i === rows7) {
      rowStr += "* ";
    } else {
      rowStr += "  ";
    }
  }
  console.log(rowStr.trimEnd());
}
