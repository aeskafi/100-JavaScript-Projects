
    const ctx = new (window.AudioContext || window.webkitAudioContext)();

    function playDrum(freq) {
        if (ctx.state === 'suspended') ctx.resume();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);

        osc.frequency.setValueAtTime(freq, ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.3);
        gain.gain.setValueAtTime(1, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.3);

        osc.start();
        osc.stop(ctx.currentTime + 0.3);
    }

    document.querySelectorAll('.drum-pad').forEach(pad => {
        pad.addEventListener('click', () => {
            playDrum(parseFloat(pad.dataset.freq));
        });
    });

    window.addEventListener('keydown', (e) => {
        const pad = document.querySelector(`.drum-pad[data-key="${e.key.toLowerCase()}"]`);
        if (pad) {
            pad.click();
            pad.classList.add('scale-95', 'border-cyan-400');
            setTimeout(() => pad.classList.remove('scale-95', 'border-cyan-400'), 150);
        }
    });
    