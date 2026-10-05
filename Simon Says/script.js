
    const colors = ['bg-emerald-500', 'bg-rose-500', 'bg-amber-500', 'bg-cyan-500'];
    const darks = ['bg-emerald-700', 'bg-rose-700', 'bg-amber-700', 'bg-cyan-700'];

    let sequence = [];
    let playerStep = 0;

    const pads = document.querySelectorAll('.simon-pad');
    const status = document.getElementById('simonStatus');
    const startBtn = document.getElementById('simonStart');

    function flash(idx) {
        pads[idx].classList.remove(darks[idx]);
        pads[idx].classList.add(colors[idx], 'scale-105');
        setTimeout(() => {
            pads[idx].classList.remove(colors[idx], 'scale-105');
            pads[idx].classList.add(darks[idx]);
        }, 300);
    }

    function playSequence() {
        status.innerText = `Watch sequence (Round ${sequence.length})...`;
        let i = 0;
        const interval = setInterval(() => {
            flash(sequence[i]);
            i++;
            if (i >= sequence.length) {
                clearInterval(interval);
                playerStep = 0;
                status.innerText = 'Your turn!';
            }
        }, 600);
    }

    pads.forEach((pad, idx) => {
        pad.addEventListener('click', () => {
            if (sequence.length === 0) return;
            flash(idx);
            if (idx === sequence[playerStep]) {
                playerStep++;
                if (playerStep === sequence.length) {
                    status.innerText = 'Good job! Next round...';
                    setTimeout(() => {
                        sequence.push(Math.floor(Math.random() * 4));
                        playSequence();
                    }, 1000);
                }
            } else {
                status.innerText = 'Wrong sequence! Game over.';
                sequence = [];
            }
        });
    });

    startBtn.addEventListener('click', () => {
        sequence = [Math.floor(Math.random() * 4)];
        playSequence();
    });
    