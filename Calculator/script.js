let numbers = [];
let operations = [];
let isPositive = true;
let isOperation = false;
let currentNumber = '0';

function init() {

    const calculatorButtons = ["AC", "±", "%", "÷", "7", "8", "9", "x", "4", "5", "6", "-", "1", "2", "3", "+", "0", ".", "="];

    calculatorButtons.forEach(value => {
        var btn = document.createElement('button');

        // zero button need to be wider than another buttons
        if (value === "0") btn.style.gridColumn = 'span 2';

        var btnCaption = document.createTextNode(value);
        btn.appendChild(btnCaption);
        btn.className = "text-white text-4xl border-white border-2 bg-slate-500";

        document.getElementById("operatorContainer").appendChild(btn);
    });

    Array.from(document.getElementsByTagName('button')).forEach(btn => {
        btn.addEventListener('click', (e) => operationHandler(e.target.innerText))
    })

}

const operationHandler = (value) => {
    const typeOfOperation = ["÷", "x", "-", "+", "="];

    if (value === "AC") {
        reset();
        updateResult(currentNumber);
        return;
    }

    if (value === "%" && currentNumber !== "0") {
        currentNumber /= 100;
        currentNumber = currentNumber.toString();
        updateResult(currentNumber);
        return;
    }

    if (value === "±") {
        if ((currentNumber.includes(value) === false) && (currentNumber !== "0")) {
            isPositive != isPositive;
            isPositive && currentNumber[0] === "-" ? currentNumber = currentNumber.substring(1, currentNumber.length) : currentNumber = '-' + currentNumber;
            updateResult(currentNumber);
        }
        return;
    }

    if (value === ".") {
        if (currentNumber.includes(value) === false) {
            currentNumber += value;
            updateResult(currentNumber);
        }
        return;
    }

    if (typeOfOperation.includes(value)) { // !number
        calculate(value);
    } else { //? number
        currentNumber === "0" ? currentNumber = value : currentNumber += value;
        updateResult(currentNumber);
    }

}

// TODO: define a calculator function
function calculate(operate) {
    let total = "";

    operations.push(operate === "=" ? " " : operate);
    numbers.push(currentNumber);
    updateResult(currentNumber);
    currentNumber = "0";

    numbers.map((value, index) => {
        total += value + operations[index];
    });

    if (operate === "=") { //? operator === equal 
        reset(eval(total).toString());
        updateResult(currentNumber);
    }
}

function reset(value = '0') {
    numbers = [];
    operations = [];
    currentNumber = value;
}

const updateResult = () => {
    document.getElementById("result").innerText = currentNumber;
}

window.addEventListener('DOMContentLoaded', init);