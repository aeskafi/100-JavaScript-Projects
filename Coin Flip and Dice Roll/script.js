
    const coin = document.getElementById('coinFace');
    const dice = document.getElementById('diceFace');
    const diceIcons = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅'];

    document.getElementById('flipCoin').addEventListener('click', () => {
        coin.classList.add('rotate-180');
        setTimeout(() => {
            const isHeads = Math.random() < 0.5;
            coin.innerText = isHeads ? 'HEADS' : 'TAILS';
            coin.classList.remove('rotate-180');
        }, 150);
    });

    document.getElementById('rollDice').addEventListener('click', () => {
        dice.classList.add('scale-90');
        setTimeout(() => {
            dice.innerText = diceIcons[Math.floor(Math.random() * 6)];
            dice.classList.remove('scale-90');
        }, 150);
    });
    