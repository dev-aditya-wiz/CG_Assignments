let rows5 = 6;
for (let i = 1; i <= rows5; i++) {
  let rowStr = "";
  let char = (i % 2 !== 0) ? "#" : "$";
  for (let j = 1; j <= i; j++) {
    rowStr += char + " ";
  }
  console.log(rowStr.trim());
}
