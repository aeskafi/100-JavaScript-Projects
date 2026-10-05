
    const canvas = document.getElementById('fireCanvas');
    const ctx = canvas.getContext('2d');
    let sparks = [];

    function createBurst(x, y) {
        const colors = ['#06b6d4', '#f59e0b', '#ec4899', '#10b981', '#a855f7'];
        const col = colors[Math.floor(Math.random() * colors.length)];
        for (let i = 0; i < 40; i++) {
            const angle = Math.random() * Math.PI * 2;
            const speed = Math.random() * 5 + 1;
            sparks.push({
                x, y,
                vx: Math.cos(angle) * speed,
                vy: Math.sin(angle) * speed,
                alpha: 1,
                color: col
            });
        }
    }

    canvas.addEventListener('click', (e) => {
        const r = canvas.getBoundingClientRect();
        createBurst((e.clientX - r.left) * (canvas.width / r.width), (e.clientY - r.top) * (canvas.height / r.height));
    });

    function loop() {
        ctx.fillStyle = 'rgba(15, 23, 42, 0.25)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        for (let i = sparks.length - 1; i >= 0; i--) {
            const s = sparks[i];
            s.x += s.vx;
            s.y += s.vy;
            s.vy += 0.05; // gravity
            s.alpha -= 0.02;

            if (s.alpha <= 0) {
                sparks.splice(i, 1);
                continue;
            }

            ctx.save();
            ctx.globalAlpha = s.alpha;
            ctx.fillStyle = s.color;
            ctx.fillRect(s.x, s.y, 3, 3);
            ctx.restore();
        }

        requestAnimationFrame(loop);
    }
    createBurst(canvas.width / 2, canvas.height / 3);
    loop();
    