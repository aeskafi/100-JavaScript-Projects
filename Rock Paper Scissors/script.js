
    let pScore = 0;
    let cScore = 0;
    const moves = ['rock', 'paper', 'scissors'];
    const pScoreEl = document.getElementById('rpsPScore');
    const cScoreEl = document.getElementById('rpsCScore');
    const outcomeEl = document.getElementById('rpsOutcome');

    document.querySelectorAll('.rps-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const pMove = btn.dataset.move;
            const cMove = moves[Math.floor(Math.random() * 3)];

            if (pMove === cMove) {
                outcomeEl.innerText = `Tie! Both picked ${pMove}`;
                outcomeEl.className = 'text-sm font-bold text-amber-400';
            } else if (
                (pMove === 'rock' && cMove === 'scissors') ||
                (pMove === 'paper' && cMove === 'rock') ||
                (pMove === 'scissors' && cMove === 'paper')
            ) {
                pScore++;
                outcomeEl.innerText = `You Win! ${pMove} beats ${cMove}`;
                outcomeEl.className = 'text-sm font-bold text-emerald-400';
            } else {
                cScore++;
                outcomeEl.innerText = `Computer Wins! ${cMove} beats ${pMove}`;
                outcomeEl.className = 'text-sm font-bold text-rose-400';
            }
            pScoreEl.innerText = pScore;
            cScoreEl.innerText = cScore;
        });
    });
    