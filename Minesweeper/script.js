
    const SIZE = 6;
    const MINES = 5;
    let grid = [];
    let revealed = [];

    const boardEl = document.getElementById('msGrid');

    function init() {
        grid = Array(SIZE * SIZE).fill(0);
        revealed = Array(SIZE * SIZE).fill(false);

        let placed = 0;
        while (placed < MINES) {
            const idx = Math.floor(Math.random() * (SIZE * SIZE));
            if (grid[idx] !== -1) {
                grid[idx] = -1;
                placed++;
            }
        }

        for (let i = 0; i < SIZE * SIZE; i++) {
            if (grid[i] === -1) continue;
            let count = 0;
            const r = Math.floor(i / SIZE), c = i % SIZE;
            for (let dr = -1; dr <= 1; dr++) {
                for (let dc = -1; dc <= 1; dc++) {
                    const nr = r + dr, nc = c + dc;
                    if (nr >= 0 && nr < SIZE && nc >= 0 && nc < SIZE && grid[nr * SIZE + nc] === -1) count++;
                }
            }
            grid[i] = count;
        }

        render();
    }

    function render() {
        boardEl.innerHTML = '';
        for (let i = 0; i < SIZE * SIZE; i++) {
            const btn = document.createElement('button');
            btn.className = 'w-8 h-8 rounded-lg text-xs font-bold flex items-center justify-center ' + (revealed[i] ? 'bg-slate-800 text-cyan-400' : 'bg-slate-900 hover:bg-slate-800 text-white');
            if (revealed[i]) {
                btn.innerText = grid[i] === -1 ? '💣' : (grid[i] > 0 ? grid[i] : '');
            }
            btn.addEventListener('click', () => {
                if (grid[i] === -1) {
                    revealed.fill(true);
                    render();
                    alert('💥 Boom! Game Over.');
                } else {
                    revealed[i] = true;
                    render();
                }
            });
            boardEl.appendChild(btn);
        }
    }

    document.getElementById('msReset').addEventListener('click', init);
    init();
    