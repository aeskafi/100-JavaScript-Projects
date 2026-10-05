
    const ROWS = 6;
    const COLS = 7;
    let board = Array(ROWS).fill(null).map(() => Array(COLS).fill(0));
    let turn = 1;
    let over = false;

    const grid = document.getElementById('c4Grid');
    const turnEl = document.getElementById('c4Turn');

    function render() {
        grid.innerHTML = '';
        for (let r = 0; r < ROWS; r++) {
            for (let c = 0; c < COLS; c++) {
                const cell = document.createElement('button');
                cell.className = 'w-8 h-8 rounded-full border border-slate-800 ' + (board[r][c] === 1 ? 'bg-cyan-400' : board[r][c] === 2 ? 'bg-amber-400' : 'bg-slate-900 hover:bg-slate-800');
                cell.addEventListener('click', () => drop(c));
                grid.appendChild(cell);
            }
        }
    }

    function drop(col) {
        if (over) return;
        for (let r = ROWS - 1; r >= 0; r--) {
            if (board[r][col] === 0) {
                board[r][col] = turn;
                if (checkWin(r, col)) {
                    over = true;
                    turnEl.innerText = `🎉 Player ${turn} Wins!`;
                } else {
                    turn = turn === 1 ? 2 : 1;
                    turnEl.innerText = `Player ${turn}'s Turn (${turn === 1 ? 'Cyan' : 'Amber'})`;
                }
                render();
                return;
            }
        }
    }

    function checkWin(r, c) {
        const val = board[r][c];
        const dirs = [[0,1], [1,0], [1,1], [1,-1]];
        for (let [dr, dc] of dirs) {
            let count = 1;
            for (let i = 1; i <= 3; i++) {
                const nr = r + dr * i, nc = c + dc * i;
                if (nr >= 0 && nr < ROWS && nc >= 0 && nc < COLS && board[nr][nc] === val) count++; else break;
            }
            for (let i = 1; i <= 3; i++) {
                const nr = r - dr * i, nc = c - dc * i;
                if (nr >= 0 && nr < ROWS && nc >= 0 && nc < COLS && board[nr][nc] === val) count++; else break;
            }
            if (count >= 4) return true;
        }
        return false;
    }

    render();
    