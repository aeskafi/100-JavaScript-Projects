import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def create_project(folder_name, title, category, icon, description, html_body, js_code):
    dir_path = os.path.join(BASE_DIR, folder_name)
    os.makedirs(dir_path, exist_ok=True)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | 100 JavaScript Projects</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="min-h-screen bg-slate-900 text-slate-100 flex flex-col justify-center items-center p-4 font-sans">
    <div class="w-full max-w-xl bg-slate-800 border border-slate-700 rounded-3xl shadow-2xl p-6 sm:p-8 backdrop-blur-md">
        <a href="../index.html" class="inline-flex items-center text-xs font-semibold text-cyan-400 hover:text-cyan-300 mb-6 transition-colors">
            ← Back to All Projects
        </a>
        <div class="flex items-center justify-between mb-2">
            <h1 class="text-2xl sm:text-3xl font-bold text-white flex items-center gap-2">
                <span>{icon}</span> {title}
            </h1>
            <span class="text-xs font-semibold px-2.5 py-1 rounded-full bg-slate-700 text-cyan-400 border border-slate-600">
                {category}
            </span>
        </div>
        <p class="text-sm text-slate-400 mb-6">{description}</p>
        {html_body}
    </div>
    <script src="script.js"></script>
</body>
</html>"""
    with open(os.path.join(dir_path, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)
    with open(os.path.join(dir_path, 'script.js'), 'w', encoding='utf-8') as f:
        f.write(js_code)
    print(f"Created {folder_name}")

# 61. Tic Tac Toe
create_project(
    "Tic Tac Toe",
    "Tic Tac Toe Game",
    "Games & Puzzles",
    "❌",
    "Classic 3x3 match with smart turn switching and win detection.",
    """
    <div class="space-y-4 text-center">
        <div id="tttTurn" class="text-sm font-bold text-cyan-400 mb-2">Player X's Turn</div>
        <div id="tttGrid" class="grid grid-cols-3 gap-2 max-w-[240px] mx-auto"></div>
        <button id="tttReset" class="px-5 py-2 bg-slate-700 hover:bg-slate-600 text-white rounded-xl text-xs font-bold transition">
            Restart Game
        </button>
    </div>
    """,
    """
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
    """
)

# 62. Rock Paper Scissors
create_project(
    "Rock Paper Scissors",
    "Rock Paper Scissors",
    "Games & Puzzles",
    "✊",
    "Play against the algorithmic computer with live win/loss scorekeeping.",
    """
    <div class="space-y-6 text-center">
        <div class="flex justify-around items-center bg-slate-950 p-4 rounded-2xl border border-slate-700">
            <div>
                <span class="text-xs text-slate-400">Player</span>
                <p id="rpsPScore" class="text-3xl font-black text-cyan-400 font-mono">0</p>
            </div>
            <div id="rpsOutcome" class="text-sm font-bold text-slate-300">Choose your move!</div>
            <div>
                <span class="text-xs text-slate-400">Computer</span>
                <p id="rpsCScore" class="text-3xl font-black text-rose-400 font-mono">0</p>
            </div>
        </div>
        <div class="flex justify-center gap-3">
            <button class="rps-btn p-4 bg-slate-950 hover:bg-cyan-600/30 border border-slate-700 rounded-2xl text-4xl transition active:scale-90" data-move="rock">✊</button>
            <button class="rps-btn p-4 bg-slate-950 hover:bg-cyan-600/30 border border-slate-700 rounded-2xl text-4xl transition active:scale-90" data-move="paper">✋</button>
            <button class="rps-btn p-4 bg-slate-950 hover:bg-cyan-600/30 border border-slate-700 rounded-2xl text-4xl transition active:scale-90" data-move="scissors">✌️</button>
        </div>
    </div>
    """,
    """
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
    """
)

# 63. Memory Card Match
create_project(
    "Memory Card Match",
    "Emoji Memory Match",
    "Games & Puzzles",
    "🧠",
    "Test short-term memory by finding 6 matching emoji pairs in fewer moves.",
    """
    <div class="space-y-4 text-center">
        <div class="flex justify-between items-center text-xs text-slate-400 px-2">
            <span>Moves: <strong id="memMoves" class="text-cyan-400">0</strong></span>
            <button id="memRestart" class="px-3 py-1 bg-slate-700 hover:bg-slate-600 text-white rounded-xl font-bold">Restart</button>
        </div>
        <div id="memGrid" class="grid grid-cols-4 gap-2.5 max-w-[280px] mx-auto"></div>
    </div>
    """,
    """
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
    """
)

# 64. Whack A Mole
create_project(
    "Whack A Mole",
    "Whack-a-Mole Arcade",
    "Games & Puzzles",
    "🐹",
    "Click the popping mole before it ducks back underground in 30 seconds.",
    """
    <div class="space-y-4 text-center">
        <div class="flex justify-around text-sm font-bold">
            <span>Score: <strong id="moleScore" class="text-cyan-400">0</strong></span>
            <span>Time Left: <strong id="moleTime" class="text-amber-400">30s</strong></span>
        </div>
        <div id="moleHoles" class="grid grid-cols-3 gap-3 max-w-[260px] mx-auto"></div>
        <button id="moleStart" class="px-6 py-2.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl text-xs transition">
            Start Whacking!
        </button>
    </div>
    """,
    """
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
    """
)

# 65. Snake Game
create_project(
    "Snake Game",
    "Retro Canvas Snake",
    "Games & Puzzles",
    "🐍",
    "Classic arcade snake with arrow key controls, food apples, and score tracking.",
    """
    <div class="space-y-4 text-center">
        <div class="flex justify-between items-center text-xs text-slate-400 px-2">
            <span>Score: <strong id="snakeScore" class="text-cyan-400">0</strong></span>
            <span>Controls: Arrow Keys</span>
        </div>
        <canvas id="snakeCanvas" width="300" height="300" class="bg-slate-950 border border-slate-700 rounded-2xl mx-auto"></canvas>
        <button id="snakeRestart" class="px-5 py-2 bg-cyan-600 hover:bg-cyan-500 text-white rounded-xl text-xs font-bold transition">
            Start / Restart
        </button>
    </div>
    """,
    """
    const canvas = document.getElementById('snakeCanvas');
    const ctx = canvas.getContext('2d');
    const scoreEl = document.getElementById('snakeScore');
    const restartBtn = document.getElementById('snakeRestart');

    const grid = 15;
    let snake = [{x: 150, y: 150}];
    let dx = grid;
    let dy = 0;
    let food = {x: 60, y: 60};
    let score = 0;
    let loop = null;

    function randomFood() {
        food.x = Math.floor(Math.random() * (canvas.width / grid)) * grid;
        food.y = Math.floor(Math.random() * (canvas.height / grid)) * grid;
    }

    function update() {
        const head = {x: snake[0].x + dx, y: snake[0].y + dy};

        // Wall collision wrap
        if (head.x < 0) head.x = canvas.width - grid;
        if (head.x >= canvas.width) head.x = 0;
        if (head.y < 0) head.y = canvas.height - grid;
        if (head.y >= canvas.height) head.y = 0;

        // Self collision
        for (let i = 1; i < snake.length; i++) {
            if (head.x === snake[i].x && head.y === snake[i].y) {
                clearInterval(loop);
                alert(`Game Over! Score: ${score}`);
                return;
            }
        }

        snake.unshift(head);

        if (head.x === food.x && head.y === food.y) {
            score += 10;
            scoreEl.innerText = score;
            randomFood();
        } else {
            snake.pop();
        }

        ctx.fillStyle = '#0f172a';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.fillStyle = '#ec4899';
        ctx.fillRect(food.x, food.y, grid - 1, grid - 1);

        ctx.fillStyle = '#06b6d4';
        snake.forEach(part => ctx.fillRect(part.x, part.y, grid - 1, grid - 1));
    }

    window.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowUp' && dy === 0) { dx = 0; dy = -grid; }
        if (e.key === 'ArrowDown' && dy === 0) { dx = 0; dy = grid; }
        if (e.key === 'ArrowLeft' && dx === 0) { dx = -grid; dy = 0; }
        if (e.key === 'ArrowRight' && dx === 0) { dx = grid; dy = 0; }
    });

    restartBtn.addEventListener('click', () => {
        clearInterval(loop);
        snake = [{x: 150, y: 150}];
        dx = grid; dy = 0;
        score = 0;
        scoreEl.innerText = '0';
        randomFood();
        loop = setInterval(update, 100);
    });
    """
)

# 66. Simon Says
create_project(
    "Simon Says",
    "Simon Says Memory Game",
    "Games & Puzzles",
    "🎮",
    "Memorize the flashing sequence of colored quadrants and repeat the sequence.",
    """
    <div class="space-y-4 text-center">
        <div id="simonStatus" class="text-sm font-bold text-cyan-400">Click Start to Play!</div>
        <div class="grid grid-cols-2 gap-3 max-w-[220px] mx-auto">
            <button class="simon-pad w-24 h-24 rounded-tl-3xl bg-emerald-700 transition active:scale-95" data-color="0"></button>
            <button class="simon-pad w-24 h-24 rounded-tr-3xl bg-rose-700 transition active:scale-95" data-color="1"></button>
            <button class="simon-pad w-24 h-24 rounded-bl-3xl bg-amber-700 transition active:scale-95" data-color="2"></button>
            <button class="simon-pad w-24 h-24 rounded-br-3xl bg-cyan-700 transition active:scale-95" data-color="3"></button>
        </div>
        <button id="simonStart" class="px-6 py-2 bg-cyan-600 hover:bg-cyan-500 text-white font-bold rounded-xl text-xs transition">
            Start Game
        </button>
    </div>
    """,
    """
    const colors = ['bg-emerald-500', 'bg-rose-500', 'bg-amber-500', 'bg-cyan-500'];
    const darks = ['bg-emerald-700', 'bg-rose-700', 'bg-amber-700', 'bg-cyan-700'];

    let sequence = [];
    let playerStep = 0;

    const pads = document.querySelectorAll('.simon-pad');
    const status = document.getElementById('simonStatus');
    const startBtn = document.getElementById('simonStart');

    function flash(idx) {
        pads[idx].classList.remove(darks[idx]);
        pads[idx].classList.add(colors[idx], 'scale-105');
        setTimeout(() => {
            pads[idx].classList.remove(colors[idx], 'scale-105');
            pads[idx].classList.add(darks[idx]);
        }, 300);
    }

    function playSequence() {
        status.innerText = `Watch sequence (Round ${sequence.length})...`;
        let i = 0;
        const interval = setInterval(() => {
            flash(sequence[i]);
            i++;
            if (i >= sequence.length) {
                clearInterval(interval);
                playerStep = 0;
                status.innerText = 'Your turn!';
            }
        }, 600);
    }

    pads.forEach((pad, idx) => {
        pad.addEventListener('click', () => {
            if (sequence.length === 0) return;
            flash(idx);
            if (idx === sequence[playerStep]) {
                playerStep++;
                if (playerStep === sequence.length) {
                    status.innerText = 'Good job! Next round...';
                    setTimeout(() => {
                        sequence.push(Math.floor(Math.random() * 4));
                        playSequence();
                    }, 1000);
                }
            } else {
                status.innerText = 'Wrong sequence! Game over.';
                sequence = [];
            }
        });
    });

    startBtn.addEventListener('click', () => {
        sequence = [Math.floor(Math.random() * 4)];
        playSequence();
    });
    """
)

# 67. Quiz App
create_project(
    "Quiz App",
    "JavaScript Developer Quiz",
    "Education & Trivia",
    "❓",
    "Interactive multiple choice trivia quiz evaluating core web engineering knowledge.",
    """
    <div class="space-y-4">
        <div id="quizQuestion" class="text-lg font-bold text-white mb-2">Question loading...</div>
        <div id="quizOptions" class="space-y-2"></div>
        <div id="quizScore" class="text-xs text-center text-slate-400 pt-2 font-mono"></div>
    </div>
    """,
    """
    const questions = [
        {
            q: 'Which operator checks for both value and type equality in JavaScript?',
            opts: ['==', '===', '=', '!='],
            ans: 1
        },
        {
            q: 'Which array method returns a brand new array with transformed elements?',
            opts: ['forEach()', 'filter()', 'map()', 'reduce()'],
            ans: 2
        },
        {
            q: 'What is the default value of an uninitialized variable in JS?',
            opts: ['null', '0', 'undefined', 'false'],
            ans: 2
        }
    ];

    let current = 0;
    let score = 0;

    const qEl = document.getElementById('quizQuestion');
    const optsEl = document.getElementById('quizOptions');
    const scoreEl = document.getElementById('quizScore');

    function render() {
        if (current >= questions.length) {
            qEl.innerText = `Quiz Complete! You scored ${score} / ${questions.length} 🎉`;
            optsEl.innerHTML = '<button onclick="location.reload()" class="w-full py-2.5 bg-cyan-600 rounded-xl text-xs font-bold text-white">Restart Quiz</button>';
            scoreEl.innerText = '';
            return;
        }

        const item = questions[current];
        qEl.innerText = item.q;
        optsEl.innerHTML = item.opts.map((opt, i) => `
            <button class="w-full text-left p-3 rounded-xl bg-slate-950 border border-slate-700 hover:border-cyan-400 text-xs font-medium text-slate-200 transition" data-idx="${i}">
                ${opt}
            </button>
        `).join('');

        optsEl.querySelectorAll('button').forEach(btn => {
            btn.addEventListener('click', () => {
                const chosen = parseInt(btn.dataset.idx);
                if (chosen === item.ans) score++;
                current++;
                render();
            });
        });

        scoreEl.innerText = `Question ${current + 1} of ${questions.length}`;
    }

    render();
    """
)

# 68. Hangman
create_project(
    "Hangman",
    "Word Guess Hangman",
    "Games & Puzzles",
    "🔤",
    "Guess secret developer vocabulary before running out of 6 attempts.",
    """
    <div class="space-y-4 text-center">
        <div id="hmWord" class="text-3xl font-mono font-bold tracking-widest text-cyan-400 my-4">_ _ _ _</div>
        <div id="hmStatus" class="text-xs text-slate-400">Mistakes: <strong id="hmErrors" class="text-rose-400">0</strong> / 6</div>
        <div id="hmLetters" class="flex flex-wrap justify-center gap-1.5 max-w-sm mx-auto"></div>
    </div>
    """,
    """
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
    """
)

# 69. Connect Four
create_project(
    "Connect Four",
    "Connect Four Mini",
    "Games & Puzzles",
    "🟡",
    "Two-player 7x6 gravity grid matching 4 discs horizontally, vertically, or diagonally.",
    """
    <div class="space-y-4 text-center">
        <div id="c4Turn" class="text-xs font-bold text-cyan-400">Player 1's Turn (Cyan)</div>
        <div id="c4Grid" class="grid grid-cols-7 gap-1.5 bg-slate-950 p-3 rounded-2xl border border-slate-700 max-w-[280px] mx-auto"></div>
    </div>
    """,
    """
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
    """
)

# 70. 15 Puzzle
create_project(
    "15 Puzzle",
    "15 Sliding Tile Puzzle",
    "Games & Puzzles",
    "🧩",
    "Slide numbered tiles to arrange them sequentially from 1 to 15.",
    """
    <div class="space-y-4 text-center">
        <div id="puz15Grid" class="grid grid-cols-4 gap-2 max-w-[240px] mx-auto bg-slate-950 p-3 rounded-2xl border border-slate-700"></div>
        <button id="puz15Shuffle" class="px-5 py-2 bg-cyan-600 hover:bg-cyan-500 text-white rounded-xl text-xs font-bold transition">
            Shuffle Puzzle
        </button>
    </div>
    """,
    """
    let tiles = [...Array(15).keys()].map(x => x + 1);
    tiles.push(null);

    const grid = document.getElementById('puz15Grid');

    function render() {
        grid.innerHTML = '';
        tiles.forEach((num, idx) => {
            const btn = document.createElement('button');
            btn.className = 'w-12 h-12 rounded-xl text-sm font-bold flex items-center justify-center transition ' + (num ? 'bg-slate-800 text-white hover:bg-cyan-600' : 'bg-transparent');
            btn.innerText = num || '';
            btn.addEventListener('click', () => move(idx));
            grid.appendChild(btn);
        });
    }

    function move(idx) {
        const empty = tiles.indexOf(null);
        const r1 = Math.floor(idx / 4), c1 = idx % 4;
        const r2 = Math.floor(empty / 4), c2 = empty % 4;
        if (Math.abs(r1 - r2) + Math.abs(c1 - c2) === 1) {
            tiles[empty] = tiles[idx];
            tiles[idx] = null;
            render();
        }
    }

    document.getElementById('puz15Shuffle').addEventListener('click', () => {
        for (let i = 0; i < 100; i++) {
            const empty = tiles.indexOf(null);
            const valid = [];
            const r = Math.floor(empty / 4), c = empty % 4;
            if (r > 0) valid.push(empty - 4);
            if (r < 3) valid.push(empty + 4);
            if (c > 0) valid.push(empty - 1);
            if (c < 3) valid.push(empty + 1);
            const pick = valid[Math.floor(Math.random() * valid.length)];
            tiles[empty] = tiles[pick];
            tiles[pick] = null;
        }
        render();
    });

    render();
    """
)

# 71. Tower of Hanoi
create_project(
    "Tower of Hanoi",
    "Tower of Hanoi Puzzle",
    "Games & Puzzles",
    "🗼",
    "Classic recursive disc stacking puzzle from Peg A to Peg C.",
    """
    <div class="space-y-4 text-center">
        <div class="flex justify-around items-end h-36 bg-slate-950 p-4 rounded-2xl border border-slate-700">
            <div id="peg0" class="peg flex flex-col-reverse items-center w-20 border-b-4 border-cyan-500 cursor-pointer"></div>
            <div id="peg1" class="peg flex flex-col-reverse items-center w-20 border-b-4 border-cyan-500 cursor-pointer"></div>
            <div id="peg2" class="peg flex flex-col-reverse items-center w-20 border-b-4 border-cyan-500 cursor-pointer"></div>
        </div>
        <p class="text-xs text-slate-400">Click a peg to pick up top disc, click destination peg to drop.</p>
    </div>
    """,
    """
    const pegs = [[3, 2, 1], [], []];
    let selectedPeg = null;

    function render() {
        for (let i = 0; i < 3; i++) {
            const el = document.getElementById(`peg${i}`);
            el.innerHTML = '';
            pegs[i].forEach(size => {
                const disc = document.createElement('div');
                disc.style.width = `${size * 22}px`;
                disc.className = 'h-5 bg-cyan-500 rounded my-0.5 shadow';
                el.appendChild(disc);
            });
            if (selectedPeg === i) el.classList.add('bg-slate-900');
            else el.classList.remove('bg-slate-900');
        }
    }

    document.querySelectorAll('.peg').forEach((p, idx) => {
        p.addEventListener('click', () => {
            if (selectedPeg === null) {
                if (pegs[idx].length > 0) selectedPeg = idx;
            } else {
                const topFrom = pegs[selectedPeg][pegs[selectedPeg].length - 1];
                const topTo = pegs[idx][pegs[idx].length - 1];
                if (!topTo || topFrom < topTo) {
                    pegs[idx].push(pegs[selectedPeg].pop());
                }
                selectedPeg = null;
            }
            render();
        });
    });

    render();
    """
)

# 72. Minesweeper
create_project(
    "Minesweeper",
    "Minesweeper Classic",
    "Games & Puzzles",
    "💣",
    "Uncover safe grid squares without detonating hidden explosive mines.",
    """
    <div class="space-y-4 text-center">
        <div id="msGrid" class="grid grid-cols-6 gap-1 max-w-[220px] mx-auto bg-slate-950 p-2.5 rounded-2xl border border-slate-700"></div>
        <button id="msReset" class="px-5 py-2 bg-slate-700 hover:bg-slate-600 text-white rounded-xl text-xs font-bold transition">
            New Game
        </button>
    </div>
    """,
    """
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
    """
)

# 73. Reaction Time Tester
create_project(
    "Reaction Time Tester",
    "Reaction Time Benchmark",
    "Games & Puzzles",
    "⚡",
    "Click as fast as possible when the red light changes to green.",
    """
    <div class="space-y-4 text-center">
        <div id="rxBox" class="bg-rose-600 rounded-3xl p-12 min-h-[160px] flex flex-col justify-center items-center cursor-pointer shadow-xl transition-all">
            <span id="rxText" class="text-xl font-black text-white">Click to Start</span>
        </div>
        <p id="rxScore" class="text-sm font-mono text-cyan-400"></p>
    </div>
    """,
    """
    const box = document.getElementById('rxBox');
    const text = document.getElementById('rxText');
    const score = document.getElementById('rxScore');

    let state = 'idle'; // idle, waiting, ready
    let startTime = 0;
    let timeout = null;

    box.addEventListener('click', () => {
        if (state === 'idle') {
            state = 'waiting';
            box.className = 'bg-rose-600 rounded-3xl p-12 min-h-[160px] flex flex-col justify-center items-center cursor-pointer shadow-xl';
            text.innerText = 'Wait for green...';
            score.innerText = '';

            timeout = setTimeout(() => {
                state = 'ready';
                box.className = 'bg-emerald-500 rounded-3xl p-12 min-h-[160px] flex flex-col justify-center items-center cursor-pointer shadow-xl';
                text.innerText = 'CLICK NOW!';
                startTime = Date.now();
            }, Math.random() * 2500 + 1500);
        } else if (state === 'waiting') {
            clearTimeout(timeout);
            state = 'idle';
            box.className = 'bg-slate-700 rounded-3xl p-12 min-h-[160px] flex flex-col justify-center items-center cursor-pointer shadow-xl';
            text.innerText = 'Too early! Click to retry.';
        } else if (state === 'ready') {
            const diff = Date.now() - startTime;
            state = 'idle';
            box.className = 'bg-slate-800 rounded-3xl p-12 min-h-[160px] flex flex-col justify-center items-center cursor-pointer shadow-xl border border-slate-700';
            text.innerText = 'Click to try again';
            score.innerText = `Reaction Time: ${diff} ms! ⚡`;
        }
    });
    """
)

# 74. 2048 Game
create_project(
    "2048 Game",
    "2048 Micro Game",
    "Games & Puzzles",
    "🎯",
    "Combine identical tiles to reach 2048 with swipe or arrow key controls.",
    """
    <div class="space-y-4 text-center">
        <div class="flex justify-between items-center text-xs text-slate-400 px-2">
            <span>Score: <strong id="g2048Score" class="text-cyan-400">0</strong></span>
            <button id="g2048Restart" class="px-3 py-1 bg-slate-700 hover:bg-slate-600 text-white rounded-xl font-bold">Restart</button>
        </div>
        <div id="g2048Grid" class="grid grid-cols-4 gap-2 max-w-[240px] mx-auto bg-slate-950 p-3 rounded-2xl border border-slate-700"></div>
        <div class="flex justify-center gap-2">
            <button id="btnLeft" class="px-3 py-1.5 bg-slate-800 text-white text-xs font-bold rounded-xl">←</button>
            <button id="btnUp" class="px-3 py-1.5 bg-slate-800 text-white text-xs font-bold rounded-xl">↑</button>
            <button id="btnDown" class="px-3 py-1.5 bg-slate-800 text-white text-xs font-bold rounded-xl">↓</button>
            <button id="btnRight" class="px-3 py-1.5 bg-slate-800 text-white text-xs font-bold rounded-xl">→</button>
        </div>
    </div>
    """,
    """
    let grid = Array(16).fill(0);
    let score = 0;

    const board = document.getElementById('g2048Grid');
    const scoreEl = document.getElementById('g2048Score');

    function spawn() {
        const empty = [];
        grid.forEach((v, i) => { if (v === 0) empty.push(i); });
        if (empty.length > 0) {
            grid[empty[Math.floor(Math.random() * empty.length)]] = Math.random() < 0.9 ? 2 : 4;
        }
    }

    function render() {
        board.innerHTML = '';
        grid.forEach(v => {
            const cell = document.createElement('div');
            cell.className = 'w-12 h-12 rounded-xl text-sm font-black flex items-center justify-center ' + (v ? 'bg-cyan-600 text-white shadow' : 'bg-slate-900 text-transparent');
            cell.innerText = v || '';
            board.appendChild(cell);
        });
        scoreEl.innerText = score;
    }

    function slide(row) {
        let arr = row.filter(x => x !== 0);
        for (let i = 0; i < arr.length - 1; i++) {
            if (arr[i] === arr[i + 1]) {
                arr[i] *= 2;
                score += arr[i];
                arr.splice(i + 1, 1);
            }
        }
        while (arr.length < 4) arr.push(0);
        return arr;
    }

    function moveLeft() {
        for (let i = 0; i < 4; i++) {
            const row = [grid[i * 4], grid[i * 4 + 1], grid[i * 4 + 2], grid[i * 4 + 3]];
            const res = slide(row);
            for (let j = 0; j < 4; j++) grid[i * 4 + j] = res[j];
        }
        spawn();
        render();
    }

    function moveRight() {
        for (let i = 0; i < 4; i++) {
            const row = [grid[i * 4 + 3], grid[i * 4 + 2], grid[i * 4 + 1], grid[i * 4]].reverse();
            const res = slide(row.reverse()).reverse();
            for (let j = 0; j < 4; j++) grid[i * 4 + j] = res[j];
        }
        spawn();
        render();
    }

    document.getElementById('btnLeft').addEventListener('click', moveLeft);
    document.getElementById('btnRight').addEventListener('click', moveRight);
    document.getElementById('g2048Restart').addEventListener('click', () => {
        grid.fill(0);
        score = 0;
        spawn(); spawn();
        render();
    });

    spawn(); spawn();
    render();
    """
)

# 75. Guess The Number
create_project(
    "Guess The Number",
    "Higher or Lower Number Guess",
    "Games & Puzzles",
    "🔮",
    "Find the secret integer between 1 and 100 with binary hint feedback.",
    """
    <div class="space-y-4 text-center">
        <input type="number" id="guessInput" min="1" max="100" placeholder="1 - 100" class="w-32 bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-center text-white text-lg font-mono focus:ring-2 focus:ring-cyan-500 outline-none" />
        <div>
            <button id="guessBtn" class="px-6 py-2.5 bg-cyan-600 hover:bg-cyan-500 text-white font-bold rounded-xl text-xs transition">
                Submit Guess
            </button>
        </div>
        <div id="guessFeedback" class="text-sm font-bold text-slate-300">Guess a number between 1 and 100</div>
    </div>
    """,
    """
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
    """
)

# 76. Coin Flip and Dice Roll
create_project(
    "Coin Flip and Dice Roll",
    "Coin Flipper & 3D Dice",
    "Games & Puzzles",
    "🪙",
    "Flip virtual currency coins or roll six-sided dice with probability tracking.",
    """
    <div class="space-y-6 text-center">
        <div class="flex justify-center gap-6">
            <div id="coinFace" class="w-24 h-24 rounded-full bg-amber-500 border-4 border-amber-300 flex items-center justify-center text-xl font-black text-slate-900 shadow-xl transition-transform">
                HEADS
            </div>
            <div id="diceFace" class="w-24 h-24 rounded-2xl bg-white border-4 border-slate-300 flex items-center justify-center text-4xl font-black text-slate-900 shadow-xl transition-transform">
                ⚅
            </div>
        </div>
        <div class="flex justify-center gap-3">
            <button id="flipCoin" class="px-5 py-2.5 bg-amber-600 hover:bg-amber-500 text-white font-bold rounded-xl text-xs transition">Flip Coin</button>
            <button id="rollDice" class="px-5 py-2.5 bg-cyan-600 hover:bg-cyan-500 text-white font-bold rounded-xl text-xs transition">Roll Dice</button>
        </div>
    </div>
    """,
    """
    const coin = document.getElementById('coinFace');
    const dice = document.getElementById('diceFace');
    const diceIcons = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅'];

    document.getElementById('flipCoin').addEventListener('click', () => {
        coin.classList.add('rotate-180');
        setTimeout(() => {
            const isHeads = Math.random() < 0.5;
            coin.innerText = isHeads ? 'HEADS' : 'TAILS';
            coin.classList.remove('rotate-180');
        }, 150);
    });

    document.getElementById('rollDice').addEventListener('click', () => {
        dice.classList.add('scale-90');
        setTimeout(() => {
            dice.innerText = diceIcons[Math.floor(Math.random() * 6)];
            dice.classList.remove('scale-90');
        }, 150);
    });
    """
)

# 77. Typing Fall Game
create_project(
    "Typing Fall Game",
    "Falling Words Typing Game",
    "Games & Puzzles",
    "🌧️",
    "Type falling target words before they hit the ground bottom threshold.",
    """
    <div class="space-y-4 text-center">
        <canvas id="typeFallCanvas" width="400" height="240" class="w-full bg-slate-950 border border-slate-700 rounded-2xl"></canvas>
        <input type="text" id="typeFallInput" placeholder="Type falling words..." class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-white font-mono text-center outline-none" />
    </div>
    """,
    """
    const canvas = document.getElementById('typeFallCanvas');
    const ctx = canvas.getContext('2d');
    const input = document.getElementById('typeFallInput');

    const dictionary = ['code', 'fast', 'mvp', 'build', 'ship', 'stack', 'nomad'];
    let words = [];

    function spawnWord() {
        words.push({
            text: dictionary[Math.floor(Math.random() * dictionary.length)],
            x: Math.random() * (canvas.width - 80) + 20,
            y: 0
        });
    }

    input.addEventListener('input', () => {
        const val = input.value.trim().toLowerCase();
        const idx = words.findIndex(w => w.text === val);
        if (idx !== -1) {
            words.splice(idx, 1);
            input.value = '';
        }
    });

    setInterval(spawnWord, 2000);

    function loop() {
        ctx.fillStyle = '#0f172a';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.font = '16px monospace';
        ctx.fillStyle = '#06b6d4';

        for (let i = words.length - 1; i >= 0; i--) {
            const w = words[i];
            w.y += 0.8;
            ctx.fillText(w.text, w.x, w.y);
            if (w.y > canvas.height) words.splice(i, 1);
        }

        requestAnimationFrame(loop);
    }
    loop();
    """
)

# 78. Word Scramble
create_project(
    "Word Scramble",
    "Word Scramble Solver",
    "Games & Puzzles",
    "🔀",
    "Unscramble letters to find the hidden programming vocabulary term.",
    """
    <div class="space-y-4 text-center">
        <div id="scrambleWord" class="text-3xl font-mono font-bold tracking-widest text-cyan-400 my-4">CODE</div>
        <div class="flex justify-center gap-2">
            <input type="text" id="scrambleInput" placeholder="Unscrambled word..." class="w-48 bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-white text-center font-mono outline-none" />
            <button id="scrambleCheck" class="px-5 py-2 bg-cyan-600 hover:bg-cyan-500 text-white font-bold rounded-xl text-xs transition">Check</button>
        </div>
        <div id="scrambleMsg" class="text-xs text-slate-400">Can you unscramble the word?</div>
    </div>
    """,
    """
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
    """
)
