
    const ctx = new (window.AudioContext || window.webkitAudioContext)();

    function playSfx(type) {
        if (ctx.state === 'suspended') ctx.resume();
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);

        if (type === 'coin') {
            osc.frequency.setValueAtTime(987.77, now);
            osc.frequency.setValueAtTime(1318.51, now + 0.08);
            gain.gain.setValueAtTime(0.3, now);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
            osc.start(now); osc.stop(now + 0.3);
        } else if (type === 'laser') {
            osc.frequency.setValueAtTime(880, now);
            osc.frequency.exponentialRampToValueAtTime(110, now + 0.15);
            gain.gain.setValueAtTime(0.3, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.15);
            osc.start(now); osc.stop(now + 0.15);
        } else if (type === 'jump') {
            osc.frequency.setValueAtTime(150, now);
            osc.frequency.exponentialRampToValueAtTime(600, now + 0.15);
            gain.gain.setValueAtTime(0.3, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.15);
            osc.start(now); osc.stop(now + 0.15);
        } else if (type === 'powerup') {
            osc.frequency.setValueAtTime(300, now);
            osc.frequency.linearRampToValueAtTime(800, now + 0.3);
            gain.gain.setValueAtTime(0.3, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);
            osc.start(now); osc.stop(now + 0.3);
        } else if (type === 'explode') {
            osc.type = 'sawtooth';
            osc.frequency.setValueAtTime(120, now);
            osc.frequency.exponentialRampToValueAtTime(20, now + 0.4);
            gain.gain.setValueAtTime(0.5, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.4);
            osc.start(now); osc.stop(now + 0.4);
        } else if (type === 'victory') {
            [440, 554, 659, 880].forEach((f, idx) => {
                const o = ctx.createOscillator();
                const g = ctx.createGain();
                o.connect(g); g.connect(ctx.destination);
                o.frequency.value = f;
                g.gain.setValueAtTime(0.2, now + idx * 0.1);
                g.gain.exponentialRampToValueAtTime(0.01, now + idx * 0.1 + 0.2);
                o.start(now + idx * 0.1);
                o.stop(now + idx * 0.1 + 0.2);
            });
        }
    }

    document.querySelectorAll('.sfx-btn').forEach(btn => {
        btn.addEventListener('click', () => playSfx(btn.dataset.sfx));
    });
    