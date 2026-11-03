let n13 = 5;
for (let i = 1; i <= n13; i++) {
  let rowStr = "";
  for (let j = 1; j <= n13; j++) {
    if (i === j) {
      rowStr += "  ";
    } else {
      rowStr += "* ";
    }
  }
  console.log(rowStr.trimEnd());
}
