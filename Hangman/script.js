
    const words = ['REACT', 'NODE', 'VANILLA', 'CURSOR', 'NOMAD', 'GITHUB'];
    let secret = words[Math.floor(Math.random() * words.length)];
    let guessed = [];
    let errors = 0;

    const wordEl = document.getElementById('hmWord');
    const errorsEl = document.getElementById('hmErrors');
    const lettersEl = document.getElementById('hmLetters');
    const statusEl = document.getElementById('hmStatus');

    function update() {
        let display = '';
        let won = true;
        for (let char of secret) {
            if (guessed.includes(char)) {
                display += char + ' ';
            } else {
                display += '_ ';
                won = false;
            }
        }
        wordEl.innerText = display.trim();
        errorsEl.innerText = errors;

        if (won) {
            statusEl.innerText = '🎉 Congratulations, You Won!';
            statusEl.className = 'text-sm font-bold text-emerald-400';
            lettersEl.innerHTML = '';
        } else if (errors >= 6) {
            wordEl.innerText = secret;
            statusEl.innerText = '💀 Game Over! The word was: ' + secret;
            statusEl.className = 'text-sm font-bold text-rose-400';
            lettersEl.innerHTML = '';
        }
    }

    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('').forEach(l => {
        const btn = document.createElement('button');
        btn.className = 'w-7 h-7 bg-slate-950 border border-slate-700 rounded-lg text-xs font-bold text-slate-300 hover:border-cyan-400';
        btn.innerText = l;
        btn.addEventListener('click', () => {
            btn.disabled = true;
            btn.className = 'w-7 h-7 bg-slate-900 border border-slate-800 rounded-lg text-xs font-bold text-slate-600';
            guessed.push(l);
            if (!secret.includes(l)) errors++;
            update();
        });
        lettersEl.appendChild(btn);
    });

    update();
    