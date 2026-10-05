
    const cards = [
        { q: 'What does DOM stand for?', a: 'Document Object Model' },
        { q: 'What is a closure in JavaScript?', a: 'A function bundled together with references to its surrounding lexical state.' },
        { q: 'What is the purpose of Promise.all()?', a: 'Resolves when all promises resolve, or rejects when any promise rejects.' },
        { q: 'What is Event Bubbling?', a: 'Events start from the deepest target element and bubble up the DOM tree.' }
    ];

    let current = 0;
    let isFlipped = false;

    const box = document.getElementById('cardBox');
    const side = document.getElementById('cardSide');
    const text = document.getElementById('cardText');

    function update() {
        const c = cards[current];
        side.innerText = isFlipped ? 'Answer' : 'Question';
        side.className = isFlipped ? 'text-xs font-bold text-emerald-400 uppercase tracking-widest mb-2' : 'text-xs font-bold text-cyan-400 uppercase tracking-widest mb-2';
        text.innerText = isFlipped ? c.a : c.q;
    }

    box.addEventListener('click', () => { isFlipped = !isFlipped; update(); });
    document.getElementById('fcFlip').addEventListener('click', () => { isFlipped = !isFlipped; update(); });
    document.getElementById('fcNext').addEventListener('click', () => { current = (current + 1) % cards.length; isFlipped = false; update(); });
    document.getElementById('fcPrev').addEventListener('click', () => { current = (current - 1 + cards.length) % cards.length; isFlipped = false; update(); });

    update();
    