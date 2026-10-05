
    const input = document.getElementById('obfInput');
    const hex = document.getElementById('obfHex');
    const uni = document.getElementById('obfUni');

    function obfuscate() {
        const val = input.value;
        hex.value = val.split('').map(c => '\\x' + c.charCodeAt(0).toString(16).padStart(2, '0')).join('');
        uni.value = val.split('').map(c => '\\u' + c.charCodeAt(0).toString(16).padStart(4, '0')).join('');
    }

    input.addEventListener('input', obfuscate);
    obfuscate();
    