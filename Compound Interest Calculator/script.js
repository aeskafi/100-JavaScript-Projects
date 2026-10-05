
    const principal = document.getElementById('principal');
    const cRate = document.getElementById('cRate');
    const cYears = document.getElementById('cYears');
    const contribution = document.getElementById('contribution');
    const futureVal = document.getElementById('futureVal');
    const totalContributed = document.getElementById('totalContributed');

    function calculate() {
        const p = parseFloat(principal.value) || 0;
        const r = (parseFloat(cRate.value) || 0) / 100;
        const y = parseFloat(cYears.value) || 0;
        const pmt = parseFloat(contribution.value) || 0;

        let total = p;
        for (let m = 0; m < y * 12; m++) {
            total = total * (1 + r / 12) + pmt;
        }
        const contributed = p + (pmt * y * 12);
        futureVal.innerText = '$' + total.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});
        totalContributed.innerText = `Total Contributed: $${contributed.toLocaleString()} | Interest Earned: $${Math.max(0, total - contributed).toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}`;
    }
    [principal, cRate, cYears, contribution].forEach(el => el.addEventListener('input', calculate));
    calculate();
    