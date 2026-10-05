
    const canvas = document.getElementById('typeFallCanvas');
    const ctx = canvas.getContext('2d');
    const input = document.getElementById('typeFallInput');

    const dictionary = ['code', 'fast', 'mvp', 'build', 'ship', 'stack', 'nomad'];
    let words = [];

    function spawnWord() {
        words.push({
            text: dictionary[Math.floor(Math.random() * dictionary.length)],
            x: Math.random() * (canvas.width - 80) + 20,
            y: 0
        });
    }

    input.addEventListener('input', () => {
        const val = input.value.trim().toLowerCase();
        const idx = words.findIndex(w => w.text === val);
        if (idx !== -1) {
            words.splice(idx, 1);
            input.value = '';
        }
    });

    setInterval(spawnWord, 2000);

    function loop() {
        ctx.fillStyle = '#0f172a';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.font = '16px monospace';
        ctx.fillStyle = '#06b6d4';

        for (let i = words.length - 1; i >= 0; i--) {
            const w = words[i];
            w.y += 0.8;
            ctx.fillText(w.text, w.x, w.y);
            if (w.y > canvas.height) words.splice(i, 1);
        }

        requestAnimationFrame(loop);
    }
    loop();
    