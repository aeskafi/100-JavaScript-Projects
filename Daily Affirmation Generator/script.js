
    const affirmations = [
        "I build fast, test rigorously, and deliver real value to the world.",
        "Every bug is simply an invitation to understand the system more deeply.",
        "Freedom and discipline go hand in hand on the nomad engineering journey.",
        "Simplicity is the prerequisite for reliability and speed.",
        "My potential as a creator expands every time I solve a hard challenge."
    ];

    const text = document.getElementById('affText');
    const btn = document.getElementById('nextAff');

    btn.addEventListener('click', () => {
        const quote = affirmations[Math.floor(Math.random() * affirmations.length)];
        text.innerText = `"${quote}"`;
    });
    