
    let board = Array(9).fill(null);
    let turn = 'X';
    let over = false;

    const grid = document.getElementById('tttGrid');
    const turnEl = document.getElementById('tttTurn');
    const reset = document.getElementById('tttReset');

    const wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ];

    function checkWin() {
        for (let [a,b,c] of wins) {
            if (board[a] && board[a] === board[b] && board[a] === board[c]) return board[a];
        }
        return board.includes(null) ? null : 'Tie';
    }

    function render() {
        grid.innerHTML = '';
        board.forEach((val, i) => {
            const btn = document.createElement('button');
            btn.className = 'w-18 h-18 bg-slate-950 border border-slate-700 rounded-2xl text-3xl font-black flex items-center justify-center transition active:scale-95 ' + (val === 'X' ? 'text-cyan-400' : 'text-amber-400');
            btn.style.height = '70px';
            btn.innerText = val || '';
            btn.addEventListener('click', () => {
                if (over || board[i]) return;
                board[i] = turn;
                const winner = checkWin();
                if (winner) {
                    over = true;
                    turnEl.innerText = winner === 'Tie' ? "It's a Tie Game!" : `🎉 Player ${winner} Wins!`;
                } else {
                    turn = turn === 'X' ? 'O' : 'X';
                    turnEl.innerText = `Player ${turn}'s Turn`;
                }
                render();
            });
            grid.appendChild(btn);
        });
    }

    reset.addEventListener('click', () => {
        board = Array(9).fill(null);
        turn = 'X';
        over = false;
        turnEl.innerText = "Player X's Turn";
        render();
    });

    render();
    