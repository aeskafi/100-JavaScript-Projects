
    const origPrice = document.getElementById('origPrice');
    const discPct = document.getElementById('discPct');
    const finalPrice = document.getElementById('finalPrice');
    const savings = document.getElementById('savings');

    function calculate() {
        const price = parseFloat(origPrice.value) || 0;
        const pct = parseFloat(discPct.value) || 0;
        const saved = (price * pct) / 100;
        const final = price - saved;
        savings.innerText = '$' + saved.toFixed(2);
        finalPrice.innerText = '$' + Math.max(0, final).toFixed(2);
    }
    origPrice.addEventListener('input', calculate);
    discPct.addEventListener('input', calculate);
    calculate();
    