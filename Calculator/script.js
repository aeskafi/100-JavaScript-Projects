let currentOperand = '0';
let previousOperand = '';
let operation = undefined;
let shouldResetScreen = false;

const buttons = [
    { label: 'AC', type: 'fn' },
    { label: '±', type: 'fn' },
    { label: '%', type: 'fn' },
    { label: '÷', type: 'op' },
    { label: '7', type: 'num' },
    { label: '8', type: 'num' },
    { label: '9', type: 'num' },
    { label: '×', type: 'op' },
    { label: '4', type: 'num' },
    { label: '5', type: 'num' },
    { label: '6', type: 'num' },
    { label: '-', type: 'op' },
    { label: '1', type: 'num' },
    { label: '2', type: 'num' },
    { label: '3', type: 'num' },
    { label: '+', type: 'op' },
    { label: '0', type: 'num', span: 2 },
    { label: '.', type: 'num' },
    { label: '=', type: 'op' }
];

function init() {
    const container = document.getElementById('operatorContainer');
    container.innerHTML = '';

    buttons.forEach((btnData) => {
        const btn = document.createElement('button');
        btn.innerText = btnData.label;
        btn.className = `calc-btn calc-btn-${btnData.type}`;
        if (btnData.span === 2) {
            btn.style.gridColumn = 'span 2';
        }
        btn.addEventListener('click', () => handleInput(btnData.label));
        container.appendChild(btn);
    });

    window.addEventListener('keydown', handleKeyboard);
    updateDisplay();
}

function handleInput(val) {
    if (!isNaN(val)) {
        appendNumber(val);
    } else if (val === '.') {
        appendDecimal();
    } else if (val === 'AC') {
        clearAll();
    } else if (val === '±') {
        toggleSign();
    } else if (val === '%') {
        percentage();
    } else if (val === '=') {
        compute();
    } else if (['+', '-', '×', '÷', '*', '/'].includes(val)) {
        const normalized = val === '*' ? '×' : val === '/' ? '÷' : val;
        chooseOperation(normalized);
    }
}

function appendNumber(num) {
    if (currentOperand === '0' || shouldResetScreen) {
        currentOperand = num;
        shouldResetScreen = false;
    } else {
        currentOperand += num;
    }
    updateDisplay();
}

function appendDecimal() {
    if (shouldResetScreen) {
        currentOperand = '0.';
        shouldResetScreen = false;
        updateDisplay();
        return;
    }
    if (!currentOperand.includes('.')) {
        currentOperand += '.';
        updateDisplay();
    }
}

function clearAll() {
    currentOperand = '0';
    previousOperand = '';
    operation = undefined;
    shouldResetScreen = false;
    updateDisplay();
}

function toggleSign() {
    if (currentOperand === '0') return;
    if (currentOperand.startsWith('-')) {
        currentOperand = currentOperand.substring(1);
    } else {
        currentOperand = '-' + currentOperand;
    }
    updateDisplay();
}

function percentage() {
    const num = parseFloat(currentOperand);
    if (!isNaN(num)) {
        currentOperand = (num / 100).toString();
        updateDisplay();
    }
}

function chooseOperation(op) {
    if (operation !== undefined) {
        compute();
    }
    previousOperand = currentOperand;
    operation = op;
    shouldResetScreen = true;
    updateDisplay();
}

function compute() {
    if (operation === undefined || shouldResetScreen) return;
    const prev = parseFloat(previousOperand);
    const curr = parseFloat(currentOperand);
    if (isNaN(prev) || isNaN(curr)) return;

    let result = 0;
    switch (operation) {
        case '+':
            result = prev + curr;
            break;
        case '-':
            result = prev - curr;
            break;
        case '×':
            result = prev * curr;
            break;
        case '÷':
            if (curr === 0) {
                currentOperand = 'Error';
                operation = undefined;
                previousOperand = '';
                shouldResetScreen = true;
                updateDisplay();
                return;
            }
            result = prev / curr;
            break;
        default:
            return;
    }

    currentOperand = Math.round(result * 100000000) / 100000000 + '';
    operation = undefined;
    previousOperand = '';
    shouldResetScreen = true;
    updateDisplay();
}

function updateDisplay() {
    const resultEl = document.getElementById('result');
    const equationEl = document.getElementById('equation');

    resultEl.innerText = currentOperand;
    if (operation != null) {
        equationEl.innerText = `${previousOperand} ${operation}`;
    } else {
        equationEl.innerText = '';
    }
}

function handleKeyboard(e) {
    if (e.key >= '0' && e.key <= '9') handleInput(e.key);
    if (e.key === '.') handleInput('.');
    if (e.key === '=' || e.key === 'Enter') handleInput('=');
    if (e.key === 'Backspace') {
        if (currentOperand.length > 1 && !shouldResetScreen) {
            currentOperand = currentOperand.slice(0, -1);
        } else {
            currentOperand = '0';
        }
        updateDisplay();
    }
    if (e.key === 'Escape' || e.key.toLowerCase() === 'c') handleInput('AC');
    if (e.key === '+') handleInput('+');
    if (e.key === '-') handleInput('-');
    if (e.key === '*') handleInput('×');
    if (e.key === '/') {
        e.preventDefault();
        handleInput('÷');
    }
    if (e.key === '%') handleInput('%');
}

window.addEventListener('DOMContentLoaded', init);