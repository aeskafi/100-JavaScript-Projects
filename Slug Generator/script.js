
    const input = document.getElementById('slugInput');
    const output = document.getElementById('slugOutput');
    const copyBtn = document.getElementById('copySlug');

    function generateSlug() {
        const str = input.value;
        const slug = str
            .toLowerCase()
            .trim()
            .replace(/[^\w\s-]/g, '')
            .replace(/[\s_-]+/g, '-')
            .replace(/^-+|-+$/g, '');
        output.value = slug;
    }

    copyBtn.addEventListener('click', () => {
        navigator.clipboard.writeText(output.value);
        copyBtn.innerText = 'Copied!';
        setTimeout(() => copyBtn.innerText = 'Copy', 1500);
    });

    input.addEventListener('input', generateSlug);
    generateSlug();
    