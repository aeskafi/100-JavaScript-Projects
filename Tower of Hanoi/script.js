
    const pegs = [[3, 2, 1], [], []];
    let selectedPeg = null;

    function render() {
        for (let i = 0; i < 3; i++) {
            const el = document.getElementById(`peg${i}`);
            el.innerHTML = '';
            pegs[i].forEach(size => {
                const disc = document.createElement('div');
                disc.style.width = `${size * 22}px`;
                disc.className = 'h-5 bg-cyan-500 rounded my-0.5 shadow';
                el.appendChild(disc);
            });
            if (selectedPeg === i) el.classList.add('bg-slate-900');
            else el.classList.remove('bg-slate-900');
        }
    }

    document.querySelectorAll('.peg').forEach((p, idx) => {
        p.addEventListener('click', () => {
            if (selectedPeg === null) {
                if (pegs[idx].length > 0) selectedPeg = idx;
            } else {
                const topFrom = pegs[selectedPeg][pegs[selectedPeg].length - 1];
                const topTo = pegs[idx][pegs[idx].length - 1];
                if (!topTo || topFrom < topTo) {
                    pegs[idx].push(pegs[selectedPeg].pop());
                }
                selectedPeg = null;
            }
            render();
        });
    });

    render();
    