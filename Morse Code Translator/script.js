
    const MORSE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', '0': '-----', ' ': '/'
    };
    const REVERSE_MORSE = {};
    for (let k in MORSE) REVERSE_MORSE[MORSE[k]] = k;

    const textEl = document.getElementById('morseText');
    const codeEl = document.getElementById('morseCode');

    textEl.addEventListener('input', () => {
        const val = textEl.value.toUpperCase();
        codeEl.value = val.split('').map(c => MORSE[c] || c).join(' ');
    });

    codeEl.addEventListener('input', () => {
        const tokens = codeEl.value.trim().split(/\s+/);
        textEl.value = tokens.map(t => REVERSE_MORSE[t] || (t === '/' ? ' ' : '')).join('');
    });

    textEl.dispatchEvent(new Event('input'));
    