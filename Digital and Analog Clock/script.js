
    let is24Hour = false;
    const timeEl = document.getElementById('clockTime');
    const periodEl = document.getElementById('clockPeriod');
    const dateEl = document.getElementById('clockDate');
    const toggleBtn = document.getElementById('clockToggle');

    function update() {
        const now = new Date();
        let h = now.getHours();
        const m = String(now.getMinutes()).padStart(2, '0');
        const s = String(now.getSeconds()).padStart(2, '0');

        if (is24Hour) {
            timeEl.innerText = `${String(h).padStart(2, '0')}:${m}:${s}`;
            periodEl.style.display = 'none';
        } else {
            const period = h >= 12 ? 'PM' : 'AM';
            h = h % 12 || 12;
            timeEl.innerText = `${String(h).padStart(2, '0')}:${m}:${s}`;
            periodEl.innerText = period;
            periodEl.style.display = 'block';
        }

        dateEl.innerText = now.toLocaleDateString(undefined, {
            weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'
        });
    }

    toggleBtn.addEventListener('click', () => {
        is24Hour = !is24Hour;
        toggleBtn.innerText = is24Hour ? 'Switch to 12-Hour Format' : 'Switch to 24-Hour Format';
        update();
    });

    setInterval(update, 1000);
    update();
    