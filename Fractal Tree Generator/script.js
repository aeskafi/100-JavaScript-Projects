
    const canvas = document.getElementById('treeCanvas');
    const ctx = canvas.getContext('2d');
    const angleRange = document.getElementById('treeAngle');

    function drawBranch(len, angle) {
        ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.lineTo(0, -len);
        ctx.stroke();

        if (len < 10) return;

        ctx.save();
        ctx.translate(0, -len);
        ctx.rotate(angle);
        drawBranch(len * 0.72, angle);
        ctx.restore();

        ctx.save();
        ctx.translate(0, -len);
        ctx.rotate(-angle);
        drawBranch(len * 0.72, angle);
        ctx.restore();
    }

    function render() {
        ctx.fillStyle = '#0f172a';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.strokeStyle = '#06b6d4';
        ctx.lineWidth = 2;

        ctx.save();
        ctx.translate(canvas.width / 2, canvas.height);
        const rad = (parseInt(angleRange.value) * Math.PI) / 180;
        drawBranch(65, rad);
        ctx.restore();
    }

    angleRange.addEventListener('input', render);
    render();
    