
    const dec = document.getElementById('decInput');
    const bin = document.getElementById('binInput');
    const hex = document.getElementById('hexInput');
    const oct = document.getElementById('octInput');

    function updateAll(n) {
        if (isNaN(n)) {
            bin.value = ''; hex.value = ''; oct.value = ''; dec.value = '';
            return;
        }
        dec.value = n;
        bin.value = n.toString(2);
        hex.value = n.toString(16).toUpperCase();
        oct.value = n.toString(8);
    }

    dec.addEventListener('input', () => updateAll(parseInt(dec.value, 10)));
    bin.addEventListener('input', () => updateAll(parseInt(bin.value, 2)));
    hex.addEventListener('input', () => updateAll(parseInt(hex.value, 16)));
    oct.addEventListener('input', () => updateAll(parseInt(oct.value, 8)));
    