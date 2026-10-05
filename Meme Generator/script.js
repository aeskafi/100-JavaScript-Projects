
    const canvas = document.getElementById('memeCanvas');
    const ctx = canvas.getContext('2d');
    const topInp = document.getElementById('memeTop');
    const botInp = document.getElementById('memeBot');

    function drawMeme() {
        ctx.fillStyle = '#1e293b';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.fillStyle = '#0f172a';
        ctx.fillRect(20, 20, canvas.width - 40, canvas.height - 40);

        ctx.font = 'bold 24px Impact, sans-serif';
        ctx.fillStyle = 'white';
        ctx.strokeStyle = 'black';
        ctx.lineWidth = 3;
        ctx.textAlign = 'center';

        const top = topInp.value.toUpperCase() || 'WHEN YOU AUDIT REPOS';
        const bot = botInp.value.toUpperCase() || 'AND SHIP 100 APPS IN ONE GO';

        ctx.strokeText(top, canvas.width / 2, 60);
        ctx.fillText(top, canvas.width / 2, 60);

        ctx.strokeText(bot, canvas.width / 2, canvas.height - 40);
        ctx.fillText(bot, canvas.width / 2, canvas.height - 40);
    }

    topInp.addEventListener('input', drawMeme);
    botInp.addEventListener('input', drawMeme);
    drawMeme();
    