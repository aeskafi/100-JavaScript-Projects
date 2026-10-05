
    function gcd(a, b) {
        return b === 0 ? a : gcd(b, a % b);
    }

    const w = document.getElementById('arW');
    const h = document.getElementById('arH');
    const res = document.getElementById('arResult');

    function calculate() {
        const width = parseInt(w.value) || 0;
        const height = parseInt(h.value) || 0;
        if (width <= 0 || height <= 0) { res.innerText = '--:--'; return; }
        const divisor = gcd(width, height);
        res.innerText = `${width / divisor}:${height / divisor}`;
    }

    w.addEventListener('input', calculate);
    h.addEventListener('input', calculate);
    calculate();
    