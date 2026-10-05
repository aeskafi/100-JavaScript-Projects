
    let cards = JSON.parse(localStorage.getItem('micro_kanban') || '[]');
    const input = document.getElementById('kanbanInput');

    function save() {
        localStorage.setItem('micro_kanban', JSON.stringify(cards));
        render();
    }

    function render() {
        ['colTodo', 'colProg', 'colDone'].forEach(id => document.getElementById(id).innerHTML = '');
        cards.forEach((c, idx) => {
            const div = document.createElement('div');
            div.className = 'bg-slate-900 border border-slate-800 p-2.5 rounded-xl text-xs flex justify-between items-center';
            div.innerHTML = `
                <span class="text-slate-200 font-medium">${c.text}</span>
                <div class="flex gap-1">
                    ${c.col > 0 ? '<button class="prev px-1.5 py-0.5 bg-slate-800 hover:bg-slate-700 rounded text-cyan-400">←</button>' : ''}
                    ${c.col < 2 ? '<button class="next px-1.5 py-0.5 bg-slate-800 hover:bg-slate-700 rounded text-cyan-400">→</button>' : ''}
                    <button class="del px-1.5 py-0.5 bg-slate-800 hover:bg-rose-900 rounded text-rose-400">✕</button>
                </div>
            `;
            if (div.querySelector('.prev')) div.querySelector('.prev').addEventListener('click', () => { c.col--; save(); });
            if (div.querySelector('.next')) div.querySelector('.next').addEventListener('click', () => { c.col++; save(); });
            div.querySelector('.del').addEventListener('click', () => { cards.splice(idx, 1); save(); });

            const targetId = c.col === 0 ? 'colTodo' : c.col === 1 ? 'colProg' : 'colDone';
            document.getElementById(targetId).appendChild(div);
        });
    }

    document.getElementById('addKanban').addEventListener('click', () => {
        const text = input.value.trim();
        if (!text) return;
        cards.push({ text, col: 0 });
        input.value = '';
        save();
    });

    render();
    