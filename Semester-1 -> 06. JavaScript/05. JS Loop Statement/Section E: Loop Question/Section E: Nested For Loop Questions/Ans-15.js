let rows15 = 3;
for (let i = 1; i <= rows15; i++) {
  let rowStr = "";
  for (let s = 1; s <= rows15 - i; s++) {
    rowStr += "  ";
  }
  for (let j = 1; j <= i; j++) {
    rowStr += j + " ";
  }
  for (let j = i - 1; j >= 1; j--) {
    rowStr += j + " ";
  }
  console.log(rowStr.trimEnd());
}
