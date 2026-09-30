# Assignment: Introduction to Variables and Datatypes

---

# Part I: Variables (`let`, `var`, `const`)

## Part a — 4 Questions

### 1. Personal Information

```javascript
const name = "Aditya";
let age = 20;
const city = "Ahmedabad";

console.log(name);
console.log(age);
console.log(city);
```

### 2. Change the Score

```javascript
let score = 50;
score = 80;
console.log(score);
```

**Output:**
```text
80
```

### 3. Constant Value

```javascript
const PI = 3.14;
console.log(PI);
```

**Output:**
```text
3.14
```

### 4. Uninitialized Variables

```javascript
var num1;
let num2;

console.log(num1);
console.log(num2);

num1 = 10;
num2 = 20;

console.log(num1);
console.log(num2);
```

**Output:**
```text
undefined
undefined
10
20
```

---

# Part b — 4 Questions

## 5. Choose the Correct Keyword

```javascript
const studentName = "Aditya";
let marks = 75;
const schoolName = "ABC School";

marks = 85;

console.log(studentName);
console.log(marks);
console.log(schoolName);
```

`const` is used for values that should not be reassigned, while `let` is used for values that may change.

## 6. Understand Scope

```javascript
if (true) {
    var a = "var variable";
    let b = "let variable";
    const c = "const variable";

    console.log(a);
    console.log(b);
    console.log(c);
}

console.log(a);
console.log(b);
console.log(c);
```

Inside the block, all three variables can be accessed. Outside the block, `var` can be accessed, but `let` and `const` cannot because they are block-scoped.

The final `console.log(b)` and `console.log(c)` cause `ReferenceError`.

## 7. Test Re-declaration

### `var`

```javascript
var user = "Aditya";
var user = "Rahul";

console.log(user);
```

**Output:**
```text
Rahul
```

`var` allows re-declaration in the same scope.

### `let`

```javascript
let user = "Aditya";
let user = "Rahul";

console.log(user);
```

This produces a **SyntaxError** because `let` does not allow re-declaration in the same scope.

## 8. Test Re-assignment

```javascript
var a = 10;
let b = 20;
const c = 30;

a = 100;
b = 200;

console.log(a);
console.log(b);
console.log(c);
```

**Output:**
```text
100
200
30
```

`var` and `let` allow re-assignment. `const` does not.

Trying this:

```javascript
c = 300;
```

produces a **TypeError**.

---

# Part c — 2 Questions

## 9. Predict and Explain

```javascript
var x = 10;

if (true) {
    var x = 20;
    let y = 30;
    const z = 40;
}

console.log(x);
console.log(y);
console.log(z);
```

**Answer:**

```text
20
ReferenceError: y is not defined
```

`x` becomes `20` because `var` is not block-scoped. `y` and `z` are block-scoped and cannot be accessed outside the `if` block. The program stops at `console.log(y)`, so the `z` statement is not reached.

## 10. Fix the Program

```javascript
const name = "Aditya";

let age = 20;
age = 25;

if (true) {
    var city = "Delhi";
    let country = "India";

    console.log(country);
}

console.log(name);
console.log(age);
console.log(city);

const score = 50;
console.log(score);
```

**Errors fixed:**

1. `const name;` was invalid because `const` must be initialized.
2. `let age` was declared twice; the second declaration was changed to re-assignment.
3. `country` was kept inside the block because `let` is block-scoped.
4. Re-assignment of `const score` was removed.

---

# Part d — 2 Questions

## 11. Predict the Hoisting Behavior

```javascript
console.log(a);
console.log(b);
console.log(c);

var a = 10;
let b = 20;
const c = 30;
```

**Answer:**

```text
undefined
ReferenceError
```

`var` is hoisted and initialized with `undefined`.

`let` and `const` are hoisted but remain in the **Temporal Dead Zone (TDZ)** until their declarations are reached, so accessing them before declaration causes a `ReferenceError`.

| Keyword | Hoisted | Initialized During Hoisting | Access Before Declaration |
|---|---|---|---|
| `var` | Yes | `undefined` | `undefined` |
| `let` | Yes | No | ReferenceError |
| `const` | Yes | No | ReferenceError |

## 12. Fix the Hoisting Errors

```javascript
var x = "Hello";
let y = "World";
const z = "!";

console.log(x);
console.log(y);
console.log(z);

console.log(x + " " + y + z);
```

**Output:**

```text
Hello
World
!
Hello World!
```

---

# Part II: Primitive vs Non-Primitive Data Types

# Part e — Basic Identification

## 1. Classify the Types

```javascript
let wholeNumber = 25;
let decimalNumber = 10.5;
let text = "JavaScript";
let isStudent = true;

console.log(wholeNumber, typeof wholeNumber);
console.log(decimalNumber, typeof decimalNumber);
console.log(text, typeof text);
console.log(isStudent, typeof isStudent);
```

**Output:**

```text
25 number
10.5 number
JavaScript string
true boolean
```

Both whole numbers and decimal numbers have the JavaScript type `number`.

## 2. Undefined vs Null

```javascript
let a;
let b = null;

console.log(a);
console.log(typeof a);

console.log(b);
console.log(typeof b);
```

**Output:**

```text
undefined
undefined
null
object
```

- **`undefined`** means a variable has been declared but has not been assigned a value.
- **`null`** represents an intentional absence of a value.
- `typeof null` returning `"object"` is a historical JavaScript behavior.

## 3. Number Special Values

