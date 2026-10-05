
    const box = document.getElementById('paletteBox');
    const genBtn = document.getElementById('genPalette');

    function getRandomColor() {
        const letters = '0123456789ABCDEF';
        let color = '#';
        for (let i = 0; i < 6; i++) color += letters[Math.floor(Math.random() * 16)];
        return color;
    }

    function render() {
        box.innerHTML = '';
        for (let i = 0; i < 5; i++) {
            const hex = getRandomColor();
            const div = document.createElement('div');
            div.style.backgroundColor = hex;
            div.className = 'h-full flex items-end justify-center p-2 cursor-pointer transition hover:opacity-90 active:scale-95';
            div.innerHTML = `<span class="bg-black/60 px-2 py-1 rounded text-white text-xs font-mono font-bold">${hex}</span>`;
            div.addEventListener('click', () => {
                navigator.clipboard.writeText(hex);
                div.querySelector('span').innerText = 'Copied!';
                setTimeout(() => div.querySelector('span').innerText = hex, 1000);
            });
            box.appendChild(div);
        }
    }

    genBtn.addEventListener('click', render);
    window.addEventListener('keydown', (e) => {
        if (e.code === 'Space' && e.target === document.body) {
            e.preventDefault();
            render();
        }
    });

    render();
    