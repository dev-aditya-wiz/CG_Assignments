let price = 150;
for (let people = 1; people <= 8; people++) {
    let person = people === 1 ? " person: ₹" : " people: ₹";
    console.log(people + person + (people * price));
}


for (let i = 1; i <= 8; i++) {
    console.log(i + " people: ₹" + (i * 150));
}


for (let i = 1; i <= 8; i++) {
    console.log(i + " people: ₹" + (i * price));
}


for (let i = 1; i <= 8; i++) {
    total += 150;
    console.log(i + " people: ₹" + total);
}