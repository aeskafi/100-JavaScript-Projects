function getNextSeptemberFifth() {
    const now = new Date();
    let year = now.getFullYear();
    let target = new Date(`Sep 5, ${year} 00:00:00`);
    if (target.getTime() <= now.getTime()) {
        target = new Date(`Sep 5, ${year + 1} 00:00:00`);
    }
    return target;
}

let targetDate = getNextSeptemberFifth();
let intervalId = null;

function updateCountdown() {
    const now = new Date().getTime();
    const distance = targetDate.getTime() - now;

    const targetLabel = document.getElementById('targetLabel');
    targetLabel.innerText = `Counting down to: ${targetDate.toLocaleDateString(undefined, {
        weekday: 'short',
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    })}`;

    if (distance <= 0) {
        document.getElementById('day').innerText = '00';
        document.getElementById('hour').innerText = '00';
        document.getElementById('minutes').innerText = '00';
        document.getElementById('second').innerText = '00';
        targetLabel.innerText = 'Countdown reached! 🎊';
        return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById('day').innerText = String(days).padStart(2, '0');
    document.getElementById('hour').innerText = String(hours).padStart(2, '0');
    document.getElementById('minutes').innerText = String(minutes).padStart(2, '0');
    document.getElementById('second').innerText = String(seconds).padStart(2, '0');
}

function init() {
    updateCountdown();
    intervalId = setInterval(updateCountdown, 1000);

    const customDateInput = document.getElementById('customDate');
    const setCustomBtn = document.getElementById('setCustomDate');

    // Pre-fill input with local ISO string
    const tzOffset = targetDate.getTimezoneOffset() * 60000;
    const localISOTime = new Date(targetDate.getTime() - tzOffset).toISOString().slice(0, 16);
    customDateInput.value = localISOTime;

    setCustomBtn.addEventListener('click', () => {
        if (!customDateInput.value) return;
        const newDate = new Date(customDateInput.value);
        if (!isNaN(newDate.getTime())) {
            targetDate = newDate;
            updateCountdown();
        }
    });
}

window.addEventListener('DOMContentLoaded', init);