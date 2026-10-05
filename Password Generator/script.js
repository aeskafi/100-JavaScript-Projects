
    const passOut = document.getElementById('passOut');
    const copyPass = document.getElementById('copyPass');
    const refreshPass = document.getElementById('refreshPass');
    const passLen = document.getElementById('passLen');
    const lenVal = document.getElementById('lenVal');

    const chars = {
        upper: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        lower: 'abcdefghijklmnopqrstuvwxyz',
        nums: '0123456789',
        syms: '!@#$%^&*()_+~|}{[]:;?><,./-='
    };

    function generate() {
        let pool = '';
        if (document.getElementById('incUpper').checked) pool += chars.upper;
        if (document.getElementById('incLower').checked) pool += chars.lower;
        if (document.getElementById('incNums').checked) pool += chars.nums;
        if (document.getElementById('incSyms').checked) pool += chars.syms;

        if (!pool) { passOut.value = 'Select at least one set'; return; }

        const len = parseInt(passLen.value);
        lenVal.innerText = len;
        let pass = '';
        const arr = new Uint32Array(len);
        window.crypto.getRandomValues(arr);
        for (let i = 0; i < len; i++) {
            pass += pool[arr[i] % pool.length];
        }
        passOut.value = pass;
    }

    copyPass.addEventListener('click', () => {
        navigator.clipboard.writeText(passOut.value);
        copyPass.innerText = 'Copied!';
        setTimeout(() => copyPass.innerText = 'Copy', 1500);
    });

    [passLen, refreshPass, document.getElementById('incUpper'), document.getElementById('incLower'), document.getElementById('incNums'), document.getElementById('incSyms')].forEach(el => el.addEventListener('input', generate));
    generate();
    