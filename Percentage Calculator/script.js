const init = () => {
    document.getElementById('x_1').focus();

    document.getElementById('c_1').addEventListener('click', calculateFirst);
    document.getElementById('c_2').addEventListener('click', calculateSecond);
    document.getElementById('c_3').addEventListener('click', calculateThird);

    // Support Enter key on all inputs
    ['x_1', 'y_1'].forEach((id) => {
        document.getElementById(id).addEventListener('keydown', (e) => {
            if (e.key === 'Enter') calculateFirst();
        });
    });

    ['x_2', 'y_2'].forEach((id) => {
        document.getElementById(id).addEventListener('keydown', (e) => {
            if (e.key === 'Enter') calculateSecond();
        });
    });

    ['x_3', 'y_3'].forEach((id) => {
        document.getElementById(id).addEventListener('keydown', (e) => {
            if (e.key === 'Enter') calculateThird();
        });
    });
};

function formatNumber(num) {
    if (isNaN(num)) return 'Invalid input';
    return Number.isInteger(num) ? num.toString() : num.toFixed(2).replace(/\.?0+$/, '');
}

function calculateFirst() {
    // What is X% of Y? (X / 100) * Y
    const x = parseFloat(document.getElementById('x_1').value);
    const y = parseFloat(document.getElementById('y_1').value);
    const resultEl = document.getElementById('z_1');

    if (isNaN(x) || isNaN(y)) {
        resultEl.innerText = 'Please enter valid numbers';
        return;
    }

    const result = (x / 100) * y;
    resultEl.innerText = formatNumber(result);
}

function calculateSecond() {
    // X is what % of Y? (X / Y) * 100
    const x = parseFloat(document.getElementById('x_2').value);
    const y = parseFloat(document.getElementById('y_2').value);
    const resultEl = document.getElementById('z_2');

    if (isNaN(x) || isNaN(y)) {
        resultEl.innerText = 'Please enter valid numbers';
        return;
    }

    if (y === 0) {
        resultEl.innerText = 'Division by zero is undefined';
        return;
    }

    const result = (x / y) * 100;
    resultEl.innerText = `${formatNumber(result)}%`;
}

function calculateThird() {
    // % increase/decrease from X to Y: ((Y - X) / X) * 100
    const x = parseFloat(document.getElementById('x_3').value);
    const y = parseFloat(document.getElementById('y_3').value);
    const resultEl = document.getElementById('z_3');

    if (isNaN(x) || isNaN(y)) {
        resultEl.innerText = 'Please enter valid numbers';
        return;
    }

    if (x === 0) {
        resultEl.innerText = 'Base value cannot be zero';
        return;
    }

    const diff = y - x;
    const result = (diff / x) * 100;
    const direction = diff >= 0 ? 'increase' : 'decrease';
    resultEl.innerText = `${formatNumber(Math.abs(result))}% ${direction}`;
}

window.addEventListener('DOMContentLoaded', init);