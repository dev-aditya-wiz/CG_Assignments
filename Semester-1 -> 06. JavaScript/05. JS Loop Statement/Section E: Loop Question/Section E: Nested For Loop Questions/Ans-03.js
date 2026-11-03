let rows1 = 4;
let count = 1;
for (let i = 1; i <= rows1; i++) {
  let rowStr = "";
  for (let j = 1; j <= i; j++) {
    rowStr += count + " ";
    count++;
  }
  console.log(rowStr.trim());
}
