
    const prompt = document.getElementById('typePrompt');
    const input = document.getElementById('typeInput');
    const wpmEl = document.getElementById('typeWpm');
    const accEl = document.getElementById('typeAcc');

    let startTime = null;

    input.addEventListener('input', () => {
        if (!startTime) startTime = Date.now();
        const pText = prompt.innerText.trim();
        const iText = input.value;

        const timeElapsed = (Date.now() - startTime) / 1000 / 60; // minutes
        const words = iText.trim().split(/\s+/).filter(x => x.length > 0).length;
        const wpm = Math.round(words / (timeElapsed || 0.01));
        wpmEl.innerText = `${wpm} WPM`;

        let correct = 0;
        for (let i = 0; i < iText.length; i++) {
            if (iText[i] === pText[i]) correct++;
        }
        const acc = iText.length ? Math.round((correct / iText.length) * 100) : 100;
        accEl.innerText = `${acc}%`;
    });
    