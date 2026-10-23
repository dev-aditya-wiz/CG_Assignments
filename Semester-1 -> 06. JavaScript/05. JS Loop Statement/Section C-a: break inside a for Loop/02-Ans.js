let correctPass = "1234";
let pass = "1111";
for (let i = 1; i <= 5; i++) {
    if (pass === correctPass) {
        console.log("Access granted");
        break;
    }
    if (i === 5) {
        console.log("Account locked");
    }
}
// Account locked

let password = 1234;
let flag = false;
for(let i=1; i<=5;i++){
  let enteredPassword = prompt ("Enter the password: ");
  if(parseInt (enteredPassword)===password){
    console. log("Access granted");
    flag = true;
    break;
  }
}
if(!flag){
  console.log("Account locked!")
}