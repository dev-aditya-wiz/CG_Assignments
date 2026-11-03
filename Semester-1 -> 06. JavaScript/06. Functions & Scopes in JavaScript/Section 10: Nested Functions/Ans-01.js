// Q1. Write a function mainTask that contains an inner function helperTask.
// The inner function should return "Task completed successfully".
// Call the inner function from mainTask and return its result.
function mainTask() {

    function helperTask() {
        return "Task completed successfully";
    }

    return helperTask();
}

console.log(mainTask());
