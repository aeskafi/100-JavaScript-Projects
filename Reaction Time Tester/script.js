
    const box = document.getElementById('rxBox');
    const text = document.getElementById('rxText');
    const score = document.getElementById('rxScore');

    let state = 'idle'; // idle, waiting, ready
    let startTime = 0;
    let timeout = null;

    box.addEventListener('click', () => {
        if (state === 'idle') {
            state = 'waiting';
            box.className = 'bg-rose-600 rounded-3xl p-12 min-h-[160px] flex flex-col justify-center items-center cursor-pointer shadow-xl';
            text.innerText = 'Wait for green...';
            score.innerText = '';

            timeout = setTimeout(() => {
                state = 'ready';
                box.className = 'bg-emerald-500 rounded-3xl p-12 min-h-[160px] flex flex-col justify-center items-center cursor-pointer shadow-xl';
                text.innerText = 'CLICK NOW!';
                startTime = Date.now();
            }, Math.random() * 2500 + 1500);
        } else if (state === 'waiting') {
            clearTimeout(timeout);
            state = 'idle';
            box.className = 'bg-slate-700 rounded-3xl p-12 min-h-[160px] flex flex-col justify-center items-center cursor-pointer shadow-xl';
            text.innerText = 'Too early! Click to retry.';
        } else if (state === 'ready') {
            const diff = Date.now() - startTime;
            state = 'idle';
            box.className = 'bg-slate-800 rounded-3xl p-12 min-h-[160px] flex flex-col justify-center items-center cursor-pointer shadow-xl border border-slate-700';
            text.innerText = 'Click to try again';
            score.innerText = `Reaction Time: ${diff} ms! ⚡`;
        }
    });
    