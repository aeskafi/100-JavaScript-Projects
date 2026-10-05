
    const raw = document.getElementById('urlRaw');
    const enc = document.getElementById('urlEnc');

    document.getElementById('urlEncBtn').addEventListener('click', () => {
        enc.value = encodeURIComponent(raw.value);
    });
    document.getElementById('urlDecBtn').addEventListener('click', () => {
        try {
            raw.value = decodeURIComponent(enc.value);
        } catch(e) {
            raw.value = 'Malformed URI sequence';
        }
    });
    document.getElementById('urlEncBtn').click();
    