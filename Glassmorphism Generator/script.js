
    const target = document.getElementById('glassTarget');
    const blur = document.getElementById('glassBlur');
    const op = document.getElementById('glassOp');
    const css = document.getElementById('glassCss');

    function update() {
        document.getElementById('glassBlurVal').innerText = blur.value;
        document.getElementById('glassOpVal').innerText = op.value;

        target.style.background = `rgba(255, 255, 255, ${op.value})`;
        target.style.backdropFilter = `blur(${blur.value}px)`;

        css.value = `background: rgba(255, 255, 255, ${op.value});\nbackdrop-filter: blur(${blur.value}px);\n-webkit-backdrop-filter: blur(${blur.value}px);\nborder: 1px solid rgba(255, 255, 255, 0.2);`;
    }

    [blur, op].forEach(el => el.addEventListener('input', update));
    update();
    