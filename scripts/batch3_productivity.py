import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def create_project(folder_name, title, category, icon, description, html_body, js_code):
    dir_path = os.path.join(BASE_DIR, folder_name)
    os.makedirs(dir_path, exist_ok=True)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | 100 JavaScript Projects</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="min-h-screen bg-slate-900 text-slate-100 flex flex-col justify-center items-center p-4 font-sans">
    <div class="w-full max-w-xl bg-slate-800 border border-slate-700 rounded-3xl shadow-2xl p-6 sm:p-8 backdrop-blur-md">
        <a href="../index.html" class="inline-flex items-center text-xs font-semibold text-cyan-400 hover:text-cyan-300 mb-6 transition-colors">
            ← Back to All Projects
        </a>
        <div class="flex items-center justify-between mb-2">
            <h1 class="text-2xl sm:text-3xl font-bold text-white flex items-center gap-2">
                <span>{icon}</span> {title}
            </h1>
            <span class="text-xs font-semibold px-2.5 py-1 rounded-full bg-slate-700 text-cyan-400 border border-slate-600">
                {category}
            </span>
        </div>
        <p class="text-sm text-slate-400 mb-6">{description}</p>
        {html_body}
    </div>
    <script src="script.js"></script>
</body>
</html>"""
    with open(os.path.join(dir_path, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)
    with open(os.path.join(dir_path, 'script.js'), 'w', encoding='utf-8') as f:
        f.write(js_code)
    print(f"Created {folder_name}")

# 32. Todo List
create_project(
    "Todo List",
    "Minimalist Todo List",
    "Productivity",
    "✅",
    "Track tasks with local storage persistence, filtering, and strike-through completion.",
    """
    <div class="space-y-4">
        <form id="todoForm" class="flex gap-2">
            <input type="text" id="todoInput" placeholder="Add a new task..." class="flex-1 bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:ring-2 focus:ring-cyan-500 outline-none" />
            <button type="submit" class="px-5 py-2.5 bg-cyan-600 hover:bg-cyan-500 text-white font-bold rounded-xl text-sm transition">Add</button>
        </form>
        <ul id="todoList" class="space-y-2 max-h-64 overflow-y-auto pr-1"></ul>
    </div>
    """,
    """
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
    """
)

# 33. Pomodoro Timer
create_project(
    "Pomodoro Timer",
    "Focus Pomodoro Timer",
    "Productivity",
    "🍅",
    "Stay in the zone with 25-minute focus intervals and 5-minute restorative breaks.",
    """
    <div class="space-y-6 text-center">
        <div class="flex justify-center gap-2">
            <button id="modeWork" class="px-4 py-1.5 rounded-xl bg-cyan-600 text-xs font-bold text-white transition">Work (25m)</button>
            <button id="modeBreak" class="px-4 py-1.5 rounded-xl bg-slate-700 text-xs font-bold text-slate-300 transition">Short Break (5m)</button>
        </div>
        <div id="pomoTime" class="text-6xl font-black text-cyan-400 font-mono tracking-wider">25:00</div>
        <div class="flex justify-center gap-3">
            <button id="pomoStart" class="px-6 py-2.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl text-sm transition">Start</button>
            <button id="pomoReset" class="px-6 py-2.5 bg-slate-700 hover:bg-slate-600 text-slate-300 font-bold rounded-xl text-sm transition">Reset</button>
        </div>
    </div>
    """,
    """
    let duration = 25 * 60;
    let remaining = duration;
    let timer = null;
    let isRunning = false;

    const display = document.getElementById('pomoTime');
    const startBtn = document.getElementById('pomoStart');
    const resetBtn = document.getElementById('pomoReset');
    const modeWork = document.getElementById('modeWork');
    const modeBreak = document.getElementById('modeBreak');

    function update() {
        const m = Math.floor(remaining / 60);
        const s = remaining % 60;
        display.innerText = `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
    }

    startBtn.addEventListener('click', () => {
        if (isRunning) {
            clearInterval(timer);
            startBtn.innerText = 'Start';
            startBtn.className = 'px-6 py-2.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl text-sm transition';
            isRunning = false;
        } else {
            isRunning = true;
            startBtn.innerText = 'Pause';
            startBtn.className = 'px-6 py-2.5 bg-amber-600 hover:bg-amber-500 text-white font-bold rounded-xl text-sm transition';
            timer = setInterval(() => {
                if (remaining > 0) {
                    remaining--;
                    update();
                } else {
                    clearInterval(timer);
                    isRunning = false;
                    startBtn.innerText = 'Done!';
                }
            }, 1000);
        }
    });

    resetBtn.addEventListener('click', () => {
        clearInterval(timer);
        isRunning = false;
        startBtn.innerText = 'Start';
        startBtn.className = 'px-6 py-2.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl text-sm transition';
        remaining = duration;
        update();
    });

    modeWork.addEventListener('click', () => {
        duration = 25 * 60;
        remaining = duration;
        modeWork.className = 'px-4 py-1.5 rounded-xl bg-cyan-600 text-xs font-bold text-white transition';
        modeBreak.className = 'px-4 py-1.5 rounded-xl bg-slate-700 text-xs font-bold text-slate-300 transition';
        resetBtn.click();
    });

    modeBreak.addEventListener('click', () => {
        duration = 5 * 60;
        remaining = duration;
        modeBreak.className = 'px-4 py-1.5 rounded-xl bg-cyan-600 text-xs font-bold text-white transition';
        modeWork.className = 'px-4 py-1.5 rounded-xl bg-slate-700 text-xs font-bold text-slate-300 transition';
        resetBtn.click();
    });

    update();
    """
)

# 34. Stopwatch
create_project(
    "Stopwatch",
    "High-Precision Stopwatch",
    "Productivity",
    "⏱️",
    "Millisecond-accurate stopwatch with lap recording and clean time split log.",
    """
    <div class="space-y-5 text-center">
        <div id="swDisplay" class="text-5xl sm:text-6xl font-black text-cyan-400 font-mono tracking-wider">00:00:00.00</div>
        <div class="flex justify-center gap-3">
            <button id="swStart" class="px-6 py-2.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl text-sm transition">Start</button>
            <button id="swLap" class="px-6 py-2.5 bg-cyan-600 hover:bg-cyan-500 text-white font-bold rounded-xl text-sm transition">Lap</button>
            <button id="swReset" class="px-6 py-2.5 bg-slate-700 hover:bg-slate-600 text-slate-300 font-bold rounded-xl text-sm transition">Reset</button>
        </div>
        <div id="swLaps" class="max-h-40 overflow-y-auto bg-slate-950 border border-slate-700 rounded-2xl p-3 text-xs font-mono text-slate-300 space-y-1"></div>
    </div>
    """,
    """
    let startTime = 0;
    let elapsed = 0;
    let timer = null;
    let running = false;
    let lapCount = 0;

    const display = document.getElementById('swDisplay');
    const startBtn = document.getElementById('swStart');
    const lapBtn = document.getElementById('swLap');
    const resetBtn = document.getElementById('swReset');
    const laps = document.getElementById('swLaps');

    function formatTime(ms) {
        const totalSec = Math.floor(ms / 1000);
        const hours = Math.floor(totalSec / 3600);
        const minutes = Math.floor((totalSec % 3600) / 60);
        const seconds = totalSec % 60;
        const centis = Math.floor((ms % 1000) / 10);
        return `${String(hours).padStart(2,'0')}:${String(minutes).padStart(2,'0')}:${String(seconds).padStart(2,'0')}.${String(centis).padStart(2,'0')}`;
    }

    startBtn.addEventListener('click', () => {
        if (!running) {
            running = true;
            startTime = Date.now() - elapsed;
            timer = setInterval(() => {
                elapsed = Date.now() - startTime;
                display.innerText = formatTime(elapsed);
            }, 10);
            startBtn.innerText = 'Pause';
            startBtn.className = 'px-6 py-2.5 bg-amber-600 hover:bg-amber-500 text-white font-bold rounded-xl text-sm transition';
        } else {
            running = false;
            clearInterval(timer);
            startBtn.innerText = 'Resume';
            startBtn.className = 'px-6 py-2.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl text-sm transition';
        }
    });

    lapBtn.addEventListener('click', () => {
        if (!running) return;
        lapCount++;
        const div = document.createElement('div');
        div.className = 'flex justify-between py-1 border-b border-slate-800';
        div.innerHTML = `<span class="text-cyan-400">Lap #${lapCount}</span><span>${formatTime(elapsed)}</span>`;
        laps.prepend(div);
    });

    resetBtn.addEventListener('click', () => {
        running = false;
        clearInterval(timer);
        elapsed = 0;
        lapCount = 0;
        display.innerText = '00:00:00.00';
        startBtn.innerText = 'Start';
        startBtn.className = 'px-6 py-2.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl text-sm transition';
        laps.innerHTML = '';
    });
    """
)

# 35. Digital and Analog Clock
create_project(
    "Digital and Analog Clock",
    "Digital & Analog World Clock",
    "Productivity",
    "🕒",
    "Live ticking digital display with date, timezone offset, and 12/24 hour toggle.",
    """
    <div class="space-y-6 text-center">
        <div class="bg-slate-900 border border-slate-700 rounded-2xl p-6 max-w-sm mx-auto shadow-inner">
            <div id="clockTime" class="text-5xl font-black text-cyan-400 font-mono tracking-wider">00:00:00</div>
            <div id="clockPeriod" class="text-sm font-bold text-amber-400 font-mono mt-1">PM</div>
            <div id="clockDate" class="text-sm text-slate-400 mt-3">Loading date...</div>
        </div>
        <button id="clockToggle" class="px-4 py-2 bg-slate-700 hover:bg-slate-600 text-white rounded-xl text-xs font-bold transition">
            Switch to 24-Hour Format
        </button>
    </div>
    """,
    """
    let is24Hour = false;
    const timeEl = document.getElementById('clockTime');
    const periodEl = document.getElementById('clockPeriod');
    const dateEl = document.getElementById('clockDate');
    const toggleBtn = document.getElementById('clockToggle');

    function update() {
        const now = new Date();
        let h = now.getHours();
        const m = String(now.getMinutes()).padStart(2, '0');
        const s = String(now.getSeconds()).padStart(2, '0');

        if (is24Hour) {
            timeEl.innerText = `${String(h).padStart(2, '0')}:${m}:${s}`;
            periodEl.style.display = 'none';
        } else {
            const period = h >= 12 ? 'PM' : 'AM';
            h = h % 12 || 12;
            timeEl.innerText = `${String(h).padStart(2, '0')}:${m}:${s}`;
            periodEl.innerText = period;
            periodEl.style.display = 'block';
        }

        dateEl.innerText = now.toLocaleDateString(undefined, {
            weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'
        });
    }

    toggleBtn.addEventListener('click', () => {
        is24Hour = !is24Hour;
        toggleBtn.innerText = is24Hour ? 'Switch to 12-Hour Format' : 'Switch to 24-Hour Format';
        update();
    });

    setInterval(update, 1000);
    update();
    """
)

# 36. Notes App
create_project(
    "Notes App",
    "Quick Notes Pad",
    "Productivity",
    "📓",
    "Auto-saving scratchpad with search, note deletion, and local storage retention.",
    """
    <div class="space-y-4">
        <div class="flex gap-2">
            <input type="text" id="noteTitle" placeholder="Note Title..." class="flex-1 bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-sm text-white outline-none" />
            <button id="saveNote" class="px-4 py-2 bg-cyan-600 hover:bg-cyan-500 text-white font-bold rounded-xl text-xs transition">Save Note</button>
        </div>
        <textarea id="noteContent" rows="4" placeholder="Write thoughts, ideas, or meeting notes..." class="w-full bg-slate-950 border border-slate-700 rounded-xl p-3 text-sm text-slate-100 outline-none resize-none"></textarea>
        <div id="notesContainer" class="space-y-2 max-h-56 overflow-y-auto"></div>
    </div>
    """,
    """
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
    """
)

# 37. Kanban Board
create_project(
    "Kanban Board",
    "Micro Kanban Board",
    "Productivity",
    "📋",
    "Agile workflow board with To Do, In Progress, and Done stages.",
    """
    <div class="space-y-4">
        <div class="flex gap-2">
            <input type="text" id="kanbanInput" placeholder="Add new task card..." class="flex-1 bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-sm text-white outline-none" />
            <button id="addKanban" class="px-4 py-2 bg-cyan-600 hover:bg-cyan-500 text-white font-bold rounded-xl text-xs transition">Add Card</button>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div class="bg-slate-950 border border-slate-700 rounded-2xl p-3">
                <h4 class="text-xs font-bold text-amber-400 mb-2 uppercase tracking-wider">To Do</h4>
                <div id="colTodo" class="space-y-2 min-h-32"></div>
            </div>
            <div class="bg-slate-950 border border-slate-700 rounded-2xl p-3">
                <h4 class="text-xs font-bold text-cyan-400 mb-2 uppercase tracking-wider">In Progress</h4>
                <div id="colProg" class="space-y-2 min-h-32"></div>
            </div>
            <div class="bg-slate-950 border border-slate-700 rounded-2xl p-3">
                <h4 class="text-xs font-bold text-emerald-400 mb-2 uppercase tracking-wider">Done</h4>
                <div id="colDone" class="space-y-2 min-h-32"></div>
            </div>
        </div>
    </div>
    """,
    """
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
    """
)

# 38. Habit Tracker
create_project(
    "Habit Tracker",
    "7-Day Habit Tracker",
    "Productivity",
    "🌱",
    "Cultivate daily routines with visual 7-day checkboxes and completion streaks.",
    """
    <div class="space-y-4">
        <div class="flex gap-2">
            <input type="text" id="habitInput" placeholder="New habit (e.g. Read 20 mins, Workout)..." class="flex-1 bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-sm text-white outline-none" />
            <button id="addHabit" class="px-4 py-2 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl text-xs transition">Add Habit</button>
        </div>
        <div id="habitList" class="space-y-3"></div>
    </div>
    """,
    """
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
    """
)

# 39. Expense Tracker
create_project(
    "Expense Tracker",
    "Personal Expense Tracker",
    "Finance",
    "💳",
    "Record income, outgoing expenses, and view live net cash balance.",
    """
    <div class="space-y-4">
        <div class="grid grid-cols-2 gap-3">
            <div class="bg-slate-900 p-4 rounded-2xl border border-slate-700 text-center">
                <span class="text-xs text-slate-400">Total Balance</span>
                <p id="netBalance" class="text-2xl font-bold text-cyan-400 font-mono mt-1">$0.00</p>
            </div>
            <div class="bg-slate-900 p-4 rounded-2xl border border-slate-700 text-center">
                <span class="text-xs text-slate-400">Expenses</span>
                <p id="totalExp" class="text-2xl font-bold text-rose-400 font-mono mt-1">$0.00</p>
            </div>
        </div>
        <div class="flex gap-2">
            <input type="text" id="expDesc" placeholder="Description (e.g. Groceries)" class="flex-1 bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-xs text-white outline-none" />
            <input type="number" id="expAmt" placeholder="Amount (+/-)" class="w-28 bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-xs text-white outline-none" />
            <button id="addExp" class="px-4 py-2 bg-cyan-600 hover:bg-cyan-500 text-white font-bold rounded-xl text-xs transition">Add</button>
        </div>
        <div id="expList" class="space-y-1.5 max-h-48 overflow-y-auto"></div>
    </div>
    """,
    """
    let txs = JSON.parse(localStorage.getItem('micro_expenses') || '[]');
    const desc = document.getElementById('expDesc');
    const amt = document.getElementById('expAmt');
    const list = document.getElementById('expList');
    const netBal = document.getElementById('netBalance');
    const totExp = document.getElementById('totalExp');

    function save() {
        localStorage.setItem('micro_expenses', JSON.stringify(txs));
        render();
    }

    function render() {
        list.innerHTML = '';
        let balance = 0;
        let expenses = 0;

        txs.forEach((t, i) => {
            balance += t.amount;
            if (t.amount < 0) expenses += Math.abs(t.amount);

            const div = document.createElement('div');
            div.className = 'flex justify-between items-center bg-slate-900 p-2.5 rounded-xl border border-slate-800 text-xs';
            div.innerHTML = `
                <span class="text-slate-200">${t.desc}</span>
                <div class="flex items-center gap-2">
                    <span class="font-mono font-bold ${t.amount >= 0 ? 'text-emerald-400' : 'text-rose-400'}">${t.amount >= 0 ? '+' : ''}$${t.amount.toFixed(2)}</span>
                    <button class="text-slate-500 hover:text-rose-400">✕</button>
                </div>
            `;
            div.querySelector('button').addEventListener('click', () => { txs.splice(i, 1); save(); });
            list.appendChild(div);
        });

        netBal.innerText = '$' + balance.toFixed(2);
        totExp.innerText = '$' + expenses.toFixed(2);
    }

    document.getElementById('addExp').addEventListener('click', () => {
        const d = desc.value.trim();
        const a = parseFloat(amt.value);
        if (!d || isNaN(a)) return;
        txs.unshift({ desc: d, amount: a });
        desc.value = '';
        amt.value = '';
        save();
    });

    render();
    """
)

# 40. Flashcards App
create_project(
    "Flashcards App",
    "Study Flashcards",
    "Education",
    "🎴",
    "Flip-card memory study app with front/back questions and answers.",
    """
    <div class="space-y-5 text-center">
        <div id="cardBox" class="bg-slate-950 border-2 border-cyan-500/40 hover:border-cyan-400 rounded-3xl p-10 cursor-pointer min-h-[160px] flex flex-col justify-center items-center shadow-xl transition-all">
            <span id="cardSide" class="text-xs font-bold text-cyan-400 uppercase tracking-widest mb-2">Question</span>
            <div id="cardText" class="text-xl font-bold text-white">What does DOM stand for?</div>
        </div>
        <div class="flex justify-center gap-3">
            <button id="fcPrev" class="px-5 py-2 bg-slate-700 hover:bg-slate-600 rounded-xl text-xs font-bold text-white transition">← Prev</button>
            <button id="fcFlip" class="px-6 py-2 bg-cyan-600 hover:bg-cyan-500 rounded-xl text-xs font-bold text-white transition">Flip Card</button>
            <button id="fcNext" class="px-5 py-2 bg-slate-700 hover:bg-slate-600 rounded-xl text-xs font-bold text-white transition">Next →</button>
        </div>
    </div>
    """,
    """
    const cards = [
        { q: 'What does DOM stand for?', a: 'Document Object Model' },
        { q: 'What is a closure in JavaScript?', a: 'A function bundled together with references to its surrounding lexical state.' },
        { q: 'What is the purpose of Promise.all()?', a: 'Resolves when all promises resolve, or rejects when any promise rejects.' },
        { q: 'What is Event Bubbling?', a: 'Events start from the deepest target element and bubble up the DOM tree.' }
    ];

    let current = 0;
    let isFlipped = false;

    const box = document.getElementById('cardBox');
    const side = document.getElementById('cardSide');
    const text = document.getElementById('cardText');

    function update() {
        const c = cards[current];
        side.innerText = isFlipped ? 'Answer' : 'Question';
        side.className = isFlipped ? 'text-xs font-bold text-emerald-400 uppercase tracking-widest mb-2' : 'text-xs font-bold text-cyan-400 uppercase tracking-widest mb-2';
        text.innerText = isFlipped ? c.a : c.q;
    }

    box.addEventListener('click', () => { isFlipped = !isFlipped; update(); });
    document.getElementById('fcFlip').addEventListener('click', () => { isFlipped = !isFlipped; update(); });
    document.getElementById('fcNext').addEventListener('click', () => { current = (current + 1) % cards.length; isFlipped = false; update(); });
    document.getElementById('fcPrev').addEventListener('click', () => { current = (current - 1 + cards.length) % cards.length; isFlipped = false; update(); });

    update();
    """
)

# 41. Simple Form Validator
create_project(
    "Simple Form Validator",
    "Live Form Validator",
    "Developer Tools",
    "🛡️",
    "Real-time validation for email formatting, password strength, and field constraints.",
    """
    <form id="valForm" class="space-y-4">
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Username (min 3 chars)</label>
            <input type="text" id="vUser" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-white text-sm outline-none" />
            <p id="vUserErr" class="text-xs text-rose-400 mt-1 hidden"></p>
        </div>
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Email Address</label>
            <input type="email" id="vEmail" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-white text-sm outline-none" />
            <p id="vEmailErr" class="text-xs text-rose-400 mt-1 hidden"></p>
        </div>
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Password (min 8 chars)</label>
            <input type="password" id="vPass" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-white text-sm outline-none" />
            <p id="vPassErr" class="text-xs text-rose-400 mt-1 hidden"></p>
        </div>
        <button type="submit" class="w-full py-3 bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-white font-bold rounded-xl text-sm transition">
            Validate & Submit
        </button>
        <div id="vSuccess" class="p-3 bg-emerald-950/60 border border-emerald-600 rounded-xl text-xs text-emerald-300 text-center hidden">
            Form validated successfully!
        </div>
    </form>
    """,
    """
    const form = document.getElementById('valForm');
    const user = document.getElementById('vUser');
    const email = document.getElementById('vEmail');
    const pass = document.getElementById('vPass');
    const success = document.getElementById('vSuccess');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        let valid = true;

        if (user.value.trim().length < 3) {
            document.getElementById('vUserErr').innerText = 'Username must be at least 3 characters.';
            document.getElementById('vUserErr').classList.remove('hidden');
            valid = false;
        } else {
            document.getElementById('vUserErr').classList.add('hidden');
        }

        const emailRe = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
        if (!emailRe.test(email.value)) {
            document.getElementById('vEmailErr').innerText = 'Please enter a valid email address.';
            document.getElementById('vEmailErr').classList.remove('hidden');
            valid = false;
        } else {
            document.getElementById('vEmailErr').classList.add('hidden');
        }

        if (pass.value.length < 8) {
            document.getElementById('vPassErr').innerText = 'Password must be at least 8 characters.';
            document.getElementById('vPassErr').classList.remove('hidden');
            valid = false;
        } else {
            document.getElementById('vPassErr').classList.add('hidden');
        }

        success.classList.toggle('hidden', !valid);
    });
    """
)

# 42. Bookmark Manager
create_project(
    "Bookmark Manager",
    "Quick Links & Bookmark Vault",
    "Productivity",
    "🔖",
    "Save frequent developer links and docs with favicon preview and one-click launch.",
    """
    <div class="space-y-4">
        <div class="flex gap-2">
            <input type="text" id="bmTitle" placeholder="Title (e.g. Arham Dev)" class="flex-1 bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-xs text-white outline-none" />
            <input type="url" id="bmUrl" placeholder="https://..." class="flex-1 bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-xs text-white outline-none" />
            <button id="addBm" class="px-4 py-2 bg-cyan-600 hover:bg-cyan-500 text-white font-bold rounded-xl text-xs transition">Save</button>
        </div>
        <div id="bmList" class="space-y-2 max-h-56 overflow-y-auto"></div>
    </div>
    """,
    """
    let bms = JSON.parse(localStorage.getItem('micro_bms') || '[{"title":"Arham Dev","url":"https://arham.dev"},{"title":"Walk Cook Live","url":"https://youtube.com/@walkcooklive"}]');
    const title = document.getElementById('bmTitle');
    const url = document.getElementById('bmUrl');
    const list = document.getElementById('bmList');

    function save() {
        localStorage.setItem('micro_bms', JSON.stringify(bms));
        render();
    }

    function render() {
        list.innerHTML = '';
        bms.forEach((b, i) => {
            const div = document.createElement('div');
            div.className = 'flex justify-between items-center bg-slate-900 border border-slate-700 p-2.5 rounded-xl text-xs';
            div.innerHTML = `
                <a href="${b.url}" target="_blank" class="text-cyan-400 hover:underline font-bold flex items-center gap-2">
                    <span>🔗</span> ${b.title}
                </a>
                <button class="text-slate-500 hover:text-rose-400">✕</button>
            `;
            div.querySelector('button').addEventListener('click', () => { bms.splice(i, 1); save(); });
            list.appendChild(div);
        });
    }

    document.getElementById('addBm').addEventListener('click', () => {
        let u = url.value.trim();
        const t = title.value.trim() || u;
        if (!u) return;
        if (!u.startsWith('http')) u = 'https://' + u;
        bms.unshift({ title: t, url: u });
        title.value = '';
        url.value = '';
        save();
    });

    render();
    """
)

# 43. Speed Reading Trainer
create_project(
    "Speed Reading Trainer",
    "RSVP Speed Reading Trainer",
    "Productivity",
    "⚡",
    "Rapid Serial Visual Presentation trainer to increase reading comprehension rate (WPM).",
    """
    <div class="space-y-5 text-center">
        <div class="bg-slate-950 border border-slate-700 rounded-3xl p-10 min-h-[140px] flex items-center justify-center">
            <span id="speedWord" class="text-4xl font-extrabold text-cyan-400 font-mono tracking-wide">Ready</span>
        </div>
        <div class="flex items-center justify-center gap-4 text-xs text-slate-300">
            <span>Speed: <strong id="wpmVal" class="text-cyan-400">300</strong> WPM</span>
            <input type="range" id="wpmRange" min="100" max="800" value="300" step="50" class="accent-cyan-500 cursor-pointer" />
        </div>
        <div class="flex justify-center gap-3">
            <button id="speedStart" class="px-6 py-2.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl text-sm transition">Start Training</button>
            <button id="speedReset" class="px-6 py-2.5 bg-slate-700 hover:bg-slate-600 text-slate-300 font-bold rounded-xl text-sm transition">Reset</button>
        </div>
    </div>
    """,
    """
    const sample = "Rapid serial visual presentation enables readers to absorb text at extreme velocity by eliminating the need for ocular saccades across printed lines. As you practice daily, comprehension and speed scale dramatically!".split(' ');

    let idx = 0;
    let timer = null;
    const wordEl = document.getElementById('speedWord');
    const startBtn = document.getElementById('speedStart');
    const resetBtn = document.getElementById('speedReset');
    const range = document.getElementById('wpmRange');
    const wpmVal = document.getElementById('wpmVal');

    range.addEventListener('input', () => { wpmVal.innerText = range.value; });

    startBtn.addEventListener('click', () => {
        if (timer) {
            clearInterval(timer);
            timer = null;
            startBtn.innerText = 'Resume';
            return;
        }
        startBtn.innerText = 'Pause';
        const delay = (60 / parseInt(range.value)) * 1000;
        timer = setInterval(() => {
            if (idx < sample.length) {
                wordEl.innerText = sample[idx];
                idx++;
            } else {
                clearInterval(timer);
                timer = null;
                startBtn.innerText = 'Restart';
                idx = 0;
            }
        }, delay);
    });

    resetBtn.addEventListener('click', () => {
        clearInterval(timer);
        timer = null;
        idx = 0;
        wordEl.innerText = 'Ready';
        startBtn.innerText = 'Start Training';
    });
    """
)

# 44. Typing Speed Test
create_project(
    "Typing Speed Test",
    "Typing Speed & Accuracy Test",
    "Productivity",
    "⌨️",
    "Test your Words Per Minute (WPM) and accuracy against sample developer sentences.",
    """
    <div class="space-y-4">
        <div id="typePrompt" class="bg-slate-950 border border-slate-700 p-4 rounded-2xl text-sm text-slate-300 font-mono select-none">
            The best code is the code that is never written, but when written, it must be fast.
        </div>
        <textarea id="typeInput" rows="3" placeholder="Start typing the prompt above..." class="w-full bg-slate-950 border border-slate-700 rounded-xl p-3 text-sm text-cyan-400 font-mono outline-none resize-none"></textarea>
        <div class="grid grid-cols-2 gap-3 text-center">
            <div class="bg-slate-900 p-3 rounded-2xl border border-slate-700">
                <span class="text-xs text-slate-400">Speed</span>
                <p id="typeWpm" class="text-2xl font-bold text-cyan-400 font-mono mt-1">0 WPM</p>
            </div>
            <div class="bg-slate-900 p-3 rounded-2xl border border-slate-700">
                <span class="text-xs text-slate-400">Accuracy</span>
                <p id="typeAcc" class="text-2xl font-bold text-emerald-400 font-mono mt-1">100%</p>
            </div>
        </div>
    </div>
    """,
    """
    const prompt = document.getElementById('typePrompt');
    const input = document.getElementById('typeInput');
    const wpmEl = document.getElementById('typeWpm');
    const accEl = document.getElementById('typeAcc');

    let startTime = null;

    input.addEventListener('input', () => {
        if (!startTime) startTime = Date.now();
        const pText = prompt.innerText.trim();
        const iText = input.value;

        const timeElapsed = (Date.now() - startTime) / 1000 / 60; // minutes
        const words = iText.trim().split(/\\s+/).filter(x => x.length > 0).length;
        const wpm = Math.round(words / (timeElapsed || 0.01));
        wpmEl.innerText = `${wpm} WPM`;

        let correct = 0;
        for (let i = 0; i < iText.length; i++) {
            if (iText[i] === pText[i]) correct++;
        }
        const acc = iText.length ? Math.round((correct / iText.length) * 100) : 100;
        accEl.innerText = `${acc}%`;
    });
    """
)

# 45. Daily Affirmation Generator
create_project(
    "Daily Affirmation Generator",
    "Daily Developer Affirmations",
    "Mindset",
    "✨",
    "Inspirational mindset boosters and affirmations for builders and nomad makers.",
    """
    <div class="space-y-6 text-center">
        <div class="bg-slate-950 border border-slate-700 rounded-3xl p-8 min-h-[140px] flex items-center justify-center shadow-inner">
            <p id="affText" class="text-xl font-bold text-cyan-400 italic">"I build fast, test rigorously, and deliver real value to the world."</p>
        </div>
        <button id="nextAff" class="px-6 py-3 bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-white font-bold rounded-xl text-sm transition active:scale-95 shadow-lg">
            ✨ Get Next Affirmation
        </button>
    </div>
    """,
    """
    const affirmations = [
        "I build fast, test rigorously, and deliver real value to the world.",
        "Every bug is simply an invitation to understand the system more deeply.",
        "Freedom and discipline go hand in hand on the nomad engineering journey.",
        "Simplicity is the prerequisite for reliability and speed.",
        "My potential as a creator expands every time I solve a hard challenge."
    ];

    const text = document.getElementById('affText');
    const btn = document.getElementById('nextAff');

    btn.addEventListener('click', () => {
        const quote = affirmations[Math.floor(Math.random() * affirmations.length)];
        text.innerText = `"${quote}"`;
    });
    """
)
