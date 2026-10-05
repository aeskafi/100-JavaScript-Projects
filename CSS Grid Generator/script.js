
    const demo = document.getElementById('gridDemo');
    const cols = document.getElementById('gridCols');
    const rows = document.getElementById('gridRows');
    const gap = document.getElementById('gridGap');
    const css = document.getElementById('gridCssOut');

    function update() {
        const c = parseInt(cols.value) || 3;
        const r = parseInt(rows.value) || 2;
        const g = parseInt(gap.value) || 8;

        demo.style.display = 'grid';
        demo.style.gridTemplateColumns = `repeat(${c}, 1fr)`;
        demo.style.gridTemplateRows = `repeat(${r}, 1fr)`;
        demo.style.gap = `${g}px`;

        demo.innerHTML = '';
        for (let i = 0; i < c * r; i++) {
            const div = document.createElement('div');
            div.className = 'bg-slate-800 border border-slate-700 rounded-xl flex items-center justify-center text-xs font-bold text-cyan-400';
            div.innerText = i + 1;
            demo.appendChild(div);
        }

        css.value = `display: grid;\ngrid-template-columns: repeat(${c}, 1fr);\ngrid-template-rows: repeat(${r}, 1fr);\ngap: ${g}px;`;
    }

    [cols, rows, gap].forEach(el => el.addEventListener('input', update));
    update();
    