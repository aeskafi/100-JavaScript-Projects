
    let target = Math.floor(Math.random() * 100) + 1;
    let attempts = 0;

    const input = document.getElementById('guessInput');
    const btn = document.getElementById('guessBtn');
    const feedback = document.getElementById('guessFeedback');

    btn.addEventListener('click', () => {
        const val = parseInt(input.value);
        if (isNaN(val)) return;
        attempts++;
        if (val === target) {
            feedback.innerText = `🎉 Correct! The number was ${target}. (Guessed in ${attempts} tries)`;
            feedback.className = 'text-sm font-bold text-emerald-400';
        } else if (val < target) {
            feedback.innerText = `📈 Too LOW! Try higher.`;
            feedback.className = 'text-sm font-bold text-cyan-400';
        } else {
            feedback.innerText = `📉 Too HIGH! Try lower.`;
            feedback.className = 'text-sm font-bold text-rose-400';
        }
    });
    