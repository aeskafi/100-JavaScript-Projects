
    const pattern = document.getElementById('regPattern');
    const flags = document.getElementById('regFlags');
    const text = document.getElementById('regText');
    const summary = document.getElementById('regSummary');
    const matchesDiv = document.getElementById('regMatches');

    function testRegex() {
        try {
            const re = new RegExp(pattern.value, flags.value);
            const matches = [...text.value.matchAll(re)];
            summary.innerText = `Matches found: ${matches.length}`;
            summary.className = 'text-xs font-bold text-cyan-400 mb-2';
            matchesDiv.innerHTML = matches.map((m, i) => `<div class="bg-slate-950 p-1.5 rounded border border-slate-800"><span class="text-slate-500">#${i+1}:</span> <span class="text-emerald-400">${m[0]}</span> <span class="text-slate-600">(index ${m.index})</span></div>`).join('');
        } catch(e) {
            summary.innerText = 'Regex Error: ' + e.message;
            summary.className = 'text-xs font-bold text-rose-400 mb-2';
            matchesDiv.innerHTML = '';
        }
    }

    [pattern, flags, text].forEach(el => el.addEventListener('input', testRegex));
    testRegex();
    