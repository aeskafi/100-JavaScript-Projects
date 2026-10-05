
    let bms = JSON.parse(localStorage.getItem('micro_bms') || '[{"title":"Arham Dev","url":"https://arham.dev"},{"title":"Walk Cook Live","url":"https://youtube.com/@walkcooklive"}]');
    const title = document.getElementById('bmTitle');
    const url = document.getElementById('bmUrl');
    const list = document.getElementById('bmList');

    function save() {
        localStorage.setItem('micro_bms', JSON.stringify(bms));
        render();
    }

    function render() {
        list.innerHTML = '';
        bms.forEach((b, i) => {
            const div = document.createElement('div');
            div.className = 'flex justify-between items-center bg-slate-900 border border-slate-700 p-2.5 rounded-xl text-xs';
            div.innerHTML = `
                <a href="${b.url}" target="_blank" class="text-cyan-400 hover:underline font-bold flex items-center gap-2">
                    <span>🔗</span> ${b.title}
                </a>
                <button class="text-slate-500 hover:text-rose-400">✕</button>
            `;
            div.querySelector('button').addEventListener('click', () => { bms.splice(i, 1); save(); });
            list.appendChild(div);
        });
    }

    document.getElementById('addBm').addEventListener('click', () => {
        let u = url.value.trim();
        const t = title.value.trim() || u;
        if (!u) return;
        if (!u.startsWith('http')) u = 'https://' + u;
        bms.unshift({ title: t, url: u });
        title.value = '';
        url.value = '';
        save();
    });

    render();
    