
    let habits = JSON.parse(localStorage.getItem('micro_habits') || '[]');
    const input = document.getElementById('habitInput');
    const list = document.getElementById('habitList');

    function save() {
        localStorage.setItem('micro_habits', JSON.stringify(habits));
        render();
    }

    function render() {
        list.innerHTML = '';
        if (habits.length === 0) {
            list.innerHTML = '<div class="text-xs text-slate-500 text-center py-4">No habits tracked yet. Start small today!</div>';
            return;
        }
        habits.forEach((h, hIdx) => {
            const card = document.createElement('div');
            card.className = 'bg-slate-900 border border-slate-700 p-3 rounded-2xl';
            const daysHtml = h.days.map((done, dIdx) => `
                <button class="w-7 h-7 rounded-lg text-xs font-bold transition ${done ? 'bg-emerald-500 text-white' : 'bg-slate-800 text-slate-400'}" data-day="${dIdx}">
                    D${dIdx + 1}
                </button>
            `).join('');

            card.innerHTML = `
                <div class="flex justify-between items-center mb-2">
                    <span class="text-sm font-bold text-white">${h.title}</span>
                    <button class="del text-rose-400 hover:text-rose-300 text-xs">Remove</button>
                </div>
                <div class="flex gap-2 justify-between">${daysHtml}</div>
            `;

            card.querySelectorAll('button[data-day]').forEach(btn => {
                btn.addEventListener('click', () => {
                    const d = parseInt(btn.dataset.day);
                    h.days[d] = !h.days[d];
                    save();
                });
            });

            card.querySelector('.del').addEventListener('click', () => {
                habits.splice(hIdx, 1);
                save();
            });

            list.appendChild(card);
        });
    }

    document.getElementById('addHabit').addEventListener('click', () => {
        const text = input.value.trim();
        if (!text) return;
        habits.push({ title: text, days: [false, false, false, false, false, false, false] });
        input.value = '';
        save();
    });

    render();
    