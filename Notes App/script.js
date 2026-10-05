
    let notes = JSON.parse(localStorage.getItem('micro_notes') || '[]');
    const title = document.getElementById('noteTitle');
    const content = document.getElementById('noteContent');
    const container = document.getElementById('notesContainer');

    function render() {
        container.innerHTML = '';
        if (notes.length === 0) {
            container.innerHTML = '<div class="text-xs text-slate-500 text-center py-4">No saved notes. Create your first note above!</div>';
            return;
        }
        notes.forEach((n, idx) => {
            const card = document.createElement('div');
            card.className = 'bg-slate-900 border border-slate-700 p-3 rounded-xl flex justify-between items-start';
            card.innerHTML = `
                <div>
                    <h4 class="text-sm font-bold text-cyan-400">${n.title || 'Untitled'}</h4>
                    <p class="text-xs text-slate-300 mt-1 whitespace-pre-wrap">${n.content}</p>
                </div>
                <button class="text-rose-400 hover:text-rose-300 text-xs px-2 py-1 bg-slate-800 rounded">✕</button>
            `;
            card.querySelector('button').addEventListener('click', () => {
                notes.splice(idx, 1);
                localStorage.setItem('micro_notes', JSON.stringify(notes));
                render();
            });
            container.appendChild(card);
        });
    }

    document.getElementById('saveNote').addEventListener('click', () => {
        if (!content.value.trim()) return;
        notes.unshift({ title: title.value.trim(), content: content.value.trim() });
        localStorage.setItem('micro_notes', JSON.stringify(notes));
        title.value = '';
        content.value = '';
        render();
    });

    render();
    