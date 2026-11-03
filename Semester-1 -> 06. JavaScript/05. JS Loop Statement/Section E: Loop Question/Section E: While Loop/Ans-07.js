// Q7. Print Numbers with Conditions
let counter = 1;
while (counter <= 100) {
  if (counter % 3 === 0 && counter % 5 === 0 && counter % 7 !== 0) {
    console.log(counter);
  }
  counter++;
}
