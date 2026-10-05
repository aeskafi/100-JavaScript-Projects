
    const preview = document.getElementById('gradPreview');
    const c1 = document.getElementById('gradC1');
    const c2 = document.getElementById('gradC2');
    const angle = document.getElementById('gradAngle');
    const angVal = document.getElementById('angVal');
    const css = document.getElementById('gradCss');

    function update() {
        angVal.innerText = angle.value;
        const code = `linear-gradient(${angle.value}deg, ${c1.value}, ${c2.value})`;
        preview.style.background = code;
        css.value = `background: ${code};`;
    }

    [c1, c2, angle].forEach(el => el.addEventListener('input', update));
    update();
    