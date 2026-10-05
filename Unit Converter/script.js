
    const toMeters = {
        m: 1,
        km: 1000,
        mi: 1609.344,
        ft: 0.3048,
        in: 0.0254,
        cm: 0.01
    };

    const valEl = document.getElementById('unitVal');
    const fromEl = document.getElementById('unitFrom');
    const toEl = document.getElementById('unitTo');
    const resultEl = document.getElementById('unitResult');

    function convert() {
        const val = parseFloat(valEl.value) || 0;
        const meters = val * toMeters[fromEl.value];
        const res = meters / toMeters[toEl.value];
        resultEl.innerText = `${res.toLocaleString(undefined, {maximumFractionDigits: 4})} ${toEl.value}`;
    }

    [valEl, fromEl, toEl].forEach(el => el.addEventListener('input', convert));
    convert();
    