
    const pool = ['JAVASCRIPT', 'COMPILER', 'ALGORITHM', 'ASYNC', 'VARIABLE'];
    let original = pool[Math.floor(Math.random() * pool.length)];

    function scramble(str) {
        return str.split('').sort(() => Math.random() - 0.5).join('');
    }

    const wordEl = document.getElementById('scrambleWord');
    const input = document.getElementById('scrambleInput');
    const checkBtn = document.getElementById('scrambleCheck');
    const msg = document.getElementById('scrambleMsg');

    wordEl.innerText = scramble(original);

    checkBtn.addEventListener('click', () => {
        if (input.value.trim().toUpperCase() === original) {
            msg.innerText = '🎉 Correct! Loading next word...';
            msg.className = 'text-xs font-bold text-emerald-400';
            setTimeout(() => {
                original = pool[Math.floor(Math.random() * pool.length)];
                wordEl.innerText = scramble(original);
                input.value = '';
                msg.innerText = 'Can you unscramble the word?';
                msg.className = 'text-xs text-slate-400';
            }, 1200);
        } else {
            msg.innerText = 'Incorrect, try again!';
            msg.className = 'text-xs font-bold text-rose-400';
        }
    });
    