```javascript
let positiveInfinity = Infinity;
let negativeInfinity = -Infinity;
let notANumber = NaN;
let scientificNumber = 2.5e3;
let largeReadableNumber = 1_000_000;

console.log(positiveInfinity, typeof positiveInfinity);
console.log(negativeInfinity, typeof negativeInfinity);
console.log(notANumber, typeof notANumber);
console.log(scientificNumber, typeof scientificNumber);
console.log(largeReadableNumber, typeof largeReadableNumber);
```

**Output:**

```text
Infinity number
-Infinity number
NaN number
2500 number
1000000 number
```

`NaN` means **Not-a-Number**, but its JavaScript type is still `number`.

## 4. String Styles

```javascript
let singleQuote = 'Hello JavaScript';
let doubleQuote = "Hello JavaScript";

let name = "Aditya";
let templateString = `Hello, ${name}!`;

console.log(singleQuote);
console.log(doubleQuote);
console.log(templateString);
```

**Output:**

```text
Hello JavaScript
Hello JavaScript
Hello, Aditya!
```

---

# Part f — Advanced Primitive Types

## 5. Symbol Uniqueness

```javascript
const symbol1 = Symbol("id");
const symbol2 = Symbol("id");

console.log(symbol1 === symbol2);
```

**Output:**

```text
false
```

Each call to `Symbol()` creates a unique Symbol, even when the descriptions are the same.

### Using Symbols as Object Keys

```javascript
const symbol1 = Symbol("id");
const symbol2 = Symbol("id");

const user = {};

user[symbol1] = "First ID";
user[symbol2] = "Second ID";

console.log(user[symbol1]);
console.log(user[symbol2]);
```

**Output:**

```text
First ID
Second ID
```

## 6. BigInt Precision

```javascript
let regularNumber = 9007199254740991;

console.log(regularNumber + 1);
console.log(regularNumber + 2);
console.log(regularNumber + 3);

let bigNumber = 9007199254740991n;

console.log(bigNumber + 1n);
console.log(bigNumber + 2n);
console.log(bigNumber + 3n);
```

**Output:**

```text
9007199254740992
9007199254740992
9007199254740994
9007199254740992n
9007199254740993n
9007199254740994n
```

`Number.MAX_SAFE_INTEGER` is `9007199254740991`. Beyond the safe integer range, `Number` cannot represent every integer exactly. `BigInt` is designed for large integers and preserves exact integer precision.

`Number` and `BigInt` should not be directly mixed in arithmetic:

```javascript
10 + 10n
```

This causes a `TypeError`.

## 7. Choose the Correct Type

### Unique identifier

**Type:** `Symbol`

```javascript
const id = Symbol("id");
```

### Very large integer requiring exact precision

**Type:** `BigInt`

```javascript
const bigNumber = 9007199254740993n;
```

### Declared but not given a value

**Type:** `undefined`

```javascript
let value;
```

### Intentional empty value

**Type:** `null`

```javascript
let emptyValue = null;
```

---

# Part g — Prediction & Fixing

## 8. Predict the Output

```javascript
let a;
let b = null;
let c = 42;
let d = "Hello";
let e = true;
let f = Symbol("key");
let g = 123n;

console.log(typeof a, a);
console.log(typeof b, b);
console.log(typeof c, c);
console.log(typeof d, d);
console.log(typeof e, e);
console.log(typeof f, f);
console.log(typeof g, g);
```

**Output:**

```text
undefined undefined
object null
number 42
string Hello
boolean true
symbol Symbol(key)
bigint 123n
```

| Variable | Value | `typeof` |
|---|---|---|
| `a` | `undefined` | `undefined` |
| `b` | `null` | `object` |
| `c` | `42` | `number` |
| `d` | `"Hello"` | `string` |
| `e` | `true` | `boolean` |
| `f` | `Symbol("key")` | `symbol` |
| `g` | `123n` | `bigint` |

## 9. Fix the Code

### Corrected Code

```javascript
let num = 10;
let text = "Hello";
let flag = true;
let empty;
let nothing = null;
let unique = Symbol("id");
let big = 9007199254740991n;

console.log(num, text, flag, empty, nothing, unique, big);
```

**Output:**

```text
10 Hello true undefined null Symbol(id) 9007199254740991n
```

### Errors Fixed

- `Hello` → `"Hello"` because strings require quotes.
- `True` → `true` because JavaScript uses lowercase `true`.
- `Null` → `null` because JavaScript uses lowercase `null`.
- `symbol()` → `Symbol()` because JavaScript is case-sensitive.
- `9007199254740991` → `9007199254740991n` to use a `BigInt`.

## 10. Primitive vs Non-Primitive

### a) What is the main difference?

**Primitive data types** represent basic single values and are not objects.

**Non-Primitive data types** are reference types that can contain collections of values or more complex structures.

### b) Why are Number, String, Boolean, Undefined, Null, Symbol, and BigInt called Primitive?

They are called primitive because they represent fundamental values and are not themselves objects.

The seven JavaScript primitive types are:

1. `Number`
2. `String`
3. `Boolean`
4. `Undefined`
5. `Null`
6. `Symbol`
7. `BigInt`

### c) Example of a Non-Primitive data type

An **Object** is a non-primitive data type.

```javascript
const student = {
    name: "Aditya",
    age: 20
};

console.log(student);
```

Objects are non-primitive/reference types because they can contain multiple properties and values and are handled through references.

---
