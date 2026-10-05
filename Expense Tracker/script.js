
    let txs = JSON.parse(localStorage.getItem('micro_expenses') || '[]');
    const desc = document.getElementById('expDesc');
    const amt = document.getElementById('expAmt');
    const list = document.getElementById('expList');
    const netBal = document.getElementById('netBalance');
    const totExp = document.getElementById('totalExp');

    function save() {
        localStorage.setItem('micro_expenses', JSON.stringify(txs));
        render();
    }

    function render() {
        list.innerHTML = '';
        let balance = 0;
        let expenses = 0;

        txs.forEach((t, i) => {
            balance += t.amount;
            if (t.amount < 0) expenses += Math.abs(t.amount);

            const div = document.createElement('div');
            div.className = 'flex justify-between items-center bg-slate-900 p-2.5 rounded-xl border border-slate-800 text-xs';
            div.innerHTML = `
                <span class="text-slate-200">${t.desc}</span>
                <div class="flex items-center gap-2">
                    <span class="font-mono font-bold ${t.amount >= 0 ? 'text-emerald-400' : 'text-rose-400'}">${t.amount >= 0 ? '+' : ''}$${t.amount.toFixed(2)}</span>
                    <button class="text-slate-500 hover:text-rose-400">✕</button>
                </div>
            `;
            div.querySelector('button').addEventListener('click', () => { txs.splice(i, 1); save(); });
            list.appendChild(div);
        });

        netBal.innerText = '$' + balance.toFixed(2);
        totExp.innerText = '$' + expenses.toFixed(2);
    }

    document.getElementById('addExp').addEventListener('click', () => {
        const d = desc.value.trim();
        const a = parseFloat(amt.value);
        if (!d || isNaN(a)) return;
        txs.unshift({ desc: d, amount: a });
        desc.value = '';
        amt.value = '';
        save();
    });

    render();
    