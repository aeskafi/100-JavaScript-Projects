
    const inputs = ['m00', 'm01', 'm10', 'm11'].map(id => document.getElementById(id));
    const detResult = document.getElementById('detResult');
    const detFormula = document.getElementById('detFormula');

    function calcDet() {
        const [a, b, c, d] = inputs.map(el => parseFloat(el.value) || 0);
        const det = (a * d) - (b * c);
        detResult.innerText = det;
        detFormula.innerText = `(${a} × ${d}) - (${b} × ${c}) = ${det}`;
    }

    inputs.forEach(el => el.addEventListener('input', calcDet));
    calcDet();
    