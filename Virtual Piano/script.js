
    const ctx = new (window.AudioContext || window.webkitAudioContext)();

    function playNote(freq) {
        if (ctx.state === 'suspended') ctx.resume();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(freq, ctx.currentTime);

        gain.gain.setValueAtTime(0.5, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 1.2);

        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start();
        osc.stop(ctx.currentTime + 1.2);
    }

    document.querySelectorAll('.piano-key').forEach(key => {
        key.addEventListener('click', () => {
            playNote(parseFloat(key.dataset.note));
        });
    });
    