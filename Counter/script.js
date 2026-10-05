const init = () => {
    const numberDisplay = document.querySelector('#number');
    const incrementBtn = document.querySelector('#increment');
    const decrementBtn = document.querySelector('#decrement');
    const resetBtn = document.querySelector('#reset');

    let count = 0;

    const updateDisplay = () => {
        numberDisplay.innerText = count;
        if (count > 0) {
            numberDisplay.className = 'w-40 py-3 bg-slate-950 border border-slate-700 rounded-2xl text-4xl font-extrabold text-emerald-400 font-mono shadow-inner';
        } else if (count < 0) {
            numberDisplay.className = 'w-40 py-3 bg-slate-950 border border-slate-700 rounded-2xl text-4xl font-extrabold text-rose-400 font-mono shadow-inner';
        } else {
            numberDisplay.className = 'w-40 py-3 bg-slate-950 border border-slate-700 rounded-2xl text-4xl font-extrabold text-cyan-400 font-mono shadow-inner';
        }
    };

    incrementBtn.addEventListener('click', () => {
        count++;
        updateDisplay();
    });

    decrementBtn.addEventListener('click', () => {
        count--;
        updateDisplay();
    });

    resetBtn.addEventListener('click', () => {
        count = 0;
        updateDisplay();
    });

    window.addEventListener('keydown', (e) => {
        if (e.key === '+' || e.key === '=') {
            count++;
            updateDisplay();
        } else if (e.key === '-' || e.key === '_') {
            count--;
            updateDisplay();
        } else if (e.key === '0' || e.key.toLowerCase() === 'r') {
            count = 0;
            updateDisplay();
        }
    });
};

window.addEventListener('DOMContentLoaded', init);