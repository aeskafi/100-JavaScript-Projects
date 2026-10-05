
    let startTime = 0;
    let elapsed = 0;
    let timer = null;
    let running = false;
    let lapCount = 0;

    const display = document.getElementById('swDisplay');
    const startBtn = document.getElementById('swStart');
    const lapBtn = document.getElementById('swLap');
    const resetBtn = document.getElementById('swReset');
    const laps = document.getElementById('swLaps');

    function formatTime(ms) {
        const totalSec = Math.floor(ms / 1000);
        const hours = Math.floor(totalSec / 3600);
        const minutes = Math.floor((totalSec % 3600) / 60);
        const seconds = totalSec % 60;
        const centis = Math.floor((ms % 1000) / 10);
        return `${String(hours).padStart(2,'0')}:${String(minutes).padStart(2,'0')}:${String(seconds).padStart(2,'0')}.${String(centis).padStart(2,'0')}`;
    }

    startBtn.addEventListener('click', () => {
        if (!running) {
            running = true;
            startTime = Date.now() - elapsed;
            timer = setInterval(() => {
                elapsed = Date.now() - startTime;
                display.innerText = formatTime(elapsed);
            }, 10);
            startBtn.innerText = 'Pause';
            startBtn.className = 'px-6 py-2.5 bg-amber-600 hover:bg-amber-500 text-white font-bold rounded-xl text-sm transition';
        } else {
            running = false;
            clearInterval(timer);
            startBtn.innerText = 'Resume';
            startBtn.className = 'px-6 py-2.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl text-sm transition';
        }
    });

    lapBtn.addEventListener('click', () => {
        if (!running) return;
        lapCount++;
        const div = document.createElement('div');
        div.className = 'flex justify-between py-1 border-b border-slate-800';
        div.innerHTML = `<span class="text-cyan-400">Lap #${lapCount}</span><span>${formatTime(elapsed)}</span>`;
        laps.prepend(div);
    });

    resetBtn.addEventListener('click', () => {
        running = false;
        clearInterval(timer);
        elapsed = 0;
        lapCount = 0;
        display.innerText = '00:00:00.00';
        startBtn.innerText = 'Start';
        startBtn.className = 'px-6 py-2.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl text-sm transition';
        laps.innerHTML = '';
    });
    