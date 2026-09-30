# Assignment: Introduction to JavaScript

---

## Section A: Short Answer Questions

### Q1. What is JavaScript?

JavaScript is a high-level, dynamically typed programming language used to make web pages interactive and dynamic. It can run in web browsers as well as on servers and other platforms.

### Q2. Who created JavaScript and in which year?

JavaScript was created by **Brendan Eich in 1995** while he was working at Netscape.

### Q3. What was the original name of JavaScript?

The original name of JavaScript was **Mocha**. It was later renamed **LiveScript** and finally **JavaScript**.

### Q4. Is JavaScript the same as Java? Give one major difference.

No, JavaScript and Java are different programming languages.

**Major difference:** Java is mainly a statically typed, class-based programming language, while JavaScript is dynamically typed and commonly used for web development.

### Q5. What does it mean when we say JavaScript is a high-level programming language?

A high-level programming language is designed to be easy for humans to read and write. JavaScript hides complex hardware and memory-management details from the programmer.

```javascript
let total = price + tax;
```

### Q6. Is JavaScript a compiled language or an interpreted language? Explain briefly.

JavaScript is traditionally described as an **interpreted language**, but modern JavaScript engines use **Just-In-Time (JIT) compilation** to improve performance. The engine executes and compiles JavaScript code at runtime.

### Q7. Name the JavaScript engines used by the following browsers.

| Browser | JavaScript Engine |
|---|---|
| Google Chrome | **V8** |
| Mozilla Firefox | **SpiderMonkey** |
| Apple Safari | **JavaScriptCore** |

### Q8. What is Dynamic Typing in JavaScript?

Dynamic typing means that a variable does not have a fixed data type. The type of a variable can change during program execution.

```javascript
let value = 10;
value = "Hello";
value = true;
```

Here, `value` changes from a number to a string and then to a boolean.

### Q9. What is the main difference between a static website and a dynamic website?

- **Static website:** Displays mostly fixed content and does not change automatically based on user interaction or data.
- **Dynamic website:** Content can change based on user actions, databases, or other conditions.

### Q10. Name the three pillars of Front-end Web Development and write one line about each.

1. **HTML** – Defines the structure and content of a webpage.
2. **CSS** – Controls the styling, layout, colors, and appearance.
3. **JavaScript** – Adds behavior, functionality, and interactivity.

### Q11. What is the difference between Frontend and Backend?

- **Frontend:** The part of a website or application that users see and interact with.
- **Backend:** The server-side part that handles data, business logic, authentication, databases, and APIs.

### Q12. What is Node.js?

Node.js is a JavaScript runtime environment that allows JavaScript to run **outside a web browser**, especially on servers.

### Q13. Explain ECMAScript. What is its relation with JavaScript?

**ECMAScript** is a standard/specification that defines how the JavaScript language should work.

JavaScript is an implementation of the ECMAScript standard. New ECMAScript versions introduce features and improvements that JavaScript engines can implement.

---

# Section B: True or False

### 1. JavaScript is a statically typed language.

**False.**

Correct statement: JavaScript is a **dynamically typed** language.

### 2. JavaScript can only run inside the browser.

**False.**

Correct statement: JavaScript can run in browsers and outside browsers using environments such as **Node.js**.

### 3. HTML is responsible for the behaviour of a webpage.

**False.**

Correct statement: **JavaScript** is mainly responsible for adding behavior and interactivity to webpages.

### 4. Node.js allows JavaScript to run outside the browser.

**True.**

### 5. JavaScript is case-insensitive.

**False.**

Correct statement: JavaScript is **case-sensitive**.

### 6. `let name` and `let Name` are the same variable.

**False.**

Correct statement: `name` and `Name` are different variables because JavaScript is case-sensitive.

### 7. ECMAScript is a programming language.

**False.**

Correct statement: ECMAScript is a **language specification/standard** that JavaScript implements.

### 8. React, Angular, and Vue.js are used for Backend development.

**False.**

Correct statement: React, Angular, and Vue.js are primarily used for **Frontend development**.

---

# Section C: Fill in the Blanks

### 1.

JavaScript was created by **Brendan Eich** in the year **1995**.

### 2.

The three technologies used in Front-end development are **HTML, CSS, and JavaScript**.

### 3.

JavaScript engines: Chrome uses **V8**, Firefox uses **SpiderMonkey**.

### 4.

In the restaurant analogy:

**Customer = User**  
**Waiter = API/Communication layer**  
**Chef = Backend/Server**

### 5.

JavaScript file extension is **`.js`**.

---

# Section D: Conceptual Questions

## Q14. Differentiate between a static website and a dynamic website. Give one real-world example of each.

| Static Website | Dynamic Website |
|---|---|
| Content is mostly fixed. | Content can change dynamically. |
| Usually simpler to develop. | Usually involves JavaScript, servers, APIs, or databases. |
| User interaction is limited. | Provides more interactive functionality. |
| Example: A simple portfolio website. | Example: Amazon or Instagram. |

**Example:** A basic personal portfolio with fixed information can be a static website. An online shopping website where products and prices are loaded dynamically is a dynamic website.

## Q15. Explain any two features of JavaScript that make it suitable for creating interactive web pages.

### 1. Event Handling

JavaScript can respond to user actions such as clicks, typing, mouse movement, and form submission.

```javascript
button.addEventListener("click", function() {
    alert("Button clicked!");
});
```

