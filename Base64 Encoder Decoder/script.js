
    const textEl = document.getElementById('b64Text');
    const cipherEl = document.getElementById('b64Cipher');

    document.getElementById('b64Encode').addEventListener('click', () => {
        try {
            cipherEl.value = btoa(unescape(encodeURIComponent(textEl.value)));
        } catch(e) {
            cipherEl.value = 'Encoding error: ' + e.message;
        }
    });

    document.getElementById('b64Decode').addEventListener('click', () => {
        try {
            textEl.value = decodeURIComponent(escape(atob(cipherEl.value)));
        } catch(e) {
            textEl.value = 'Invalid Base64 string';
        }
    });

    document.getElementById('b64Encode').click();
    