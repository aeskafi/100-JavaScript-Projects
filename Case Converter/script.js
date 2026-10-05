
    const input = document.getElementById('caseInput');
    const buttons = document.querySelectorAll('.case-btn');

    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            const val = input.value;
            const mode = btn.dataset.case;
            if (mode === 'upper') input.value = val.toUpperCase();
            if (mode === 'lower') input.value = val.toLowerCase();
            if (mode === 'title') input.value = val.replace(/\w\S*/g, (txt) => txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase());
            if (mode === 'camel') {
                input.value = val.toLowerCase().replace(/[^a-zA-Z0-9]+(.)/g, (m, chr) => chr.toUpperCase());
            }
            if (mode === 'snake') {
                input.value = val.match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
                    .map(x => x.toLowerCase()).join('_');
            }
            if (mode === 'kebab') {
                input.value = val.match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
                    .map(x => x.toLowerCase()).join('-');
            }
        });
    });
    