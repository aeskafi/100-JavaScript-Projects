
    let arr = [];
    const container = document.getElementById('sortBars');

    function randomize() {
        arr = [];
        for (let i = 0; i < 20; i++) arr.push(Math.floor(Math.random() * 90) + 10);
        render();
    }

    function render(highlightIdx = -1) {
        container.innerHTML = '';
        arr.forEach((val, i) => {
            const bar = document.createElement('div');
            bar.style.height = `${val}%`;
            bar.className = 'w-3 rounded-t transition-all ' + (i === highlightIdx ? 'bg-amber-400' : 'bg-cyan-500');
            container.appendChild(bar);
        });
    }

    async function bubbleSort() {
        for (let i = 0; i < arr.length; i++) {
            for (let j = 0; j < arr.length - i - 1; j++) {
                render(j);
                await new Promise(r => setTimeout(r, 40));
                if (arr[j] > arr[j + 1]) {
                    [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
                    render(j + 1);
                }
            }
        }
        render();
    }

    document.getElementById('sortRandom').addEventListener('click', randomize);
    document.getElementById('sortStart').addEventListener('click', bubbleSort);
    randomize();
    