
    const target = document.getElementById('shadowTarget');
    const x = document.getElementById('xOff');
    const y = document.getElementById('yOff');
    const b = document.getElementById('blur');
    const s = document.getElementById('spread');
    const css = document.getElementById('shadowCss');

    function update() {
        document.getElementById('xVal').innerText = x.value;
        document.getElementById('yVal').innerText = y.value;
        document.getElementById('bVal').innerText = b.value;
        document.getElementById('sVal').innerText = s.value;

        const val = `${x.value}px ${y.value}px ${b.value}px ${s.value}px rgba(6, 182, 212, 0.35)`;
        target.style.boxShadow = val;
        css.value = `box-shadow: ${val};`;
    }

    [x, y, b, s].forEach(el => el.addEventListener('input', update));
    update();
    