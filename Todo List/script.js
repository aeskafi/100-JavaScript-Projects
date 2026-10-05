
    let todos = JSON.parse(localStorage.getItem('micro_todos') || '[]');
    const form = document.getElementById('todoForm');
    const input = document.getElementById('todoInput');
    const list = document.getElementById('todoList');

    function save() {
        localStorage.setItem('micro_todos', JSON.stringify(todos));
        render();
    }

    function render() {
        list.innerHTML = '';
        if (todos.length === 0) {
            list.innerHTML = '<li class="text-xs text-slate-500 text-center py-4">No tasks yet. Enjoy your day!</li>';
            return;
        }
        todos.forEach((item, index) => {
            const li = document.createElement('li');
            li.className = 'flex items-center justify-between bg-slate-900 border border-slate-700 p-3 rounded-xl';
            li.innerHTML = `
                <span class="text-sm cursor-pointer select-none ${item.done ? 'line-through text-slate-500' : 'text-slate-200'}">${item.text}</span>
                <button class="text-rose-400 hover:text-rose-300 text-xs px-2 py-1 rounded bg-slate-800 transition">✕</button>
            `;
            li.querySelector('span').addEventListener('click', () => {
                todos[index].done = !todos[index].done;
                save();
            });
            li.querySelector('button').addEventListener('click', () => {
                todos.splice(index, 1);
                save();
            });
            list.appendChild(li);
        });
    }

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const text = input.value.trim();
        if (!text) return;
        todos.push({ text, done: false });
        input.value = '';
        save();
    });

    render();
    