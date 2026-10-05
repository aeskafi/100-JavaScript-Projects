
    const target = document.getElementById('neuTarget');
    const dist = document.getElementById('neuDist');
    const blur = document.getElementById('neuBlur');

    function update() {
        document.getElementById('neuDistVal').innerText = dist.value;
        document.getElementById('neuBlurVal').innerText = blur.value;
        const d = dist.value;
        const b = blur.value;
        target.style.background = '#1e293b';
        target.style.boxShadow = `${d}px ${d}px ${b}px #121927, -${d}px -${d}px ${b}px #2a394f`;
    }

    [dist, blur].forEach(el => el.addEventListener('input', update));
    update();
    