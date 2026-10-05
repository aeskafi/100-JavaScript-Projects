
    const bill = document.getElementById('bill');
    const tipRange = document.getElementById('tipRange');
    const tipVal = document.getElementById('tipVal');
    const people = document.getElementById('people');
    const tipPerPerson = document.getElementById('tipPerPerson');
    const totalPerPerson = document.getElementById('totalPerPerson');

    function calculate() {
        const billAmt = parseFloat(bill.value) || 0;
        const tipPct = parseFloat(tipRange.value) || 0;
        const numPeople = parseInt(people.value) || 1;
        tipVal.innerText = tipPct;

        const totalTip = (billAmt * tipPct) / 100;
        const totalBill = billAmt + totalTip;

        tipPerPerson.innerText = '$' + (totalTip / numPeople).toFixed(2);
        totalPerPerson.innerText = '$' + (totalBill / numPeople).toFixed(2);
    }

    [bill, tipRange, people].forEach(el => el.addEventListener('input', calculate));
    