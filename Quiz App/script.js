
    const questions = [
        {
            q: 'Which operator checks for both value and type equality in JavaScript?',
            opts: ['==', '===', '=', '!='],
            ans: 1
        },
        {
            q: 'Which array method returns a brand new array with transformed elements?',
            opts: ['forEach()', 'filter()', 'map()', 'reduce()'],
            ans: 2
        },
        {
            q: 'What is the default value of an uninitialized variable in JS?',
            opts: ['null', '0', 'undefined', 'false'],
            ans: 2
        }
    ];

    let current = 0;
    let score = 0;

    const qEl = document.getElementById('quizQuestion');
    const optsEl = document.getElementById('quizOptions');
    const scoreEl = document.getElementById('quizScore');

    function render() {
        if (current >= questions.length) {
            qEl.innerText = `Quiz Complete! You scored ${score} / ${questions.length} 🎉`;
            optsEl.innerHTML = '<button onclick="location.reload()" class="w-full py-2.5 bg-cyan-600 rounded-xl text-xs font-bold text-white">Restart Quiz</button>';
            scoreEl.innerText = '';
            return;
        }

        const item = questions[current];
        qEl.innerText = item.q;
        optsEl.innerHTML = item.opts.map((opt, i) => `
            <button class="w-full text-left p-3 rounded-xl bg-slate-950 border border-slate-700 hover:border-cyan-400 text-xs font-medium text-slate-200 transition" data-idx="${i}">
                ${opt}
            </button>
        `).join('');

        optsEl.querySelectorAll('button').forEach(btn => {
            btn.addEventListener('click', () => {
                const chosen = parseInt(btn.dataset.idx);
                if (chosen === item.ans) score++;
                current++;
                render();
            });
        });

        scoreEl.innerText = `Question ${current + 1} of ${questions.length}`;
    }

    render();
    