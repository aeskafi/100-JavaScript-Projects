import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def create_project(folder_name, title, category, icon, description, html_body, js_code):
    dir_path = os.path.join(BASE_DIR, folder_name)
    os.makedirs(dir_path, exist_ok=True)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | 100 JavaScript Projects</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="min-h-screen bg-slate-900 text-slate-100 flex flex-col justify-center items-center p-4 font-sans">
    <div class="w-full max-w-xl bg-slate-800 border border-slate-700 rounded-3xl shadow-2xl p-6 sm:p-8 backdrop-blur-md">
        <a href="../index.html" class="inline-flex items-center text-xs font-semibold text-cyan-400 hover:text-cyan-300 mb-6 transition-colors">
            ← Back to All Projects
        </a>
        <div class="flex items-center justify-between mb-2">
            <h1 class="text-2xl sm:text-3xl font-bold text-white flex items-center gap-2">
                <span>{icon}</span> {title}
            </h1>
            <span class="text-xs font-semibold px-2.5 py-1 rounded-full bg-slate-700 text-cyan-400 border border-slate-600">
                {category}
            </span>
        </div>
        <p class="text-sm text-slate-400 mb-6">{description}</p>
        {html_body}
    </div>
    <script src="script.js"></script>
</body>
</html>"""
    with open(os.path.join(dir_path, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)
    with open(os.path.join(dir_path, 'script.js'), 'w', encoding='utf-8') as f:
        f.write(js_code)
    print(f"Created {folder_name}")

# 46. Drum Kit
create_project(
    "Drum Kit",
    "Web Audio Drum Kit",
    "Audio & Music",
    "🥁",
    "Synthesized electronic drum pads playable via click or keyboard (A, S, D, F, G, H).",
    """
    <div class="grid grid-cols-3 gap-3">
        <button class="drum-pad bg-slate-950 hover:bg-cyan-600/30 border-2 border-slate-700 hover:border-cyan-400 p-6 rounded-2xl flex flex-col items-center transition active:scale-95" data-key="a" data-freq="80">
            <span class="text-2xl font-black text-cyan-400">A</span>
            <span class="text-xs text-slate-400 mt-1 uppercase font-semibold">Kick</span>
        </button>
        <button class="drum-pad bg-slate-950 hover:bg-cyan-600/30 border-2 border-slate-700 hover:border-cyan-400 p-6 rounded-2xl flex flex-col items-center transition active:scale-95" data-key="s" data-freq="200">
            <span class="text-2xl font-black text-cyan-400">S</span>
            <span class="text-xs text-slate-400 mt-1 uppercase font-semibold">Snare</span>
        </button>
        <button class="drum-pad bg-slate-950 hover:bg-cyan-600/30 border-2 border-slate-700 hover:border-cyan-400 p-6 rounded-2xl flex flex-col items-center transition active:scale-95" data-key="d" data-freq="400">
            <span class="text-2xl font-black text-cyan-400">D</span>
            <span class="text-xs text-slate-400 mt-1 uppercase font-semibold">Hi-Hat</span>
        </button>
        <button class="drum-pad bg-slate-950 hover:bg-cyan-600/30 border-2 border-slate-700 hover:border-cyan-400 p-6 rounded-2xl flex flex-col items-center transition active:scale-95" data-key="f" data-freq="130">
            <span class="text-2xl font-black text-cyan-400">F</span>
            <span class="text-xs text-slate-400 mt-1 uppercase font-semibold">Tom 1</span>
        </button>
        <button class="drum-pad bg-slate-950 hover:bg-cyan-600/30 border-2 border-slate-700 hover:border-cyan-400 p-6 rounded-2xl flex flex-col items-center transition active:scale-95" data-key="g" data-freq="100">
            <span class="text-2xl font-black text-cyan-400">G</span>
            <span class="text-xs text-slate-400 mt-1 uppercase font-semibold">Tom 2</span>
        </button>
        <button class="drum-pad bg-slate-950 hover:bg-cyan-600/30 border-2 border-slate-700 hover:border-cyan-400 p-6 rounded-2xl flex flex-col items-center transition active:scale-95" data-key="h" data-freq="600">
            <span class="text-2xl font-black text-cyan-400">H</span>
            <span class="text-xs text-slate-400 mt-1 uppercase font-semibold">Clap</span>
        </button>
    </div>
    """,
    """
    const ctx = new (window.AudioContext || window.webkitAudioContext)();

    function playDrum(freq) {
        if (ctx.state === 'suspended') ctx.resume();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);

        osc.frequency.setValueAtTime(freq, ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.3);
        gain.gain.setValueAtTime(1, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.3);

        osc.start();
        osc.stop(ctx.currentTime + 0.3);
    }

    document.querySelectorAll('.drum-pad').forEach(pad => {
        pad.addEventListener('click', () => {
            playDrum(parseFloat(pad.dataset.freq));
        });
    });

    window.addEventListener('keydown', (e) => {
        const pad = document.querySelector(`.drum-pad[data-key="${e.key.toLowerCase()}"]`);
        if (pad) {
            pad.click();
            pad.classList.add('scale-95', 'border-cyan-400');
            setTimeout(() => pad.classList.remove('scale-95', 'border-cyan-400'), 150);
        }
    });
    """
)

# 47. Virtual Piano
create_project(
    "Virtual Piano",
    "Virtual Synthesizer Piano",
    "Audio & Music",
    "🎹",
    "Full octave synthesized piano keys (C, D, E, F, G, A, B) with natural decay.",
    """
    <div class="flex justify-center items-end bg-slate-950 p-6 rounded-2xl border border-slate-700 shadow-inner">
        <div class="flex gap-1.5">
            <button class="piano-key w-12 h-40 bg-white hover:bg-slate-200 text-slate-900 rounded-b-xl font-bold flex flex-col justify-end items-center pb-3 text-sm shadow active:scale-95" data-note="261.63">C</button>
            <button class="piano-key w-12 h-40 bg-white hover:bg-slate-200 text-slate-900 rounded-b-xl font-bold flex flex-col justify-end items-center pb-3 text-sm shadow active:scale-95" data-note="293.66">D</button>
            <button class="piano-key w-12 h-40 bg-white hover:bg-slate-200 text-slate-900 rounded-b-xl font-bold flex flex-col justify-end items-center pb-3 text-sm shadow active:scale-95" data-note="329.63">E</button>
            <button class="piano-key w-12 h-40 bg-white hover:bg-slate-200 text-slate-900 rounded-b-xl font-bold flex flex-col justify-end items-center pb-3 text-sm shadow active:scale-95" data-note="349.23">F</button>
            <button class="piano-key w-12 h-40 bg-white hover:bg-slate-200 text-slate-900 rounded-b-xl font-bold flex flex-col justify-end items-center pb-3 text-sm shadow active:scale-95" data-note="392.00">G</button>
            <button class="piano-key w-12 h-40 bg-white hover:bg-slate-200 text-slate-900 rounded-b-xl font-bold flex flex-col justify-end items-center pb-3 text-sm shadow active:scale-95" data-note="440.00">A</button>
            <button class="piano-key w-12 h-40 bg-white hover:bg-slate-200 text-slate-900 rounded-b-xl font-bold flex flex-col justify-end items-center pb-3 text-sm shadow active:scale-95" data-note="493.88">B</button>
        </div>
    </div>
    """,
    """
    const ctx = new (window.AudioContext || window.webkitAudioContext)();

    function playNote(freq) {
        if (ctx.state === 'suspended') ctx.resume();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(freq, ctx.currentTime);

        gain.gain.setValueAtTime(0.5, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 1.2);

        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start();
        osc.stop(ctx.currentTime + 1.2);
    }

    document.querySelectorAll('.piano-key').forEach(key => {
        key.addEventListener('click', () => {
            playNote(parseFloat(key.dataset.note));
        });
    });
    """
)

# 48. Sound Board
create_project(
    "Sound Board",
    "8-Bit Sound Effects Board",
    "Audio & Music",
    "🔊",
    "Generate retro arcade SFX: Coin pickup, laser shot, explosion, power-up, and jump.",
    """
    <div class="grid grid-cols-2 sm:grid-cols-3 gap-3">
        <button class="sfx-btn p-4 bg-slate-950 hover:bg-cyan-600/30 border border-slate-700 rounded-xl text-center transition" data-sfx="coin">
            <span class="text-2xl block mb-1">🪙</span>
            <span class="text-xs font-bold text-white">Coin Pickup</span>
        </button>
        <button class="sfx-btn p-4 bg-slate-950 hover:bg-cyan-600/30 border border-slate-700 rounded-xl text-center transition" data-sfx="laser">
            <span class="text-2xl block mb-1">🔫</span>
            <span class="text-xs font-bold text-white">Laser Shot</span>
        </button>
        <button class="sfx-btn p-4 bg-slate-950 hover:bg-cyan-600/30 border border-slate-700 rounded-xl text-center transition" data-sfx="jump">
            <span class="text-2xl block mb-1">🦘</span>
            <span class="text-xs font-bold text-white">Jump</span>
        </button>
        <button class="sfx-btn p-4 bg-slate-950 hover:bg-cyan-600/30 border border-slate-700 rounded-xl text-center transition" data-sfx="powerup">
            <span class="text-2xl block mb-1">🍄</span>
            <span class="text-xs font-bold text-white">Power Up</span>
        </button>
        <button class="sfx-btn p-4 bg-slate-950 hover:bg-cyan-600/30 border border-slate-700 rounded-xl text-center transition" data-sfx="explode">
            <span class="text-2xl block mb-1">💥</span>
            <span class="text-xs font-bold text-white">Explosion</span>
        </button>
        <button class="sfx-btn p-4 bg-slate-950 hover:bg-cyan-600/30 border border-slate-700 rounded-xl text-center transition" data-sfx="victory">
            <span class="text-2xl block mb-1">🏆</span>
            <span class="text-xs font-bold text-white">Victory</span>
        </button>
    </div>
    """,
    """
    const ctx = new (window.AudioContext || window.webkitAudioContext)();

    function playSfx(type) {
        if (ctx.state === 'suspended') ctx.resume();
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);

        if (type === 'coin') {
            osc.frequency.setValueAtTime(987.77, now);
            osc.frequency.setValueAtTime(1318.51, now + 0.08);
            gain.gain.setValueAtTime(0.3, now);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
            osc.start(now); osc.stop(now + 0.3);
        } else if (type === 'laser') {
            osc.frequency.setValueAtTime(880, now);
            osc.frequency.exponentialRampToValueAtTime(110, now + 0.15);
            gain.gain.setValueAtTime(0.3, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.15);
            osc.start(now); osc.stop(now + 0.15);
        } else if (type === 'jump') {
            osc.frequency.setValueAtTime(150, now);
            osc.frequency.exponentialRampToValueAtTime(600, now + 0.15);
            gain.gain.setValueAtTime(0.3, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.15);
            osc.start(now); osc.stop(now + 0.15);
        } else if (type === 'powerup') {
            osc.frequency.setValueAtTime(300, now);
            osc.frequency.linearRampToValueAtTime(800, now + 0.3);
            gain.gain.setValueAtTime(0.3, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);
            osc.start(now); osc.stop(now + 0.3);
        } else if (type === 'explode') {
            osc.type = 'sawtooth';
            osc.frequency.setValueAtTime(120, now);
            osc.frequency.exponentialRampToValueAtTime(20, now + 0.4);
            gain.gain.setValueAtTime(0.5, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.4);
            osc.start(now); osc.stop(now + 0.4);
        } else if (type === 'victory') {
            [440, 554, 659, 880].forEach((f, idx) => {
                const o = ctx.createOscillator();
                const g = ctx.createGain();
                o.connect(g); g.connect(ctx.destination);
                o.frequency.value = f;
                g.gain.setValueAtTime(0.2, now + idx * 0.1);
                g.gain.exponentialRampToValueAtTime(0.01, now + idx * 0.1 + 0.2);
                o.start(now + idx * 0.1);
                o.stop(now + idx * 0.1 + 0.2);
            });
        }
    }

    document.querySelectorAll('.sfx-btn').forEach(btn => {
        btn.addEventListener('click', () => playSfx(btn.dataset.sfx));
    });
    """
)

# 49. Metronome
create_project(
    "Metronome",
    "Digital Metronome",
    "Audio & Music",
    "⏱️",
    "Adjustable BPM metronome with visual pendulum beat flashes.",
    """
    <div class="space-y-6 text-center">
        <div class="flex items-center justify-center">
            <div id="metroIndicator" class="w-16 h-16 rounded-full bg-slate-900 border-4 border-slate-700 flex items-center justify-center transition-all duration-75">
                <span class="w-4 h-4 rounded-full bg-cyan-400"></span>
            </div>
        </div>
        <div>
            <div class="text-4xl font-black text-cyan-400 font-mono mb-2"><span id="bpmVal">120</span> BPM</div>
            <input type="range" id="bpmRange" min="40" max="220" value="120" class="w-full accent-cyan-500 cursor-pointer" />
        </div>
        <button id="metroToggle" class="px-8 py-3 bg-cyan-600 hover:bg-cyan-500 text-white font-bold rounded-xl text-sm transition">
            Start Metronome
        </button>
    </div>
    """,
    """
    const ctx = new (window.AudioContext || window.webkitAudioContext)();
    let isRunning = false;
    let timer = null;

    const bpmRange = document.getElementById('bpmRange');
    const bpmVal = document.getElementById('bpmVal');
    const toggleBtn = document.getElementById('metroToggle');
    const indicator = document.getElementById('metroIndicator');

    function clickSound() {
        if (ctx.state === 'suspended') ctx.resume();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.frequency.setValueAtTime(1000, ctx.currentTime);
        gain.gain.setValueAtTime(0.5, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.05);
        osc.start();
        osc.stop(ctx.currentTime + 0.05);

        indicator.classList.add('scale-125', 'border-cyan-400');
        setTimeout(() => indicator.classList.remove('scale-125', 'border-cyan-400'), 80);
    }

    bpmRange.addEventListener('input', () => {
        bpmVal.innerText = bpmRange.value;
        if (isRunning) {
            clearInterval(timer);
            timer = setInterval(clickSound, (60 / parseInt(bpmRange.value)) * 1000);
        }
    });

    toggleBtn.addEventListener('click', () => {
        if (!isRunning) {
            isRunning = true;
            toggleBtn.innerText = 'Stop Metronome';
            toggleBtn.className = 'px-8 py-3 bg-rose-600 hover:bg-rose-500 text-white font-bold rounded-xl text-sm transition';
            clickSound();
            timer = setInterval(clickSound, (60 / parseInt(bpmRange.value)) * 1000);
        } else {
            isRunning = false;
            clearInterval(timer);
            toggleBtn.innerText = 'Start Metronome';
            toggleBtn.className = 'px-8 py-3 bg-cyan-600 hover:bg-cyan-500 text-white font-bold rounded-xl text-sm transition';
        }
    });
    """
)

# 50. White Noise Generator
create_project(
    "White Noise Generator",
    "Focus White Noise Generator",
    "Audio & Music",
    "🌊",
    "Synthesized ambient white and pink noise for deep focus and sound masking.",
    """
    <div class="space-y-6 text-center">
        <p class="text-xs text-slate-400">Pure client-side audio buffer synthesis with zero external audio assets.</p>
        <div class="flex justify-center gap-4 text-xs text-slate-300">
            <span>Volume</span>
            <input type="range" id="noiseVol" min="0" max="1" step="0.05" value="0.2" class="accent-cyan-500 cursor-pointer" />
        </div>
        <button id="noiseToggle" class="px-8 py-3 bg-cyan-600 hover:bg-cyan-500 text-white font-bold rounded-xl text-sm transition">
            ▶ Play White Noise
        </button>
    </div>
    """,
    """
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
    """
)

# 51. Canvas Drawing Board
create_project(
    "Canvas Drawing Board",
    "Interactive Canvas Sketchpad",
    "Canvas & Graphics",
    "🎨",
    "Freehand HTML5 canvas drawing pad with color picker, line thickness, and image export.",
    """
    <div class="space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2">
            <div class="flex items-center gap-2">
                <input type="color" id="drawColor" value="#06b6d4" class="w-8 h-8 rounded-lg bg-transparent cursor-pointer" />
                <input type="range" id="drawSize" min="1" max="25" value="4" class="w-24 accent-cyan-500" />
            </div>
            <div class="flex gap-2">
                <button id="clearCanvas" class="px-3 py-1.5 bg-slate-700 hover:bg-rose-600 text-white rounded-xl text-xs font-bold transition">Clear</button>
                <button id="saveCanvas" class="px-3 py-1.5 bg-cyan-600 hover:bg-cyan-500 text-white rounded-xl text-xs font-bold transition">Save PNG</button>
            </div>
        </div>
        <canvas id="paintCanvas" width="500" height="320" class="w-full bg-slate-950 border border-slate-700 rounded-2xl cursor-crosshair touch-none"></canvas>
    </div>
    """,
    """
    const canvas = document.getElementById('paintCanvas');
    const ctx = canvas.getContext('2d');
    const color = document.getElementById('drawColor');
    const size = document.getElementById('drawSize');

    let painting = false;

    function start(e) {
        painting = true;
        draw(e);
    }
    function end() {
        painting = false;
        ctx.beginPath();
    }
    function draw(e) {
        if (!painting) return;
        const rect = canvas.getBoundingClientRect();
        const scaleX = canvas.width / rect.width;
        const scaleY = canvas.height / rect.height;
        const clientX = e.clientX || (e.touches && e.touches[0].clientX);
        const clientY = e.clientY || (e.touches && e.touches[0].clientY);

        ctx.lineWidth = size.value;
        ctx.lineCap = 'round';
        ctx.strokeStyle = color.value;

        ctx.lineTo((clientX - rect.left) * scaleX, (clientY - rect.top) * scaleY);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo((clientX - rect.left) * scaleX, (clientY - rect.top) * scaleY);
    }

    canvas.addEventListener('mousedown', start);
    canvas.addEventListener('mouseup', end);
    canvas.addEventListener('mousemove', draw);
    canvas.addEventListener('touchstart', (e) => { e.preventDefault(); start(e); });
    canvas.addEventListener('touchend', end);
    canvas.addEventListener('touchmove', (e) => { e.preventDefault(); draw(e); });

    document.getElementById('clearCanvas').addEventListener('click', () => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    });

    document.getElementById('saveCanvas').addEventListener('click', () => {
        const link = document.createElement('a');
        link.download = 'sketch.png';
        link.href = canvas.toDataURL();
        link.click();
    });
    """
)

# 52. Color Palette Generator
create_project(
    "Color Palette Generator",
    "Color Palette Generator",
    "Canvas & Graphics",
    "🎨",
    "Generate harmonious 5-color palettes with hex codes and spacebar generation.",
    """
    <div class="space-y-4">
        <div id="paletteBox" class="grid grid-cols-5 h-36 rounded-2xl overflow-hidden border border-slate-700"></div>
        <div class="flex justify-between items-center">
            <span class="text-xs text-slate-400">Click a color to copy Hex code!</span>
            <button id="genPalette" class="px-5 py-2.5 bg-cyan-600 hover:bg-cyan-500 text-white font-bold rounded-xl text-xs transition">
                Generate Palette (Spacebar)
            </button>
        </div>
    </div>
    """,
    """
    const box = document.getElementById('paletteBox');
    const genBtn = document.getElementById('genPalette');

    function getRandomColor() {
        const letters = '0123456789ABCDEF';
        let color = '#';
        for (let i = 0; i < 6; i++) color += letters[Math.floor(Math.random() * 16)];
        return color;
    }

    function render() {
        box.innerHTML = '';
        for (let i = 0; i < 5; i++) {
            const hex = getRandomColor();
            const div = document.createElement('div');
            div.style.backgroundColor = hex;
            div.className = 'h-full flex items-end justify-center p-2 cursor-pointer transition hover:opacity-90 active:scale-95';
            div.innerHTML = `<span class="bg-black/60 px-2 py-1 rounded text-white text-xs font-mono font-bold">${hex}</span>`;
            div.addEventListener('click', () => {
                navigator.clipboard.writeText(hex);
                div.querySelector('span').innerText = 'Copied!';
                setTimeout(() => div.querySelector('span').innerText = hex, 1000);
            });
            box.appendChild(div);
        }
    }

    genBtn.addEventListener('click', render);
    window.addEventListener('keydown', (e) => {
        if (e.code === 'Space' && e.target === document.body) {
            e.preventDefault();
            render();
        }
    });

    render();
    """
)

# 53. Gradient Generator
create_project(
    "Gradient Generator",
    "CSS Linear Gradient Generator",
    "Canvas & Graphics",
    "🌈",
    "Craft multi-stop CSS gradients with real-time CSS code export.",
    """
    <div class="space-y-4">
        <div id="gradPreview" class="h-32 rounded-2xl border border-slate-700 shadow-inner"></div>
        <div class="grid grid-cols-3 gap-3">
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Color 1</label>
                <input type="color" id="gradC1" value="#06b6d4" class="w-full h-10 rounded-xl bg-transparent cursor-pointer" />
            </div>
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Color 2</label>
                <input type="color" id="gradC2" value="#3b82f6" class="w-full h-10 rounded-xl bg-transparent cursor-pointer" />
            </div>
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Angle (<span id="angVal">90</span>°)</label>
                <input type="range" id="gradAngle" min="0" max="360" value="90" class="w-full accent-cyan-500 mt-2 cursor-pointer" />
            </div>
        </div>
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">CSS Output</label>
            <input type="text" id="gradCss" readonly class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-cyan-400 font-mono text-xs outline-none" />
        </div>
    </div>
    """,
    """
    const preview = document.getElementById('gradPreview');
    const c1 = document.getElementById('gradC1');
    const c2 = document.getElementById('gradC2');
    const angle = document.getElementById('gradAngle');
    const angVal = document.getElementById('angVal');
    const css = document.getElementById('gradCss');

    function update() {
        angVal.innerText = angle.value;
        const code = `linear-gradient(${angle.value}deg, ${c1.value}, ${c2.value})`;
        preview.style.background = code;
        css.value = `background: ${code};`;
    }

    [c1, c2, angle].forEach(el => el.addEventListener('input', update));
    update();
    """
)

# 54. QR Code Generator
create_project(
    "QR Code Generator",
    "Dynamic QR Code Generator",
    "Utilities",
    "📱",
    "Generate scannable QR matrix codes instantly via SVG vector generation.",
    """
    <div class="space-y-4 text-center">
        <input type="text" id="qrText" value="https://arham.dev" placeholder="Enter text or URL..." class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white text-sm outline-none" />
        <div class="flex justify-center p-4 bg-white rounded-2xl max-w-[200px] mx-auto shadow-xl">
            <img id="qrImg" src="https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=https://arham.dev" alt="QR" class="w-40 h-40" />
        </div>
    </div>
    """,
    """
    const input = document.getElementById('qrText');
    const img = document.getElementById('qrImg');

    input.addEventListener('input', () => {
        const val = encodeURIComponent(input.value || 'https://arham.dev');
        img.src = `https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=${val}`;
    });
    """
)

# 55. ASCII Art Generator
create_project(
    "ASCII Art Generator",
    "ASCII Banner Art Generator",
    "Text & Graphics",
    "🔤",
    "Transform standard text into retro monospaced terminal banner typography.",
    """
    <div class="space-y-4">
        <input type="text" id="asciiInput" value="ARHAM" maxlength="8" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-white font-mono text-sm uppercase outline-none" />
        <pre id="asciiOutput" class="bg-slate-950 border border-slate-700 rounded-2xl p-4 text-cyan-400 font-mono text-xs overflow-x-auto leading-none"></pre>
    </div>
    """,
    """
    const font = {
        'A': ["  █  ", " █ █ ", "█████", "█   █"],
        'B': ["████ ", "████ ", "█   █", "████ "],
        'C': [" ████", "█    ", "█    ", " ████"],
        'D': ["████ ", "█   █", "█   █", "████ "],
        'E': ["█████", "████ ", "█    ", "█████"],
        'F': ["█████", "████ ", "█    ", "█    "],
        'G': [" ████", "█    ", "█  ██", " ████"],
        'H': ["█   █", "█████", "█   █", "█   █"],
        'I': ["█████", "  █  ", "  █  ", "█████"],
        'J': ["   ██", "    █", "█   █", " ███ "],
        'K': ["█  █ ", "███  ", "█  █ ", "█   █"],
        'L': ["█    ", "█    ", "█    ", "█████"],
        'M': ["█   █", "██ ██", "█ █ █", "█   █"],
        'N': ["█   █", "██  █", "█ █ █", "█  ██"],
        'O': [" ███ ", "█   █", "█   █", " ███ "],
        'P': ["████ ", "█   █", "████ ", "█    "],
        'R': ["████ ", "█   █", "████ ", "█  █ "],
        'S': [" ████", "████ ", "   ██", "████ "],
        'T': ["█████", "  █  ", "  █  ", "  █  "],
        'U': ["█   █", "█   █", "█   █", " ███ "],
        'V': ["█   █", "█   █", " █ █ ", "  █  "],
        'W': ["█   █", "█ █ █", "██ ██", "█   █"],
        'X': ["█   █", "  █  ", " █ █ ", "█   █"],
        'Y': ["█   █", " █ █ ", "  █  ", "  █  "],
        'Z': ["█████", "   █ ", "  █  ", "█████"],
        ' ': ["     ", "     ", "     ", "     "]
    };

    const input = document.getElementById('asciiInput');
    const out = document.getElementById('asciiOutput');

    function render() {
        const text = input.value.toUpperCase();
        let lines = ["", "", "", ""];
        for (let char of text) {
            const glyph = font[char] || font[' '];
            for (let i = 0; i < 4; i++) {
                lines[i] += glyph[i] + " ";
            }
        }
        out.innerText = lines.join('\\n');
    }

    input.addEventListener('input', render);
    render();
    """
)

# 56. Pixel Art Studio
create_project(
    "Pixel Art Studio",
    "16x16 Pixel Art Studio",
    "Canvas & Graphics",
    "👾",
    "Paint retro 16x16 sprites with multi-color palette and eraser support.",
    """
    <div class="space-y-4">
        <div class="flex justify-between items-center">
            <div class="flex items-center gap-2">
                <input type="color" id="pixelColor" value="#10b981" class="w-8 h-8 rounded-lg bg-transparent cursor-pointer" />
                <button id="pixelEraser" class="px-3 py-1 bg-slate-700 hover:bg-slate-600 rounded-xl text-xs font-bold text-slate-300">Eraser</button>
            </div>
            <button id="pixelClear" class="px-3 py-1 bg-rose-600 hover:bg-rose-500 rounded-xl text-xs font-bold text-white">Reset Grid</button>
        </div>
        <div id="pixelGrid" class="grid grid-cols-16 gap-px bg-slate-950 p-2 border border-slate-700 rounded-2xl max-w-[280px] mx-auto"></div>
    </div>
    """,
    """
    const grid = document.getElementById('pixelGrid');
    const colorPicker = document.getElementById('pixelColor');
    const eraser = document.getElementById('pixelEraser');
    const clearBtn = document.getElementById('pixelClear');

    let isErasing = false;
    let isDrawing = false;

    grid.style.gridTemplateColumns = 'repeat(16, minmax(0, 1fr))';

    for (let i = 0; i < 256; i++) {
        const cell = document.createElement('div');
        cell.className = 'w-4 h-4 bg-slate-900 cursor-pointer hover:opacity-80 transition';
        cell.addEventListener('mousedown', () => {
            cell.style.backgroundColor = isErasing ? '#0f172a' : colorPicker.value;
        });
        cell.addEventListener('mouseover', () => {
            if (isDrawing) cell.style.backgroundColor = isErasing ? '#0f172a' : colorPicker.value;
        });
        grid.appendChild(cell);
    }

    window.addEventListener('mousedown', () => isDrawing = true);
    window.addEventListener('mouseup', () => isDrawing = false);

    eraser.addEventListener('click', () => {
        isErasing = !isErasing;
        eraser.className = isErasing ? 'px-3 py-1 bg-cyan-600 rounded-xl text-xs font-bold text-white' : 'px-3 py-1 bg-slate-700 rounded-xl text-xs font-bold text-slate-300';
    });

    clearBtn.addEventListener('click', () => {
        grid.querySelectorAll('div').forEach(c => c.style.backgroundColor = '#0f172a');
    });
    """
)

# 57. Meme Generator
create_project(
    "Meme Generator",
    "Quick Meme Generator",
    "Canvas & Graphics",
    "🖼️",
    "Canvas meme maker with customizable top and bottom bold impact typography.",
    """
    <div class="space-y-4">
        <div class="grid grid-cols-2 gap-2">
            <input type="text" id="memeTop" placeholder="TOP TEXT" class="bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-white font-bold text-xs uppercase outline-none" />
            <input type="text" id="memeBot" placeholder="BOTTOM TEXT" class="bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-white font-bold text-xs uppercase outline-none" />
        </div>
        <canvas id="memeCanvas" width="400" height="260" class="w-full bg-slate-950 border border-slate-700 rounded-2xl"></canvas>
    </div>
    """,
    """
    const canvas = document.getElementById('memeCanvas');
    const ctx = canvas.getContext('2d');
    const topInp = document.getElementById('memeTop');
    const botInp = document.getElementById('memeBot');

    function drawMeme() {
        ctx.fillStyle = '#1e293b';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.fillStyle = '#0f172a';
        ctx.fillRect(20, 20, canvas.width - 40, canvas.height - 40);

        ctx.font = 'bold 24px Impact, sans-serif';
        ctx.fillStyle = 'white';
        ctx.strokeStyle = 'black';
        ctx.lineWidth = 3;
        ctx.textAlign = 'center';

        const top = topInp.value.toUpperCase() || 'WHEN YOU AUDIT REPOS';
        const bot = botInp.value.toUpperCase() || 'AND SHIP 100 APPS IN ONE GO';

        ctx.strokeText(top, canvas.width / 2, 60);
        ctx.fillText(top, canvas.width / 2, 60);

        ctx.strokeText(bot, canvas.width / 2, canvas.height - 40);
        ctx.fillText(bot, canvas.width / 2, canvas.height - 40);
    }

    topInp.addEventListener('input', drawMeme);
    botInp.addEventListener('input', drawMeme);
    drawMeme();
    """
)

# 58. Particle Visualizer
create_project(
    "Particle Visualizer",
    "Interactive Particle Field",
    "Canvas & Graphics",
    "✨",
    "Physics particle simulation with mouse gravity attractor and velocity trails.",
    """
    <div class="space-y-4">
        <canvas id="partCanvas" width="500" height="300" class="w-full bg-slate-950 border border-slate-700 rounded-2xl"></canvas>
        <p class="text-xs text-center text-slate-400">Move your mouse across the canvas to attract cosmic particles.</p>
    </div>
    """,
    """
    const canvas = document.getElementById('partCanvas');
    const ctx = canvas.getContext('2d');

    const particles = [];
    for (let i = 0; i < 60; i++) {
        particles.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            vx: (Math.random() - 0.5) * 2,
            vy: (Math.random() - 0.5) * 2,
            radius: Math.random() * 2 + 1
        });
    }

    let mouse = { x: canvas.width / 2, y: canvas.height / 2 };
    canvas.addEventListener('mousemove', (e) => {
        const r = canvas.getBoundingClientRect();
        mouse.x = (e.clientX - r.left) * (canvas.width / r.width);
        mouse.y = (e.clientY - r.top) * (canvas.height / r.height);
    });

    function loop() {
        ctx.fillStyle = 'rgba(15, 23, 42, 0.2)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        particles.forEach(p => {
            p.x += p.vx;
            p.y += p.vy;
            if (p.x < 0 || p.x > canvas.width) p.vx *= -1;
            if (p.y < 0 || p.y > canvas.height) p.vy *= -1;

            const dx = mouse.x - p.x;
            const dy = mouse.y - p.y;
            const dist = Math.sqrt(dx * dx + dy * dy);
            if (dist < 100) {
                p.x += dx * 0.02;
                p.y += dy * 0.02;
            }

            ctx.beginPath();
            ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
            ctx.fillStyle = '#06b6d4';
            ctx.fill();
        });

        requestAnimationFrame(loop);
    }
    loop();
    """
)

# 59. Canvas Fireworks
create_project(
    "Canvas Fireworks",
    "Canvas Celebration Fireworks",
    "Canvas & Graphics",
    "🎆",
    "Sparkling fireworks particle explosion simulator with physics gravity.",
    """
    <div class="space-y-4 text-center">
        <canvas id="fireCanvas" width="500" height="300" class="w-full bg-slate-950 border border-slate-700 rounded-2xl cursor-pointer"></canvas>
        <p class="text-xs text-slate-400">Click anywhere inside the canvas to launch firework bursts!</p>
    </div>
    """,
    """
    const canvas = document.getElementById('fireCanvas');
    const ctx = canvas.getContext('2d');
    let sparks = [];

    function createBurst(x, y) {
        const colors = ['#06b6d4', '#f59e0b', '#ec4899', '#10b981', '#a855f7'];
        const col = colors[Math.floor(Math.random() * colors.length)];
        for (let i = 0; i < 40; i++) {
            const angle = Math.random() * Math.PI * 2;
            const speed = Math.random() * 5 + 1;
            sparks.push({
                x, y,
                vx: Math.cos(angle) * speed,
                vy: Math.sin(angle) * speed,
                alpha: 1,
                color: col
            });
        }
    }

    canvas.addEventListener('click', (e) => {
        const r = canvas.getBoundingClientRect();
        createBurst((e.clientX - r.left) * (canvas.width / r.width), (e.clientY - r.top) * (canvas.height / r.height));
    });

    function loop() {
        ctx.fillStyle = 'rgba(15, 23, 42, 0.25)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        for (let i = sparks.length - 1; i >= 0; i--) {
            const s = sparks[i];
            s.x += s.vx;
            s.y += s.vy;
            s.vy += 0.05; // gravity
            s.alpha -= 0.02;

            if (s.alpha <= 0) {
                sparks.splice(i, 1);
                continue;
            }

            ctx.save();
            ctx.globalAlpha = s.alpha;
            ctx.fillStyle = s.color;
            ctx.fillRect(s.x, s.y, 3, 3);
            ctx.restore();
        }

        requestAnimationFrame(loop);
    }
    createBurst(canvas.width / 2, canvas.height / 3);
    loop();
    """
)

# 60. Audio Frequency Visualizer
create_project(
    "Audio Frequency Visualizer",
    "Audio Spectrum Visualizer",
    "Audio & Canvas",
    "📊",
    "Simulated frequency bars dancing to procedural synth audio waves.",
    """
    <div class="space-y-4 text-center">
        <canvas id="specCanvas" width="500" height="200" class="w-full bg-slate-950 border border-slate-700 rounded-2xl"></canvas>
        <button id="specToggle" class="px-6 py-2.5 bg-cyan-600 hover:bg-cyan-500 text-white font-bold rounded-xl text-xs transition">
            ▶ Toggle Visualizer Sound
        </button>
    </div>
    """,
    """
    const canvas = document.getElementById('specCanvas');
    const ctx = canvas.getContext('2d');
    const toggle = document.getElementById('specToggle');

    let audioCtx = null;
    let osc = null;
    let isPlaying = false;

    function renderBars() {
        ctx.fillStyle = '#0f172a';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        const bars = 24;
        const width = canvas.width / bars;

        for (let i = 0; i < bars; i++) {
            const h = isPlaying ? (Math.sin(Date.now() / 200 + i) * 0.5 + 0.5) * (canvas.height - 20) + 10 : 8;
            ctx.fillStyle = '#06b6d4';
            ctx.fillRect(i * width + 2, canvas.height - h, width - 4, h);
        }

        requestAnimationFrame(renderBars);
    }

    toggle.addEventListener('click', () => {
        if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        if (!isPlaying) {
            osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            osc.frequency.setValueAtTime(220, audioCtx.currentTime);
            gain.gain.setValueAtTime(0.05, audioCtx.currentTime);
            osc.connect(gain);
            gain.connect(audioCtx.destination);
            osc.start();
            isPlaying = true;
            toggle.innerText = '⏹ Stop Visualizer Sound';
        } else {
            osc.stop();
            isPlaying = false;
            toggle.innerText = '▶ Toggle Visualizer Sound';
        }
    });

    renderBars();
    """
)
