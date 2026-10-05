
    const items = ['🚀', '⚡', '🔥', '💻', '🎯', '🥑'];
    let deck = [...items, ...items].sort(() => Math.random() - 0.5);
    let flipped = [];
    let matched = 0;
    let moves = 0;

    const grid = document.getElementById('memGrid');
    const movesEl = document.getElementById('memMoves');

    function render() {
        grid.innerHTML = '';
        deck.forEach((emoji, idx) => {
            const card = document.createElement('button');
            card.className = 'w-16 h-16 bg-slate-950 border border-slate-700 rounded-2xl text-2xl flex items-center justify-center transition active:scale-95';
            card.dataset.index = idx;
            card.innerText = '?';

            card.addEventListener('click', () => {
                if (flipped.length === 2 || card.innerText !== '?' || flipped.some(f => f.idx === idx)) return;
                card.innerText = emoji;
                card.classList.add('border-cyan-400', 'bg-slate-900');
                flipped.push({ idx, emoji, card });

                if (flipped.length === 2) {
                    moves++;
                    movesEl.innerText = moves;
                    if (flipped[0].emoji === flipped[1].emoji) {
                        matched += 2;
                        flipped = [];
                        if (matched === deck.length) {
                            setTimeout(() => alert(`🎉 Solved in ${moves} moves!`), 300);
                        }
                    } else {
                        setTimeout(() => {
                            flipped[0].card.innerText = '?';
                            flipped[0].card.classList.remove('border-cyan-400', 'bg-slate-900');
                            flipped[1].card.innerText = '?';
                            flipped[1].card.classList.remove('border-cyan-400', 'bg-slate-900');
                            flipped = [];
                        }, 700);
                    }
                }
            });
            grid.appendChild(card);
        });
    }

    document.getElementById('memRestart').addEventListener('click', () => {
        deck = [...items, ...items].sort(() => Math.random() - 0.5);
        flipped = [];
        matched = 0;
        moves = 0;
        movesEl.innerText = '0';
        render();
    });

    render();
    