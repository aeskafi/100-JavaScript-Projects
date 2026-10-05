
    const canvas = document.getElementById('paintCanvas');
    const ctx = canvas.getContext('2d');
    const color = document.getElementById('drawColor');
    const size = document.getElementById('drawSize');

    let painting = false;

    function start(e) {
        painting = true;
        draw(e);
    }
    function end() {
        painting = false;
        ctx.beginPath();
    }
    function draw(e) {
        if (!painting) return;
        const rect = canvas.getBoundingClientRect();
        const scaleX = canvas.width / rect.width;
        const scaleY = canvas.height / rect.height;
        const clientX = e.clientX || (e.touches && e.touches[0].clientX);
        const clientY = e.clientY || (e.touches && e.touches[0].clientY);

        ctx.lineWidth = size.value;
        ctx.lineCap = 'round';
        ctx.strokeStyle = color.value;

        ctx.lineTo((clientX - rect.left) * scaleX, (clientY - rect.top) * scaleY);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo((clientX - rect.left) * scaleX, (clientY - rect.top) * scaleY);
    }

    canvas.addEventListener('mousedown', start);
    canvas.addEventListener('mouseup', end);
    canvas.addEventListener('mousemove', draw);
    canvas.addEventListener('touchstart', (e) => { e.preventDefault(); start(e); });
    canvas.addEventListener('touchend', end);
    canvas.addEventListener('touchmove', (e) => { e.preventDefault(); draw(e); });

    document.getElementById('clearCanvas').addEventListener('click', () => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    });

    document.getElementById('saveCanvas').addEventListener('click', () => {
        const link = document.createElement('a');
        link.download = 'sketch.png';
        link.href = canvas.toDataURL();
        link.click();
    });
    