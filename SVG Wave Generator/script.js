
    const svg = document.getElementById('waveSvg');
    const btn = document.getElementById('waveGen');

    function makeWave() {
        const y1 = Math.floor(Math.random() * 80) + 30;
        const y2 = Math.floor(Math.random() * 80) + 30;
        const y3 = Math.floor(Math.random() * 80) + 30;
        const path = `M 0,${y1} C 150,${y2} 350,${y3} 500,${y1} L 500,150 L 0,150 Z`;
        svg.innerHTML = `<path d="${path}" fill="#06b6d4"></path>`;
    }

    btn.addEventListener('click', makeWave);
    makeWave();
    