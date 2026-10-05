
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
    