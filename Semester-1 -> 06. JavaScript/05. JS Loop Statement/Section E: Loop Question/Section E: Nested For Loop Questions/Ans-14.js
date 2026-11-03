for (let i = 1; i <= 5; i++) {
  let rowStr = `Table of ${i} (Even products): `;
  for (let j = 1; j <= 10; j++) {
    let product = i * j;
    if (product % 2 === 0) {
      rowStr += product + " ";
    }
  }
  console.log(rowStr.trimEnd());
}
