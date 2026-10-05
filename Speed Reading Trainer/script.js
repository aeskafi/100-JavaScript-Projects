
    const sample = "Rapid serial visual presentation enables readers to absorb text at extreme velocity by eliminating the need for ocular saccades across printed lines. As you practice daily, comprehension and speed scale dramatically!".split(' ');

    let idx = 0;
    let timer = null;
    const wordEl = document.getElementById('speedWord');
    const startBtn = document.getElementById('speedStart');
    const resetBtn = document.getElementById('speedReset');
    const range = document.getElementById('wpmRange');
    const wpmVal = document.getElementById('wpmVal');

    range.addEventListener('input', () => { wpmVal.innerText = range.value; });

    startBtn.addEventListener('click', () => {
        if (timer) {
            clearInterval(timer);
            timer = null;
            startBtn.innerText = 'Resume';
            return;
        }
        startBtn.innerText = 'Pause';
        const delay = (60 / parseInt(range.value)) * 1000;
        timer = setInterval(() => {
            if (idx < sample.length) {
                wordEl.innerText = sample[idx];
                idx++;
            } else {
                clearInterval(timer);
                timer = null;
                startBtn.innerText = 'Restart';
                idx = 0;
            }
        }, delay);
    });

    resetBtn.addEventListener('click', () => {
        clearInterval(timer);
        timer = null;
        idx = 0;
        wordEl.innerText = 'Ready';
        startBtn.innerText = 'Start Training';
    });
    