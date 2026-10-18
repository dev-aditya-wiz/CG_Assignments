let price = 15;
for (let i = 1; i <= 10; i++) {
    let item = i === 1 ? " chocolate = ₹" : " chocolates = ₹";
    console.log(i + item + (i * price));
}