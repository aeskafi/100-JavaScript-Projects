
    const holes = document.getElementById('moleHoles');
    const scoreEl = document.getElementById('moleScore');
    const timeEl = document.getElementById('moleTime');
    const startBtn = document.getElementById('moleStart');

    let score = 0;
    let timeLeft = 30;
    let timer = null;
    let moleTimer = null;
    let currentHole = -1;

    for (let i = 0; i < 9; i++) {
        const h = document.createElement('button');
        h.className = 'w-18 h-18 bg-slate-950 border-2 border-slate-700 rounded-2xl text-3xl flex items-center justify-center transition';
        h.style.height = '70px';
        h.addEventListener('click', () => {
            if (currentHole === i) {
                score++;
                scoreEl.innerText = score;
                h.innerText = '💥';
                currentHole = -1;
                setTimeout(() => h.innerText = '', 200);
            }
        });
        holes.appendChild(h);
    }

    startBtn.addEventListener('click', () => {
        score = 0;
        timeLeft = 30;
        scoreEl.innerText = '0';
        timeEl.innerText = '30s';
        startBtn.disabled = true;

        clearInterval(timer);
        clearInterval(moleTimer);

        moleTimer = setInterval(() => {
            const btns = holes.querySelectorAll('button');
            btns.forEach(b => b.innerText = '');
            currentHole = Math.floor(Math.random() * 9);
            btns[currentHole].innerText = '🐹';
        }, 700);

        timer = setInterval(() => {
            timeLeft--;
            timeEl.innerText = `${timeLeft}s`;
            if (timeLeft <= 0) {
                clearInterval(timer);
                clearInterval(moleTimer);
                holes.querySelectorAll('button').forEach(b => b.innerText = '');
                startBtn.disabled = false;
                alert(`Game Over! Final Score: ${score}`);
            }
        }, 1000);
    });
    