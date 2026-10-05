
    const canvas = document.getElementById('lifeCanvas');
    const ctx = canvas.getContext('2d');
    const COLS = 28;
    const ROWS = 28;
    const RES = 10;

    let grid = Array(COLS).fill(null).map(() => Array(ROWS).fill(0));
    let running = false;
    let timer = null;

    function seed() {
        for (let i = 0; i < COLS; i++) {
            for (let j = 0; j < ROWS; j++) {
                grid[i][j] = Math.random() < 0.25 ? 1 : 0;
            }
        }
        draw();
    }

    function draw() {
        ctx.fillStyle = '#0f172a';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#06b6d4';
        for (let i = 0; i < COLS; i++) {
            for (let j = 0; j < ROWS; j++) {
                if (grid[i][j]) ctx.fillRect(i * RES, j * RES, RES - 1, RES - 1);
            }
        }
    }

    function step() {
        const next = grid.map(arr => [...arr]);
        for (let x = 0; x < COLS; x++) {
            for (let y = 0; y < ROWS; y++) {
                let neighbors = 0;
                for (let i = -1; i <= 1; i++) {
                    for (let j = -1; j <= 1; j++) {
                        if (i === 0 && j === 0) continue;
                        const col = (x + i + COLS) % COLS;
                        const row = (y + j + ROWS) % ROWS;
                        neighbors += grid[col][row];
                    }
                }
                if (grid[x][y] === 1 && (neighbors < 2 || neighbors > 3)) next[x][y] = 0;
                else if (grid[x][y] === 0 && neighbors === 3) next[x][y] = 1;
            }
        }
        grid = next;
        draw();
    }

    document.getElementById('lifeToggle').addEventListener('click', () => {
        running = !running;
        if (running) timer = setInterval(step, 100);
        else clearInterval(timer);
    });

    document.getElementById('lifeSeed').addEventListener('click', seed);
    seed();
    