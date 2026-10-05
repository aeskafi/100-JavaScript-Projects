
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
    