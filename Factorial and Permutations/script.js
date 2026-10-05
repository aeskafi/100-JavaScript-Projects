
    const nEl = document.getElementById('nVal');
    const rEl = document.getElementById('rVal');
    const factRes = document.getElementById('factRes');
    const permRes = document.getElementById('permRes');
    const combRes = document.getElementById('combRes');

    function fact(num) {
        if (num <= 1) return 1;
        let res = 1;
        for (let i = 2; i <= num; i++) res *= i;
        return res;
    }

    function calculate() {
        const n = Math.min(25, Math.max(0, parseInt(nEl.value) || 0));
        const r = Math.min(n, Math.max(0, parseInt(rEl.value) || 0));

        const nf = fact(n);
        const rf = fact(r);
        const nrf = fact(n - r);

        factRes.innerText = nf.toLocaleString();
        permRes.innerText = (nf / nrf).toLocaleString();
        combRes.innerText = (nf / (rf * nrf)).toLocaleString();
    }

    nEl.addEventListener('input', calculate);
    rEl.addEventListener('input', calculate);
    calculate();
    