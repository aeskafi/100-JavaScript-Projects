
    const input = document.getElementById('primeNum');
    const status = document.getElementById('primeStatus');
    const factors = document.getElementById('factorsList');

    function checkPrime(n) {
        if (n <= 1) return { isPrime: false, f: [1] };
        const f = [];
        for (let i = 1; i <= Math.sqrt(n); i++) {
            if (n % i === 0) {
                f.push(i);
                if (i !== n / i) f.push(n / i);
            }
        }
        f.sort((a,b) => a - b);
        return { isPrime: f.length === 2, f };
    }

    input.addEventListener('input', () => {
        const val = parseInt(input.value);
        if (isNaN(val) || val <= 0) {
            status.innerText = 'Enter a positive number';
            status.className = 'text-2xl font-bold text-slate-400';
            factors.innerText = '';
            return;
        }
        const res = checkPrime(val);
        if (res.isPrime) {
            status.innerText = `${val} is a PRIME number! 🌟`;
            status.className = 'text-2xl font-bold text-emerald-400';
            factors.innerText = `Only divisible by 1 and ${val}`;
        } else {
            status.innerText = `${val} is a COMPOSITE number`;
            status.className = 'text-2xl font-bold text-rose-400';
            factors.innerText = `Factors: ${res.f.slice(0, 10).join(', ')}${res.f.length > 10 ? '...' : ''}`;
        }
    });
    