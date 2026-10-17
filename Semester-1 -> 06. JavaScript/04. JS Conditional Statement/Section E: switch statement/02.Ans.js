let ch = "a".toLowerCase();

switch (ch) {
  case "a":
  case "e":
  case "i":
  case "o":
  case "u":
    console.log("Vowel");
    break;

  default:
    if (ch.length === 1 && ch >= "a" && ch <= "z") {
      console.log("Consonant");
    } else {
      console.log("Invalid character");
    }
}