
    let duration = 25 * 60;
    let remaining = duration;
    let timer = null;
    let isRunning = false;

    const display = document.getElementById('pomoTime');
    const startBtn = document.getElementById('pomoStart');
    const resetBtn = document.getElementById('pomoReset');
    const modeWork = document.getElementById('modeWork');
    const modeBreak = document.getElementById('modeBreak');

    function update() {
        const m = Math.floor(remaining / 60);
        const s = remaining % 60;
        display.innerText = `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
    }

    startBtn.addEventListener('click', () => {
        if (isRunning) {
            clearInterval(timer);
            startBtn.innerText = 'Start';
            startBtn.className = 'px-6 py-2.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl text-sm transition';
            isRunning = false;
        } else {
            isRunning = true;
            startBtn.innerText = 'Pause';
            startBtn.className = 'px-6 py-2.5 bg-amber-600 hover:bg-amber-500 text-white font-bold rounded-xl text-sm transition';
            timer = setInterval(() => {
                if (remaining > 0) {
                    remaining--;
                    update();
                } else {
                    clearInterval(timer);
                    isRunning = false;
                    startBtn.innerText = 'Done!';
                }
            }, 1000);
        }
    });

    resetBtn.addEventListener('click', () => {
        clearInterval(timer);
        isRunning = false;
        startBtn.innerText = 'Start';
        startBtn.className = 'px-6 py-2.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl text-sm transition';
        remaining = duration;
        update();
    });

    modeWork.addEventListener('click', () => {
        duration = 25 * 60;
        remaining = duration;
        modeWork.className = 'px-4 py-1.5 rounded-xl bg-cyan-600 text-xs font-bold text-white transition';
        modeBreak.className = 'px-4 py-1.5 rounded-xl bg-slate-700 text-xs font-bold text-slate-300 transition';
        resetBtn.click();
    });

    modeBreak.addEventListener('click', () => {
        duration = 5 * 60;
        remaining = duration;
        modeBreak.className = 'px-4 py-1.5 rounded-xl bg-cyan-600 text-xs font-bold text-white transition';
        modeWork.className = 'px-4 py-1.5 rounded-xl bg-slate-700 text-xs font-bold text-slate-300 transition';
        resetBtn.click();
    });

    update();
    