
    const emojis = [
        { char: '🔥', name: 'fire hot lit' },
        { char: '🚀', name: 'rocket space launch' },
        { char: '✨', name: 'sparkles stars magic' },
        { char: '⚡', name: 'zap lightning speed' },
        { char: '💻', name: 'laptop computer code' },
        { char: '🎉', name: 'tada celebration party' },
        { char: '❤️', name: 'heart love red' },
        { char: '👍', name: 'thumbs up like good' },
        { char: '☕', name: 'coffee drink morning' },
        { char: '🌍', name: 'earth globe travel world' },
        { char: '🎯', name: 'target goal bullseye' },
        { char: '💡', name: 'idea bulb lightbulb' },
        { char: '🏖️', name: 'beach vacation summer nomad' },
        { char: '🍳', name: 'cooking pan food walkcooklive' },
        { char: '🥑', name: 'avocado food healthy' },
        { char: '🤖', name: 'robot ai bot tech' }
    ];

    const search = document.getElementById('emojiSearch');
    const grid = document.getElementById('emojiGrid');
    const notice = document.getElementById('emojiNotice');

    function render(list) {
        grid.innerHTML = list.map(e => `<button class="text-2xl p-2 bg-slate-800 hover:bg-slate-700 rounded-xl transition active:scale-90" data-char="${e.char}">${e.char}</button>`).join('');
        grid.querySelectorAll('button').forEach(btn => {
            btn.addEventListener('click', () => {
                navigator.clipboard.writeText(btn.dataset.char);
                notice.innerText = `Copied ${btn.dataset.char} to clipboard!`;
                setTimeout(() => notice.innerText = 'Click any emoji to copy to clipboard!', 1500);
            });
        });
    }

    search.addEventListener('input', () => {
        const q = search.value.toLowerCase().trim();
        render(emojis.filter(e => e.name.includes(q) || e.char === q));
    });

    render(emojis);
    