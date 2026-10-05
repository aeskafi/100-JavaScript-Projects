
    const input = document.getElementById('palInput');
    const status = document.getElementById('palStatus');
    const cleanEl = document.getElementById('palClean');

    function check() {
        const raw = input.value;
        const clean = raw.toLowerCase().replace(/[^a-z0-9]/g, '');
        const reversed = clean.split('').reverse().join('');
        cleanEl.innerText = `Normalized: ${clean}`;
        if (!clean) {
            status.innerText = 'Type something';
            status.className = 'text-2xl font-bold text-slate-400';
            return;
        }
        if (clean === reversed) {
            status.innerText = "Yes! It's a Palindrome! 🎉";
            status.className = 'text-2xl font-bold text-emerald-400';
        } else {
            status.innerText = 'Nope, not a palindrome.';
            status.className = 'text-2xl font-bold text-rose-400';
        }
    }

    input.addEventListener('input', check);
    check();
    