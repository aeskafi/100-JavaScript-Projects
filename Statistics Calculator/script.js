
    const input = document.getElementById('statInput');
    const meanEl = document.getElementById('statMean');
    const medianEl = document.getElementById('statMedian');
    const modeEl = document.getElementById('statMode');
    const stdEl = document.getElementById('statStd');
    const varEl = document.getElementById('statVar');
    const rangeEl = document.getElementById('statRange');

    function calculate() {
        const nums = input.value.split(/[,\s]+/).map(s => parseFloat(s)).filter(n => !isNaN(n));
        if (nums.length === 0) return;

        nums.sort((a, b) => a - b);
        const sum = nums.reduce((a, b) => a + b, 0);
        const mean = sum / nums.length;

        let median;
        const mid = Math.floor(nums.length / 2);
        if (nums.length % 2 === 0) {
            median = (nums[mid - 1] + nums[mid]) / 2;
        } else {
            median = nums[mid];
        }

        const counts = {};
        let maxCount = 0;
        let mode = [];
        nums.forEach(n => {
            counts[n] = (counts[n] || 0) + 1;
            if (counts[n] > maxCount) maxCount = counts[n];
        });
        if (maxCount > 1) {
            for (let k in counts) {
                if (counts[k] === maxCount) mode.push(k);
            }
        }

        const variance = nums.reduce((acc, n) => acc + Math.pow(n - mean, 2), 0) / nums.length;
        const stdDev = Math.sqrt(variance);
        const range = nums[nums.length - 1] - nums[0];

        meanEl.innerText = mean.toFixed(2);
        medianEl.innerText = median.toFixed(2);
        modeEl.innerText = mode.length ? mode.join(', ') : 'None';
        stdEl.innerText = stdDev.toFixed(2);
        varEl.innerText = variance.toFixed(2);
        rangeEl.innerText = range.toFixed(2);
    }

    input.addEventListener('input', calculate);
    calculate();
    