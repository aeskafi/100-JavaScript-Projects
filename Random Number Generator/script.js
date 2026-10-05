
    const minVal = document.getElementById('minVal');
    const maxVal = document.getElementById('maxVal');
    const genBtn = document.getElementById('genBtn');
    const randResult = document.getElementById('randResult');

    genBtn.addEventListener('click', () => {
        const min = parseInt(minVal.value) || 0;
        const max = parseInt(maxVal.value) || 100;
        if (min >= max) {
            randResult.innerText = 'Invalid';
            return;
        }
        const val = Math.floor(Math.random() * (max - min + 1)) + min;
        randResult.innerText = val;
    });
    