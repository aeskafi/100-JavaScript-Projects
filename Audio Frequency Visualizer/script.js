
    const canvas = document.getElementById('specCanvas');
    const ctx = canvas.getContext('2d');
    const toggle = document.getElementById('specToggle');

    let audioCtx = null;
    let osc = null;
    let isPlaying = false;

    function renderBars() {
        ctx.fillStyle = '#0f172a';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        const bars = 24;
        const width = canvas.width / bars;

        for (let i = 0; i < bars; i++) {
            const h = isPlaying ? (Math.sin(Date.now() / 200 + i) * 0.5 + 0.5) * (canvas.height - 20) + 10 : 8;
            ctx.fillStyle = '#06b6d4';
            ctx.fillRect(i * width + 2, canvas.height - h, width - 4, h);
        }

        requestAnimationFrame(renderBars);
    }

    toggle.addEventListener('click', () => {
        if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        if (!isPlaying) {
            osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            osc.frequency.setValueAtTime(220, audioCtx.currentTime);
            gain.gain.setValueAtTime(0.05, audioCtx.currentTime);
            osc.connect(gain);
            gain.connect(audioCtx.destination);
            osc.start();
            isPlaying = true;
            toggle.innerText = '⏹ Stop Visualizer Sound';
        } else {
            osc.stop();
            isPlaying = false;
            toggle.innerText = '▶ Toggle Visualizer Sound';
        }
    });

    renderBars();
    