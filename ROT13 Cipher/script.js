
    const input = document.getElementById('rotInput');
    const output = document.getElementById('rotOutput');

    function rot13(str) {
        return str.replace(/[a-zA-Z]/g, function (c) {
            return String.fromCharCode((c <= 'Z' ? 90 : 122) >= (c = c.charCodeAt(0) + 13) ? c : c - 26);
        });
    }

    input.addEventListener('input', () => {
        output.value = rot13(input.value);
    });
    output.value = rot13(input.value);
    