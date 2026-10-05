
    const input = document.getElementById('jsonInput');
    const status = document.getElementById('jsonStatus');

    document.getElementById('jsonFormat').addEventListener('click', () => {
        try {
            const obj = JSON.parse(input.value);
            input.value = JSON.stringify(obj, null, 2);
            status.innerText = 'Valid JSON formatted successfully!';
            status.className = 'text-xs font-mono font-medium text-emerald-400';
        } catch(e) {
            status.innerText = 'Error: ' + e.message;
            status.className = 'text-xs font-mono font-medium text-rose-400';
        }
    });

    document.getElementById('jsonMinify').addEventListener('click', () => {
        try {
            const obj = JSON.parse(input.value);
            input.value = JSON.stringify(obj);
            status.innerText = 'Minified successfully!';
            status.className = 'text-xs font-mono font-medium text-emerald-400';
        } catch(e) {
            status.innerText = 'Error: ' + e.message;
            status.className = 'text-xs font-mono font-medium text-rose-400';
        }
    });

    document.getElementById('jsonValidate').addEventListener('click', () => {
        try {
            JSON.parse(input.value);
            status.innerText = '✓ Valid JSON structure!';
            status.className = 'text-xs font-mono font-medium text-emerald-400';
        } catch(e) {
            status.innerText = '✗ Syntax Error: ' + e.message;
            status.className = 'text-xs font-mono font-medium text-rose-400';
        }
    });
    