
    const target = document.getElementById('clipTarget');
    const css = document.getElementById('clipCss');

    const shapes = {
        triangle: 'polygon(50% 0%, 0% 100%, 100% 100%)',
        rhombus: 'polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%)',
        star: 'polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%)'
    };

    document.querySelectorAll('.clip-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const poly = shapes[btn.dataset.shape];
            target.style.clipPath = poly;
            css.value = `clip-path: ${poly};`;
        });
    });

    document.querySelector('.clip-btn').click();
    