### 2. DOM Manipulation

JavaScript can change HTML elements and their content, styles, and attributes while the page is running.

```javascript
document.getElementById("demo").textContent = "Hello!";
```

## Q16. List any four areas (apart from web browsers) where JavaScript is used today.

| Area | Example Framework/Technology |
|---|---|
| Backend/Server | Node.js, Express.js |
| Mobile Applications | React Native |
| Desktop Applications | Electron |
| AI/ML and Data Science | TensorFlow.js |

JavaScript is also used for tools, automation, games, and other application development.

## Q17. What is the difference between writing JavaScript code inside an HTML file and in an external `.js` file?

### JavaScript inside HTML

JavaScript can be written directly inside an HTML document using the `<script>` tag.

```html
<script>
    alert("Hello JavaScript!");
</script>
```

### External JavaScript

JavaScript can be written in a separate `.js` file.

**HTML:**

```html
<script src="script.js"></script>
```

**script.js:**

```javascript
alert("Hello JavaScript!");
```

### Two advantages of external JavaScript:

1. **Code Reusability:** One JavaScript file can be used by multiple HTML pages.
2. **Better Organization:** HTML and JavaScript are separated, making the project easier to maintain.

## Q18. Explain the difference between Frontend and Backend using the restaurant analogy.

Think of a website as a restaurant.

- **Customer → User:** The customer interacts with the restaurant just like a user interacts with a website.
- **Dining area/menu → Frontend:** This is what the customer sees and interacts with.
- **Waiter → Communication/API:** The waiter takes the customer's request and communicates it to the kitchen.
- **Kitchen → Backend:** The kitchen processes the request and prepares the required result.
- **Database → Storage:** Ingredients and information stored by the restaurant can be compared to data stored in databases.

Therefore, the **frontend is the visible and interactive part**, while the **backend handles processing, data, and business logic behind the scenes**.

## Q19. Why should a beginner learn JavaScript?

A beginner should learn JavaScript because:

1. It is one of the most important languages for **web development**.
2. It allows us to create **interactive and dynamic websites**.
3. It can be used for both **frontend and backend development**.
4. It has a large ecosystem of libraries, frameworks, and tools.
5. JavaScript can also be used for **mobile, desktop, server-side, and other applications**.
6. It provides many career and project opportunities.

---

# Section E: Code-Based Questions

## Q20. Predict the output of the following code and explain why.

```javascript
let value = 25;
console.log(typeof value);

value = "JavaScript";
console.log(typeof value);

value = false;
console.log(typeof value);
```

### Output

```text
number
string
boolean
```

### Explanation

JavaScript is dynamically typed. The variable `value` can store different types of data during execution.

Initially:

```javascript
value = 25;
```

So `typeof value` returns `number`.

Then:

```javascript
value = "JavaScript";
```

The type becomes `string`.

Finally:

```javascript
value = false;
```

The type becomes `boolean`.

## Q21. Write a simple HTML + JavaScript program that displays an alert box.

```html
<!DOCTYPE html>
<html>
<head>
    <title>JavaScript Alert</title>
</head>
<body>

    <button onclick="showMessage()">Click Me</button>

    <script>
        function showMessage() {
            alert("Welcome to JavaScript!");
        }
    </script>

</body>
</html>
```

When the button is clicked, the alert displays:

```text
Welcome to JavaScript!
```

## Q22. Write JavaScript code to demonstrate event-driven programming.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Event Driven Programming</title>
</head>
<body>

    <button id="myBtn">Click Me</button>

    <p id="demo">Click the button.</p>

    <script>
        document.getElementById("myBtn").addEventListener("click", function() {
            document.getElementById("demo").textContent = "Button was clicked!";
        });
    </script>

</body>
</html>
```

The `click` event occurs when the user clicks the button. JavaScript detects the event and changes the paragraph text. This is called **event-driven programming** because the program responds to events generated by the user or system.

---

# Section F: Practical / Application Based

## Q23. Create a complete web page using HTML + JavaScript.

```html
<!DOCTYPE html>
<html>
<head>
    <title>My First JavaScript Page</title>
</head>

<body>

    <h1>My First JavaScript Page</h1>

    <button id="clickBtn">Click Me</button>

    <script>
        console.log("JavaScript is running successfully!");

        document.getElementById("clickBtn").addEventListener("click", function() {

            alert("Hello, B.Tech Student!");

            document.body.style.backgroundColor = "lightblue";

        });
    </script>

</body>
</html>
```
---

# Section G: Higher Order Thinking

## Q24. Why did JavaScript become so popular and multipurpose?

JavaScript became popular because it was originally designed to add interactivity to websites and was supported by major web browsers. As web applications became more advanced, JavaScript evolved and gained a large ecosystem of tools, libraries, and frameworks.

One major reason for its growth was **Node.js**. Node.js allowed JavaScript to run outside the browser, making it possible to use JavaScript for backend/server-side development as well.

JavaScript also became useful in many other areas through technologies such as **React Native** for mobile applications and **Electron** for desktop applications.

**ECMAScript** also played an important role. Regular ECMAScript updates introduced new language features, improvements, and modern programming capabilities. JavaScript engines implemented these features, allowing developers to write more powerful and maintainable applications.

Therefore, JavaScript became a multipurpose language because of its **browser support, continuous development through ECMAScript, Node.js, large ecosystem, and ability to work across different types of applications**.
