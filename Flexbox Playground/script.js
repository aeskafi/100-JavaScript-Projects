
    const demo = document.getElementById('flexDemo');
    const dir = document.getElementById('flexDir');
    const just = document.getElementById('flexJust');
    const align = document.getElementById('flexAlign');

    function update() {
        demo.style.flexDirection = dir.value;
        demo.style.justifyContent = just.value;
        demo.style.alignItems = align.value;
    }

    [dir, just, align].forEach(el => el.addEventListener('change', update));
    update();
    