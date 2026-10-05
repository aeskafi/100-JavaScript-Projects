
    const target = document.getElementById('blobTarget');
    const tl = document.getElementById('tl');
    const tr = document.getElementById('tr');
    const bl = document.getElementById('bl');
    const br = document.getElementById('br');
    const css = document.getElementById('blobCss');

    function update() {
        document.getElementById('tlVal').innerText = tl.value;
        document.getElementById('trVal').innerText = tr.value;
        document.getElementById('blVal').innerText = bl.value;
        document.getElementById('brVal').innerText = br.value;

        const val = `${tl.value}% ${tr.value}% ${br.value}% ${bl.value}% / ${br.value}% ${bl.value}% ${tr.value}% ${tl.value}%`;
        target.style.borderRadius = val;
        css.value = `border-radius: ${val};`;
    }

    [tl, tr, bl, br].forEach(el => el.addEventListener('input', update));
    update();
    