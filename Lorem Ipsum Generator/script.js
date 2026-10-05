
    const words = "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum".split(' ');

    function makeSentence() {
        const len = Math.floor(Math.random() * 10) + 8;
        let s = [];
        for (let i = 0; i < len; i++) {
            s.push(words[Math.floor(Math.random() * words.length)]);
        }
        let res = s.join(' ');
        return res.charAt(0).toUpperCase() + res.slice(1) + '.';
    }

    function makeParagraph() {
        const sCount = Math.floor(Math.random() * 4) + 4;
        let p = [];
        for (let i = 0; i < sCount; i++) p.push(makeSentence());
        return p.join(' ');
    }

    const countInput = document.getElementById('loremCount');
    const genBtn = document.getElementById('genLorem');
    const copyBtn = document.getElementById('copyLorem');
    const output = document.getElementById('loremOutput');

    function generate() {
        const count = parseInt(countInput.value) || 3;
        output.innerHTML = '';
        for (let i = 0; i < count; i++) {
            const p = document.createElement('p');
            p.innerText = makeParagraph();
            output.appendChild(p);
        }
    }

    copyBtn.addEventListener('click', () => {
        navigator.clipboard.writeText(output.innerText);
        copyBtn.innerText = 'Copied!';
        setTimeout(() => copyBtn.innerText = 'Copy', 1500);
    });

    genBtn.addEventListener('click', generate);
    generate();
    