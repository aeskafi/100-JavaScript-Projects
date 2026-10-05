
    const aEl = document.getElementById('quadA');
    const bEl = document.getElementById('quadB');
    const cEl = document.getElementById('quadC');
    const rootsEl = document.getElementById('quadRoots');
    const discEl = document.getElementById('quadDisc');

    function solve() {
        const a = parseFloat(aEl.value) || 0;
        const b = parseFloat(bEl.value) || 0;
        const c = parseFloat(cEl.value) || 0;

        if (a === 0) {
            rootsEl.innerText = 'Linear equation: x = ' + (-c / b).toFixed(2);
            discEl.innerText = '';
            return;
        }

        const delta = b * b - 4 * a * c;
        discEl.innerText = `Discriminant Δ = ${delta}`;

        if (delta > 0) {
            const x1 = (-b + Math.sqrt(delta)) / (2 * a);
            const x2 = (-b - Math.sqrt(delta)) / (2 * a);
            rootsEl.innerText = `x₁ = ${x1.toFixed(2)}, x₂ = ${x2.toFixed(2)}`;
        } else if (delta === 0) {
            const x = -b / (2 * a);
            rootsEl.innerText = `Single Root: x = ${x.toFixed(2)}`;
        } else {
            const real = (-b / (2 * a)).toFixed(2);
            const imag = (Math.sqrt(-delta) / (2 * a)).toFixed(2);
            rootsEl.innerText = `Complex: ${real} ± ${imag}i`;
        }
    }

    [aEl, bEl, cEl].forEach(el => el.addEventListener('input', solve));
    solve();
    