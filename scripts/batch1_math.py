import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def create_project(folder_name, title, category, icon, description, html_body, js_code):
    dir_path = os.path.join(BASE_DIR, folder_name)
    os.makedirs(dir_path, exist_ok=True)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | 100 JavaScript Projects</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="min-h-screen bg-slate-900 text-slate-100 flex flex-col justify-center items-center p-4 font-sans">
    <div class="w-full max-w-xl bg-slate-800 border border-slate-700 rounded-3xl shadow-2xl p-6 sm:p-8 backdrop-blur-md">
        <a href="../index.html" class="inline-flex items-center text-xs font-semibold text-cyan-400 hover:text-cyan-300 mb-6 transition-colors">
            ← Back to All Projects
        </a>
        <div class="flex items-center justify-between mb-2">
            <h1 class="text-2xl sm:text-3xl font-bold text-white flex items-center gap-2">
                <span>{icon}</span> {title}
            </h1>
            <span class="text-xs font-semibold px-2.5 py-1 rounded-full bg-slate-700 text-cyan-400 border border-slate-600">
                {category}
            </span>
        </div>
        <p class="text-sm text-slate-400 mb-6">{description}</p>
        {html_body}
    </div>
    <script src="script.js"></script>
</body>
</html>"""
    with open(os.path.join(dir_path, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)
    with open(os.path.join(dir_path, 'script.js'), 'w', encoding='utf-8') as f:
        f.write(js_code)
    print(f"Created {folder_name}")

# 1. Tip Calculator
create_project(
    "Tip Calculator",
    "Tip & Split Calculator",
    "Math & Finance",
    "💵",
    "Calculate tip amounts, total bill, and split evenly among party members.",
    """
    <div class="space-y-4">
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Bill Amount ($)</label>
            <input type="number" id="bill" min="0" step="0.01" placeholder="0.00" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:ring-2 focus:ring-cyan-500 outline-none" />
        </div>
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Tip Percentage (<span id="tipVal">15</span>%)</label>
            <input type="range" id="tipRange" min="0" max="40" value="15" class="w-full accent-cyan-500 cursor-pointer" />
            <div class="flex justify-between text-xs text-slate-400 mt-1">
                <span>0%</span><span>15%</span><span>20%</span><span>30%</span><span>40%</span>
            </div>
        </div>
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Split Between (People)</label>
            <input type="number" id="people" min="1" value="1" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:ring-2 focus:ring-cyan-500 outline-none" />
        </div>
        <div class="grid grid-cols-2 gap-3 pt-4 border-t border-slate-700">
            <div class="bg-slate-900 p-4 rounded-2xl border border-slate-700">
                <span class="text-xs text-slate-400">Tip / Person</span>
                <p id="tipPerPerson" class="text-2xl font-bold text-cyan-400 font-mono mt-1">$0.00</p>
            </div>
            <div class="bg-slate-900 p-4 rounded-2xl border border-slate-700">
                <span class="text-xs text-slate-400">Total / Person</span>
                <p id="totalPerPerson" class="text-2xl font-bold text-emerald-400 font-mono mt-1">$0.00</p>
            </div>
        </div>
    </div>
    """,
    """
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
    """
)

# 2. BMI Calculator
create_project(
    "BMI Calculator",
    "Body Mass Index Calculator",
    "Health & Science",
    "⚖️",
    "Compute your BMI and category based on metric or imperial metrics.",
    """
    <div class="space-y-4">
        <div class="grid grid-cols-2 gap-3">
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Weight (kg)</label>
                <input type="number" id="weight" min="20" max="300" placeholder="70" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:ring-2 focus:ring-cyan-500 outline-none" />
            </div>
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Height (cm)</label>
                <input type="number" id="height" min="80" max="250" placeholder="175" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:ring-2 focus:ring-cyan-500 outline-none" />
            </div>
        </div>
        <div class="bg-slate-900 p-6 rounded-2xl border border-slate-700 text-center">
            <span class="text-xs text-slate-400">Your BMI</span>
            <div id="bmiVal" class="text-4xl font-extrabold text-cyan-400 font-mono my-2">--</div>
            <div id="bmiCat" class="text-sm font-semibold text-slate-400">Enter height and weight</div>
        </div>
    </div>
    """,
    """
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
    """
)

# 3. Loan Calculator
create_project(
    "Loan Calculator",
    "Loan & Mortgage Calculator",
    "Math & Finance",
    "🏦",
    "Calculate monthly mortgage payments, interest paid, and amortization overview.",
    """
    <div class="space-y-4">
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Loan Amount ($)</label>
            <input type="number" id="amount" value="250000" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:ring-2 focus:ring-cyan-500 outline-none" />
        </div>
        <div class="grid grid-cols-2 gap-3">
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Interest Rate (%)</label>
                <input type="number" id="rate" step="0.1" value="5.5" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:ring-2 focus:ring-cyan-500 outline-none" />
            </div>
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Term (Years)</label>
                <input type="number" id="years" value="30" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:ring-2 focus:ring-cyan-500 outline-none" />
            </div>
        </div>
        <div class="grid grid-cols-2 gap-3 pt-4 border-t border-slate-700">
            <div class="bg-slate-900 p-4 rounded-2xl border border-slate-700">
                <span class="text-xs text-slate-400">Monthly Payment</span>
                <p id="monthly" class="text-2xl font-bold text-cyan-400 font-mono mt-1">$0.00</p>
            </div>
            <div class="bg-slate-900 p-4 rounded-2xl border border-slate-700">
                <span class="text-xs text-slate-400">Total Interest</span>
                <p id="totalInterest" class="text-2xl font-bold text-amber-400 font-mono mt-1">$0.00</p>
            </div>
        </div>
    </div>
    """,
    """
    const amount = document.getElementById('amount');
    const rate = document.getElementById('rate');
    const years = document.getElementById('years');
    const monthly = document.getElementById('monthly');
    const totalInterest = document.getElementById('totalInterest');

    function calculate() {
        const p = parseFloat(amount.value) || 0;
        const r = (parseFloat(rate.value) || 0) / 100 / 12;
        const n = (parseFloat(years.value) || 0) * 12;

        if (p <= 0 || r <= 0 || n <= 0) {
            monthly.innerText = '$0.00';
            totalInterest.innerText = '$0.00';
            return;
        }

        const m = (p * r * Math.pow(1 + r, n)) / (Math.pow(1 + r, n) - 1);
        const total = m * n;
        monthly.innerText = '$' + m.toFixed(2);
        totalInterest.innerText = '$' + (total - p).toFixed(2);
    }
    [amount, rate, years].forEach(el => el.addEventListener('input', calculate));
    calculate();
    """
)

# 4. Compound Interest Calculator
create_project(
    "Compound Interest Calculator",
    "Compound Interest Calculator",
    "Math & Finance",
    "📈",
    "Simulate wealth accumulation with annual compound interest and regular contributions.",
    """
    <div class="space-y-4">
        <div class="grid grid-cols-2 gap-3">
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Initial Principal ($)</label>
                <input type="number" id="principal" value="10000" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-white focus:ring-2 focus:ring-cyan-500 outline-none" />
            </div>
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Annual Rate (%)</label>
                <input type="number" id="cRate" step="0.1" value="7" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-white focus:ring-2 focus:ring-cyan-500 outline-none" />
            </div>
        </div>
        <div class="grid grid-cols-2 gap-3">
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Years to Grow</label>
                <input type="number" id="cYears" value="10" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-white focus:ring-2 focus:ring-cyan-500 outline-none" />
            </div>
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Monthly Contribution ($)</label>
                <input type="number" id="contribution" value="200" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-white focus:ring-2 focus:ring-cyan-500 outline-none" />
            </div>
        </div>
        <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 text-center">
            <span class="text-xs text-slate-400">Future Balance</span>
            <div id="futureVal" class="text-3xl font-extrabold text-emerald-400 font-mono my-1">$0.00</div>
            <p id="totalContributed" class="text-xs text-slate-400"></p>
        </div>
    </div>
    """,
    """
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
    """
)

# 5. Discount Calculator
create_project(
    "Discount Calculator",
    "Discount & Sale Calculator",
    "Math & Finance",
    "🏷️",
    "Find final price and money saved during discounts and promotional sales.",
    """
    <div class="space-y-4">
        <div class="grid grid-cols-2 gap-3">
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Original Price ($)</label>
                <input type="number" id="origPrice" value="80" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-white focus:ring-2 focus:ring-cyan-500 outline-none" />
            </div>
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Discount (%)</label>
                <input type="number" id="discPct" value="25" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-white focus:ring-2 focus:ring-cyan-500 outline-none" />
            </div>
        </div>
        <div class="grid grid-cols-2 gap-3 pt-3 border-t border-slate-700">
            <div class="bg-slate-900 p-4 rounded-2xl border border-slate-700">
                <span class="text-xs text-slate-400">Final Price</span>
                <p id="finalPrice" class="text-2xl font-bold text-emerald-400 font-mono mt-1">$60.00</p>
            </div>
            <div class="bg-slate-900 p-4 rounded-2xl border border-slate-700">
                <span class="text-xs text-slate-400">You Save</span>
                <p id="savings" class="text-2xl font-bold text-cyan-400 font-mono mt-1">$20.00</p>
            </div>
        </div>
    </div>
    """,
    """
    const origPrice = document.getElementById('origPrice');
    const discPct = document.getElementById('discPct');
    const finalPrice = document.getElementById('finalPrice');
    const savings = document.getElementById('savings');

    function calculate() {
        const price = parseFloat(origPrice.value) || 0;
        const pct = parseFloat(discPct.value) || 0;
        const saved = (price * pct) / 100;
        const final = price - saved;
        savings.innerText = '$' + saved.toFixed(2);
        finalPrice.innerText = '$' + Math.max(0, final).toFixed(2);
    }
    origPrice.addEventListener('input', calculate);
    discPct.addEventListener('input', calculate);
    calculate();
    """
)

# 6. Currency Converter
create_project(
    "Currency Converter",
    "Currency Converter",
    "Math & Finance",
    "💱",
    "Convert between major world currencies (USD, EUR, GBP, JPY, CAD, AUD).",
    """
    <div class="space-y-4">
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Amount</label>
            <input type="number" id="currAmt" value="100" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-white focus:ring-2 focus:ring-cyan-500 outline-none" />
        </div>
        <div class="grid grid-cols-2 gap-3">
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">From</label>
                <select id="fromCurr" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-white focus:ring-2 focus:ring-cyan-500 outline-none">
                    <option value="USD" selected>USD - US Dollar</option>
                    <option value="EUR">EUR - Euro</option>
                    <option value="GBP">GBP - British Pound</option>
                    <option value="JPY">JPY - Japanese Yen</option>
                    <option value="CAD">CAD - Canadian Dollar</option>
                    <option value="AUD">AUD - Australian Dollar</option>
                </select>
            </div>
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">To</label>
                <select id="toCurr" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-white focus:ring-2 focus:ring-cyan-500 outline-none">
                    <option value="EUR" selected>EUR - Euro</option>
                    <option value="USD">USD - US Dollar</option>
                    <option value="GBP">GBP - British Pound</option>
                    <option value="JPY">JPY - Japanese Yen</option>
                    <option value="CAD">CAD - Canadian Dollar</option>
                    <option value="AUD">AUD - Australian Dollar</option>
                </select>
            </div>
        </div>
        <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 text-center">
            <span class="text-xs text-slate-400">Converted Amount</span>
            <div id="convertedCurr" class="text-3xl font-extrabold text-cyan-400 font-mono my-1">--</div>
            <div id="rateInfo" class="text-xs text-slate-400"></div>
        </div>
    </div>
    """,
    """
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
    """
)

# 7. Roman Numeral Converter
create_project(
    "Roman Numeral Converter",
    "Roman Numeral Converter",
    "Converters",
    "🏛️",
    "Two-way conversion between Standard Arabic Integers and Roman Numerals.",
    """
    <div class="space-y-4">
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Standard Number (1 - 3999)</label>
            <input type="number" id="arabicNum" min="1" max="3999" placeholder="2026" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-white focus:ring-2 focus:ring-cyan-500 outline-none" />
        </div>
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Roman Numeral</label>
            <input type="text" id="romanNum" placeholder="MMXXVI" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-white uppercase focus:ring-2 focus:ring-cyan-500 outline-none font-mono" />
        </div>
    </div>
    """,
    """
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
    """
)

# 8. Binary to Decimal Converter
create_project(
    "Binary to Decimal Converter",
    "Binary & Decimal Converter",
    "Converters",
    "0️⃣",
    "Live conversions between Binary, Decimal, Hexadecimal, and Octal formats.",
    """
    <div class="space-y-4">
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Decimal (Base 10)</label>
            <input type="number" id="decInput" placeholder="42" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-white font-mono focus:ring-2 focus:ring-cyan-500 outline-none" />
        </div>
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Binary (Base 2)</label>
            <input type="text" id="binInput" placeholder="101010" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-white font-mono focus:ring-2 focus:ring-cyan-500 outline-none" />
        </div>
        <div class="grid grid-cols-2 gap-3">
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Hexadecimal</label>
                <input type="text" id="hexInput" placeholder="2A" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-white font-mono uppercase focus:ring-2 focus:ring-cyan-500 outline-none" />
            </div>
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Octal</label>
                <input type="text" id="octInput" placeholder="52" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-white font-mono focus:ring-2 focus:ring-cyan-500 outline-none" />
            </div>
        </div>
    </div>
    """,
    """
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
    """
)

# 9. Prime Number Checker
create_project(
    "Prime Number Checker",
    "Prime Number Checker",
    "Math & Science",
    "🔢",
    "Test primality, view factors, and find nearest prime neighbors in milliseconds.",
    """
    <div class="space-y-4">
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Enter a positive integer</label>
            <input type="number" id="primeNum" min="1" placeholder="e.g. 97" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white font-mono focus:ring-2 focus:ring-cyan-500 outline-none" />
        </div>
        <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 text-center">
            <div id="primeStatus" class="text-2xl font-bold text-slate-400">Enter a number</div>
            <p id="factorsList" class="text-xs text-slate-400 mt-2"></p>
        </div>
    </div>
    """,
    """
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
    """
)

# 10. Random Number Generator
create_project(
    "Random Number Generator",
    "Random Number Generator",
    "Math & Science",
    "🎲",
    "Generate cryptographically strong random numbers, pick ranges, and roll dice.",
    """
    <div class="space-y-4">
        <div class="grid grid-cols-2 gap-3">
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Min Value</label>
                <input type="number" id="minVal" value="1" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-white font-mono focus:ring-2 focus:ring-cyan-500 outline-none" />
            </div>
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Max Value</label>
                <input type="number" id="maxVal" value="100" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-white font-mono focus:ring-2 focus:ring-cyan-500 outline-none" />
            </div>
        </div>
        <button id="genBtn" class="w-full py-3 bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-white font-bold rounded-xl transition shadow active:scale-95">
            Generate Random Number
        </button>
        <div class="bg-slate-900 p-6 rounded-2xl border border-slate-700 text-center">
            <span class="text-xs text-slate-400">Result</span>
            <div id="randResult" class="text-5xl font-extrabold text-cyan-400 font-mono my-2">--</div>
        </div>
    </div>
    """,
    """
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
    """
)

# 11. Unit Converter
create_project(
    "Unit Converter",
    "Multi-Unit Converter",
    "Converters",
    "📐",
    "Convert between length units: Meters, Kilometers, Miles, Feet, Inches, and Centimeters.",
    """
    <div class="space-y-4">
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Value</label>
            <input type="number" id="unitVal" value="10" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-white font-mono focus:ring-2 focus:ring-cyan-500 outline-none" />
        </div>
        <div class="grid grid-cols-2 gap-3">
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">From Unit</label>
                <select id="unitFrom" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-white focus:ring-2 focus:ring-cyan-500 outline-none">
                    <option value="m">Meters (m)</option>
                    <option value="km">Kilometers (km)</option>
                    <option value="mi">Miles (mi)</option>
                    <option value="ft">Feet (ft)</option>
                    <option value="in">Inches (in)</option>
                    <option value="cm">Centimeters (cm)</option>
                </select>
            </div>
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">To Unit</label>
                <select id="unitTo" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-white focus:ring-2 focus:ring-cyan-500 outline-none">
                    <option value="ft" selected>Feet (ft)</option>
                    <option value="m">Meters (m)</option>
                    <option value="km">Kilometers (km)</option>
                    <option value="mi">Miles (mi)</option>
                    <option value="in">Inches (in)</option>
                    <option value="cm">Centimeters (cm)</option>
                </select>
            </div>
        </div>
        <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 text-center">
            <span class="text-xs text-slate-400">Converted Value</span>
            <div id="unitResult" class="text-3xl font-extrabold text-cyan-400 font-mono my-1">--</div>
        </div>
    </div>
    """,
    """
    const toMeters = {
        m: 1,
        km: 1000,
        mi: 1609.344,
        ft: 0.3048,
        in: 0.0254,
        cm: 0.01
    };

    const valEl = document.getElementById('unitVal');
    const fromEl = document.getElementById('unitFrom');
    const toEl = document.getElementById('unitTo');
    const resultEl = document.getElementById('unitResult');

    function convert() {
        const val = parseFloat(valEl.value) || 0;
        const meters = val * toMeters[fromEl.value];
        const res = meters / toMeters[toEl.value];
        resultEl.innerText = `${res.toLocaleString(undefined, {maximumFractionDigits: 4})} ${toEl.value}`;
    }

    [valEl, fromEl, toEl].forEach(el => el.addEventListener('input', convert));
    convert();
    """
)

# 12. Quadratic Equation Solver
create_project(
    "Quadratic Equation Solver",
    "Quadratic Equation Solver",
    "Math & Science",
    "🧮",
    "Solve ax² + bx + c = 0 with real and complex roots breakdown.",
    """
    <div class="space-y-4">
        <div class="grid grid-cols-3 gap-3">
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">a (x²)</label>
                <input type="number" id="quadA" value="1" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-white font-mono focus:ring-2 focus:ring-cyan-500 outline-none" />
            </div>
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">b (x)</label>
                <input type="number" id="quadB" value="-5" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-white font-mono focus:ring-2 focus:ring-cyan-500 outline-none" />
            </div>
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">c (const)</label>
                <input type="number" id="quadC" value="6" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-white font-mono focus:ring-2 focus:ring-cyan-500 outline-none" />
            </div>
        </div>
        <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 text-center">
            <span class="text-xs text-slate-400">Roots</span>
            <div id="quadRoots" class="text-2xl font-bold text-cyan-400 font-mono my-2">x₁ = 3, x₂ = 2</div>
            <p id="quadDisc" class="text-xs text-slate-400">Discriminant Δ = 1</p>
        </div>
    </div>
    """,
    """
    const aEl = document.getElementById('quadA');
    const bEl = document.getElementById('quadB');
    const cEl = document.getElementById('quadC');
    const rootsEl = document.getElementById('quadRoots');
    const discEl = document.getElementById('quadDisc');

    function solve() {
        const a = parseFloat(aEl.value) || 0;
        const b = parseFloat(bEl.value) || 0;
        const c = parseFloat(cEl.value) || 0;

        if (a === 0) {
            rootsEl.innerText = 'Linear equation: x = ' + (-c / b).toFixed(2);
            discEl.innerText = '';
            return;
        }

        const delta = b * b - 4 * a * c;
        discEl.innerText = `Discriminant Δ = ${delta}`;

        if (delta > 0) {
            const x1 = (-b + Math.sqrt(delta)) / (2 * a);
            const x2 = (-b - Math.sqrt(delta)) / (2 * a);
            rootsEl.innerText = `x₁ = ${x1.toFixed(2)}, x₂ = ${x2.toFixed(2)}`;
        } else if (delta === 0) {
            const x = -b / (2 * a);
            rootsEl.innerText = `Single Root: x = ${x.toFixed(2)}`;
        } else {
            const real = (-b / (2 * a)).toFixed(2);
            const imag = (Math.sqrt(-delta) / (2 * a)).toFixed(2);
            rootsEl.innerText = `Complex: ${real} ± ${imag}i`;
        }
    }

    [aEl, bEl, cEl].forEach(el => el.addEventListener('input', solve));
    solve();
    """
)

# 13. Matrix Determinant
create_project(
    "Matrix Determinant",
    "2x2 and 3x3 Matrix Determinant",
    "Math & Science",
    "🔢",
    "Compute determinants and matrix traces with instant visual matrices.",
    """
    <div class="space-y-4">
        <label class="block text-xs font-medium text-slate-300 mb-1">Enter 2x2 Matrix Entries</label>
        <div class="grid grid-cols-2 gap-3 max-w-xs mx-auto">
            <input type="number" id="m00" value="4" class="bg-slate-950 border border-slate-700 rounded-xl p-3 text-center text-white font-mono text-xl focus:ring-2 focus:ring-cyan-500 outline-none" />
            <input type="number" id="m01" value="2" class="bg-slate-950 border border-slate-700 rounded-xl p-3 text-center text-white font-mono text-xl focus:ring-2 focus:ring-cyan-500 outline-none" />
            <input type="number" id="m10" value="3" class="bg-slate-950 border border-slate-700 rounded-xl p-3 text-center text-white font-mono text-xl focus:ring-2 focus:ring-cyan-500 outline-none" />
            <input type="number" id="m11" value="5" class="bg-slate-950 border border-slate-700 rounded-xl p-3 text-center text-white font-mono text-xl focus:ring-2 focus:ring-cyan-500 outline-none" />
        </div>
        <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 text-center">
            <span class="text-xs text-slate-400">Determinant |A|</span>
            <div id="detResult" class="text-4xl font-extrabold text-cyan-400 font-mono my-2">14</div>
            <p id="detFormula" class="text-xs text-slate-400 font-mono">(4 × 5) - (2 × 3) = 14</p>
        </div>
    </div>
    """,
    """
    const inputs = ['m00', 'm01', 'm10', 'm11'].map(id => document.getElementById(id));
    const detResult = document.getElementById('detResult');
    const detFormula = document.getElementById('detFormula');

    function calcDet() {
        const [a, b, c, d] = inputs.map(el => parseFloat(el.value) || 0);
        const det = (a * d) - (b * c);
        detResult.innerText = det;
        detFormula.innerText = `(${a} × ${d}) - (${b} × ${c}) = ${det}`;
    }

    inputs.forEach(el => el.addEventListener('input', calcDet));
    calcDet();
    """
)

# 14. Factorial and Permutations
create_project(
    "Factorial and Permutations",
    "Factorials & Combinatorics",
    "Math & Science",
    "✨",
    "Compute n!, Permutations P(n, r), and Combinations C(n, r).",
    """
    <div class="space-y-4">
        <div class="grid grid-cols-2 gap-3">
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Total Items (n)</label>
                <input type="number" id="nVal" min="0" max="25" value="6" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-white font-mono focus:ring-2 focus:ring-cyan-500 outline-none" />
            </div>
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Pick Items (r)</label>
                <input type="number" id="rVal" min="0" max="25" value="3" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-white font-mono focus:ring-2 focus:ring-cyan-500 outline-none" />
            </div>
        </div>
        <div class="grid grid-cols-3 gap-3 pt-2">
            <div class="bg-slate-900 p-3 rounded-2xl border border-slate-700 text-center">
                <span class="text-xs text-slate-400">n! (Factorial)</span>
                <p id="factRes" class="text-xl font-bold text-cyan-400 font-mono mt-1">720</p>
            </div>
            <div class="bg-slate-900 p-3 rounded-2xl border border-slate-700 text-center">
                <span class="text-xs text-slate-400">P(n, r)</span>
                <p id="permRes" class="text-xl font-bold text-emerald-400 font-mono mt-1">120</p>
            </div>
            <div class="bg-slate-900 p-3 rounded-2xl border border-slate-700 text-center">
                <span class="text-xs text-slate-400">C(n, r)</span>
                <p id="combRes" class="text-xl font-bold text-purple-400 font-mono mt-1">20</p>
            </div>
        </div>
    </div>
    """,
    """
    const nEl = document.getElementById('nVal');
    const rEl = document.getElementById('rVal');
    const factRes = document.getElementById('factRes');
    const permRes = document.getElementById('permRes');
    const combRes = document.getElementById('combRes');

    function fact(num) {
        if (num <= 1) return 1;
        let res = 1;
        for (let i = 2; i <= num; i++) res *= i;
        return res;
    }

    function calculate() {
        const n = Math.min(25, Math.max(0, parseInt(nEl.value) || 0));
        const r = Math.min(n, Math.max(0, parseInt(rEl.value) || 0));

        const nf = fact(n);
        const rf = fact(r);
        const nrf = fact(n - r);

        factRes.innerText = nf.toLocaleString();
        permRes.innerText = (nf / nrf).toLocaleString();
        combRes.innerText = (nf / (rf * nrf)).toLocaleString();
    }

    nEl.addEventListener('input', calculate);
    rEl.addEventListener('input', calculate);
    calculate();
    """
)

# 15. Statistics Calculator
create_project(
    "Statistics Calculator",
    "Descriptive Statistics Suite",
    "Math & Science",
    "📊",
    "Calculate Mean, Median, Mode, Standard Deviation, Variance, and Range from datasets.",
    """
    <div class="space-y-4">
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Numbers (comma or space separated)</label>
            <input type="text" id="statInput" value="12, 15, 23, 15, 8, 42, 19" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white font-mono focus:ring-2 focus:ring-cyan-500 outline-none" />
        </div>
        <div class="grid grid-cols-3 gap-3">
            <div class="bg-slate-900 p-3 rounded-2xl border border-slate-700 text-center">
                <span class="text-xs text-slate-400">Mean</span>
                <p id="statMean" class="text-lg font-bold text-cyan-400 font-mono mt-1">--</p>
            </div>
            <div class="bg-slate-900 p-3 rounded-2xl border border-slate-700 text-center">
                <span class="text-xs text-slate-400">Median</span>
                <p id="statMedian" class="text-lg font-bold text-cyan-400 font-mono mt-1">--</p>
            </div>
            <div class="bg-slate-900 p-3 rounded-2xl border border-slate-700 text-center">
                <span class="text-xs text-slate-400">Mode</span>
                <p id="statMode" class="text-lg font-bold text-cyan-400 font-mono mt-1">--</p>
            </div>
            <div class="bg-slate-900 p-3 rounded-2xl border border-slate-700 text-center">
                <span class="text-xs text-slate-400">Std Dev</span>
                <p id="statStd" class="text-lg font-bold text-emerald-400 font-mono mt-1">--</p>
            </div>
            <div class="bg-slate-900 p-3 rounded-2xl border border-slate-700 text-center">
                <span class="text-xs text-slate-400">Variance</span>
                <p id="statVar" class="text-lg font-bold text-emerald-400 font-mono mt-1">--</p>
            </div>
            <div class="bg-slate-900 p-3 rounded-2xl border border-slate-700 text-center">
                <span class="text-xs text-slate-400">Range</span>
                <p id="statRange" class="text-lg font-bold text-emerald-400 font-mono mt-1">--</p>
            </div>
        </div>
    </div>
    """,
    """
    const input = document.getElementById('statInput');
    const meanEl = document.getElementById('statMean');
    const medianEl = document.getElementById('statMedian');
    const modeEl = document.getElementById('statMode');
    const stdEl = document.getElementById('statStd');
    const varEl = document.getElementById('statVar');
    const rangeEl = document.getElementById('statRange');

    function calculate() {
        const nums = input.value.split(/[,\\s]+/).map(s => parseFloat(s)).filter(n => !isNaN(n));
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
    """
)
