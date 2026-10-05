
    const weight = document.getElementById('weight');
    const height = document.getElementById('height');
    const bmiVal = document.getElementById('bmiVal');
    const bmiCat = document.getElementById('bmiCat');

    function calculate() {
        const w = parseFloat(weight.value);
        const h = parseFloat(height.value) / 100;
        if (!w || !h) {
            bmiVal.innerText = '--';
            bmiCat.innerText = 'Enter height and weight';
            return;
        }
        const bmi = w / (h * h);
        bmiVal.innerText = bmi.toFixed(1);
        if (bmi < 18.5) {
            bmiCat.innerText = 'Underweight';
            bmiCat.className = 'text-sm font-semibold text-amber-400';
        } else if (bmi < 25) {
            bmiCat.innerText = 'Normal weight (Healthy)';
            bmiCat.className = 'text-sm font-semibold text-emerald-400';
        } else if (bmi < 30) {
            bmiCat.innerText = 'Overweight';
            bmiCat.className = 'text-sm font-semibold text-amber-400';
        } else {
            bmiCat.innerText = 'Obese';
            bmiCat.className = 'text-sm font-semibold text-rose-400';
        }
    }
    weight.addEventListener('input', calculate);
    height.addEventListener('input', calculate);
    