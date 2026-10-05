
    const romanMap = [
        [1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
        [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'],
        [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']
    ];

    function toRoman(num) {
        if (num < 1 || num > 3999) return '';
        let res = '';
        for (const [val, sym] of romanMap) {
            while (num >= val) {
                res += sym;
                num -= val;
            }
        }
        return res;
    }

    function fromRoman(str) {
        const valMap = { M: 1000, D: 500, C: 100, L: 50, X: 10, V: 5, I: 1 };
        let total = 0;
        let prev = 0;
        const clean = str.toUpperCase().trim();
        for (let i = clean.length - 1; i >= 0; i--) {
            const curr = valMap[clean[i]] || 0;
            if (curr < prev) total -= curr;
            else total += curr;
            prev = curr;
        }
        return total || '';
    }

    const arabicInput = document.getElementById('arabicNum');
    const romanInput = document.getElementById('romanNum');

    arabicInput.addEventListener('input', () => {
        const val = parseInt(arabicInput.value);
        romanInput.value = isNaN(val) ? '' : toRoman(val);
    });

    romanInput.addEventListener('input', () => {
        const val = fromRoman(romanInput.value);
        arabicInput.value = val;
    });
    