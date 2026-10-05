
    const amount = document.getElementById('amount');
    const rate = document.getElementById('rate');
    const years = document.getElementById('years');
    const monthly = document.getElementById('monthly');
    const totalInterest = document.getElementById('totalInterest');

    function calculate() {
        const p = parseFloat(amount.value) || 0;
        const r = (parseFloat(rate.value) || 0) / 100 / 12;
        const n = (parseFloat(years.value) || 0) * 12;

        if (p <= 0 || r <= 0 || n <= 0) {
            monthly.innerText = '$0.00';
            totalInterest.innerText = '$0.00';
            return;
        }

        const m = (p * r * Math.pow(1 + r, n)) / (Math.pow(1 + r, n) - 1);
        const total = m * n;
        monthly.innerText = '$' + m.toFixed(2);
        totalInterest.innerText = '$' + (total - p).toFixed(2);
    }
    [amount, rate, years].forEach(el => el.addEventListener('input', calculate));
    calculate();
    