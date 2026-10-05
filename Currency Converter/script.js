
    const rates = {
        USD: 1.0,
        EUR: 0.92,
        GBP: 0.79,
        JPY: 151.2,
        CAD: 1.36,
        AUD: 1.52
    };

    const currAmt = document.getElementById('currAmt');
    const fromCurr = document.getElementById('fromCurr');
    const toCurr = document.getElementById('toCurr');
    const convertedCurr = document.getElementById('convertedCurr');
    const rateInfo = document.getElementById('rateInfo');

    function convert() {
        const amt = parseFloat(currAmt.value) || 0;
        const from = fromCurr.value;
        const to = toCurr.value;
        const inUSD = amt / rates[from];
        const res = inUSD * rates[to];
        convertedCurr.innerText = `${res.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})} ${to}`;
        const singleRate = (rates[to] / rates[from]).toFixed(4);
        rateInfo.innerText = `1 ${from} = ${singleRate} ${to}`;
    }

    [currAmt, fromCurr, toCurr].forEach(el => el.addEventListener('input', convert));
    convert();
    