
    const ctx = new (window.AudioContext || window.webkitAudioContext)();
    let noiseNode = null;
    let gainNode = null;
    let isPlaying = false;

    const toggle = document.getElementById('noiseToggle');
    const vol = document.getElementById('noiseVol');

    function createWhiteNoise() {
        const bufferSize = 2 * ctx.sampleRate;
        const noiseBuffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
        const output = noiseBuffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) {
            output[i] = Math.random() * 2 - 1;
        }
        const whiteNoise = ctx.createBufferSource();
        whiteNoise.buffer = noiseBuffer;
        whiteNoise.loop = true;

        gainNode = ctx.createGain();
        gainNode.gain.setValueAtTime(parseFloat(vol.value), ctx.currentTime);

        whiteNoise.connect(gainNode);
        gainNode.connect(ctx.destination);
        return whiteNoise;
    }

    vol.addEventListener('input', () => {
        if (gainNode) gainNode.gain.setValueAtTime(parseFloat(vol.value), ctx.currentTime);
    });

    toggle.addEventListener('click', () => {
        if (ctx.state === 'suspended') ctx.resume();
        if (!isPlaying) {
            noiseNode = createWhiteNoise();
            noiseNode.start();
            isPlaying = true;
            toggle.innerText = '⏹ Stop White Noise';
            toggle.className = 'px-8 py-3 bg-rose-600 hover:bg-rose-500 text-white font-bold rounded-xl text-sm transition';
        } else {
            noiseNode.stop();
            isPlaying = false;
            toggle.innerText = '▶ Play White Noise';
            toggle.className = 'px-8 py-3 bg-cyan-600 hover:bg-cyan-500 text-white font-bold rounded-xl text-sm transition';
        }
    });
    