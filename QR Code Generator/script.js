
    const input = document.getElementById('qrText');
    const img = document.getElementById('qrImg');

    input.addEventListener('input', () => {
        const val = encodeURIComponent(input.value || 'https://arham.dev');
        img.src = `https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=${val}`;
    });
    