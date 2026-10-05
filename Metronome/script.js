
    const ctx = new (window.AudioContext || window.webkitAudioContext)();
    let isRunning = false;
    let timer = null;

    const bpmRange = document.getElementById('bpmRange');
    const bpmVal = document.getElementById('bpmVal');
    const toggleBtn = document.getElementById('metroToggle');
    const indicator = document.getElementById('metroIndicator');

    function clickSound() {
        if (ctx.state === 'suspended') ctx.resume();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.frequency.setValueAtTime(1000, ctx.currentTime);
        gain.gain.setValueAtTime(0.5, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.05);
        osc.start();
        osc.stop(ctx.currentTime + 0.05);

        indicator.classList.add('scale-125', 'border-cyan-400');
        setTimeout(() => indicator.classList.remove('scale-125', 'border-cyan-400'), 80);
    }

    bpmRange.addEventListener('input', () => {
        bpmVal.innerText = bpmRange.value;
        if (isRunning) {
            clearInterval(timer);
            timer = setInterval(clickSound, (60 / parseInt(bpmRange.value)) * 1000);
        }
    });

    toggleBtn.addEventListener('click', () => {
        if (!isRunning) {
            isRunning = true;
            toggleBtn.innerText = 'Stop Metronome';
            toggleBtn.className = 'px-8 py-3 bg-rose-600 hover:bg-rose-500 text-white font-bold rounded-xl text-sm transition';
            clickSound();
            timer = setInterval(clickSound, (60 / parseInt(bpmRange.value)) * 1000);
        } else {
            isRunning = false;
            clearInterval(timer);
            toggleBtn.innerText = 'Start Metronome';
            toggleBtn.className = 'px-8 py-3 bg-cyan-600 hover:bg-cyan-500 text-white font-bold rounded-xl text-sm transition';
        }
    });
    