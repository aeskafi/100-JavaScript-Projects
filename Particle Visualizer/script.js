
    const canvas = document.getElementById('partCanvas');
    const ctx = canvas.getContext('2d');

    const particles = [];
    for (let i = 0; i < 60; i++) {
        particles.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            vx: (Math.random() - 0.5) * 2,
            vy: (Math.random() - 0.5) * 2,
            radius: Math.random() * 2 + 1
        });
    }

    let mouse = { x: canvas.width / 2, y: canvas.height / 2 };
    canvas.addEventListener('mousemove', (e) => {
        const r = canvas.getBoundingClientRect();
        mouse.x = (e.clientX - r.left) * (canvas.width / r.width);
        mouse.y = (e.clientY - r.top) * (canvas.height / r.height);
    });

    function loop() {
        ctx.fillStyle = 'rgba(15, 23, 42, 0.2)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        particles.forEach(p => {
            p.x += p.vx;
            p.y += p.vy;
            if (p.x < 0 || p.x > canvas.width) p.vx *= -1;
            if (p.y < 0 || p.y > canvas.height) p.vy *= -1;

            const dx = mouse.x - p.x;
            const dy = mouse.y - p.y;
            const dist = Math.sqrt(dx * dx + dy * dy);
            if (dist < 100) {
                p.x += dx * 0.02;
                p.y += dy * 0.02;
            }

            ctx.beginPath();
            ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
            ctx.fillStyle = '#06b6d4';
            ctx.fill();
        });

        requestAnimationFrame(loop);
    }
    loop();
    