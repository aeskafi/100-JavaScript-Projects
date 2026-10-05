
    const target = document.getElementById('animTarget');

    document.querySelectorAll('.anim-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            target.className = 'w-16 h-16 bg-gradient-to-tr from-cyan-400 to-blue-600 rounded-2xl shadow-xl flex items-center justify-center font-bold text-white';
            const mode = btn.dataset.anim;
            if (mode === 'spin') target.classList.add('animate-spin');
            if (mode === 'bounce') target.classList.add('animate-bounce');
            if (mode === 'pulse') target.classList.add('animate-pulse');
        });
    });
    