
    const a = document.getElementById('diffA');
    const b = document.getElementById('diffB');
    const result = document.getElementById('diffResult');

    function compare() {
        const linesA = a.value.split('\n');
        const linesB = b.value.split('\n');
        result.innerHTML = '';

        const max = Math.max(linesA.length, linesB.length);
        for (let i = 0; i < max; i++) {
            const la = linesA[i];
            const lb = linesB[i];
            const div = document.createElement('div');
            if (la === lb) {
                div.className = 'text-slate-400';
                div.innerText = `  ${la}`;
            } else {
                if (la !== undefined) {
                    const da = document.createElement('div');
                    da.className = 'text-rose-400 bg-rose-950/40 px-1 rounded';
                    da.innerText = `- ${la}`;
                    result.appendChild(da);
                }
                if (lb !== undefined) {
                    const db = document.createElement('div');
                    db.className = 'text-emerald-400 bg-emerald-950/40 px-1 rounded';
                    db.innerText = `+ ${lb}`;
                    result.appendChild(db);
                }
                continue;
            }
            result.appendChild(div);
        }
    }

    a.addEventListener('input', compare);
    b.addEventListener('input', compare);
    compare();
    