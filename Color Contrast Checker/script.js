
    function lum(hex) {
        const rgb = parseInt(hex.slice(1), 16);
        const r = (rgb >> 16) & 0xff;
        const g = (rgb >> 8) & 0xff;
        const b = (rgb >> 0) & 0xff;
        const a = [r, g, b].map(v => {
            v /= 255;
            return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
        });
        return a[0] * 0.2126 + a[1] * 0.7152 + a[2] * 0.0722;
    }

    const fg = document.getElementById('contFg');
    const bg = document.getElementById('contBg');
    const box = document.getElementById('contrastBox');
    const ratioVal = document.getElementById('ratioVal');
    const badge = document.getElementById('wcagBadge');

    function check() {
        const l1 = lum(fg.value);
        const l2 = lum(bg.value);
        const ratio = (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);

        box.style.color = fg.value;
        box.style.backgroundColor = bg.value;

        ratioVal.innerText = ratio.toFixed(2) + ':1';
        if (ratio >= 7) {
            badge.innerText = 'Passes WCAG AAA (Super Accessible)';
            badge.className = 'text-xs font-bold text-emerald-400';
        } else if (ratio >= 4.5) {
            badge.innerText = 'Passes WCAG AA (Standard)';
            badge.className = 'text-xs font-bold text-cyan-400';
        } else {
            badge.innerText = 'Fails WCAG (Low Contrast)';
            badge.className = 'text-xs font-bold text-rose-400';
        }
    }

    fg.addEventListener('input', check);
    bg.addEventListener('input', check);
    check();
    