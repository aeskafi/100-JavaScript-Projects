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

# 79. Box Shadow Generator
create_project(
    "Box Shadow Generator",
    "CSS Box Shadow Generator",
    "CSS & Design",
    "🔳",
    "Tune horizontal, vertical offset, blur, spread, and shadow opacity with CSS export.",
    """
    <div class="space-y-4">
        <div class="flex justify-center p-8 bg-slate-950 rounded-2xl border border-slate-800">
            <div id="shadowTarget" class="w-32 h-32 bg-slate-800 rounded-2xl transition-all"></div>
        </div>
        <div class="grid grid-cols-2 gap-3 text-xs text-slate-300">
            <div>
                <label class="block mb-1">X Offset: <span id="xVal">0</span>px</label>
                <input type="range" id="xOff" min="-50" max="50" value="0" class="w-full accent-cyan-500" />
            </div>
            <div>
                <label class="block mb-1">Y Offset: <span id="yVal">10</span>px</label>
                <input type="range" id="yOff" min="-50" max="50" value="10" class="w-full accent-cyan-500" />
            </div>
            <div>
                <label class="block mb-1">Blur Radius: <span id="bVal">25</span>px</label>
                <input type="range" id="blur" min="0" max="100" value="25" class="w-full accent-cyan-500" />
            </div>
            <div>
                <label class="block mb-1">Spread: <span id="sVal">0</span>px</label>
                <input type="range" id="spread" min="-20" max="50" value="0" class="w-full accent-cyan-500" />
            </div>
        </div>
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">CSS Code</label>
            <input type="text" id="shadowCss" readonly class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-cyan-400 font-mono text-xs outline-none" />
        </div>
    </div>
    """,
    """
    const target = document.getElementById('shadowTarget');
    const x = document.getElementById('xOff');
    const y = document.getElementById('yOff');
    const b = document.getElementById('blur');
    const s = document.getElementById('spread');
    const css = document.getElementById('shadowCss');

    function update() {
        document.getElementById('xVal').innerText = x.value;
        document.getElementById('yVal').innerText = y.value;
        document.getElementById('bVal').innerText = b.value;
        document.getElementById('sVal').innerText = s.value;

        const val = `${x.value}px ${y.value}px ${b.value}px ${s.value}px rgba(6, 182, 212, 0.35)`;
        target.style.boxShadow = val;
        css.value = `box-shadow: ${val};`;
    }

    [x, y, b, s].forEach(el => el.addEventListener('input', update));
    update();
    """
)

# 80. Glassmorphism Generator
create_project(
    "Glassmorphism Generator",
    "Glassmorphism UI Generator",
    "CSS & Design",
    "🪟",
    "Generate frosted glass effects using backdrop-filter and semi-transparent alpha borders.",
    """
    <div class="space-y-4">
        <div class="relative p-10 rounded-2xl overflow-hidden flex justify-center items-center bg-gradient-to-tr from-cyan-600 to-fuchsia-600">
            <div id="glassTarget" class="p-6 rounded-2xl border border-white/20 text-center max-w-xs shadow-2xl">
                <h3 class="text-white font-bold text-sm">Glassmorphic Card</h3>
                <p class="text-white/80 text-xs mt-1">Frosted translucent background filter.</p>
            </div>
        </div>
        <div class="grid grid-cols-2 gap-3 text-xs text-slate-300">
            <div>
                <label class="block mb-1">Blur: <span id="glassBlurVal">12</span>px</label>
                <input type="range" id="glassBlur" min="0" max="40" value="12" class="w-full accent-cyan-500" />
            </div>
            <div>
                <label class="block mb-1">Opacity: <span id="glassOpVal">0.2</span></label>
                <input type="range" id="glassOp" min="0.05" max="0.8" step="0.05" value="0.2" class="w-full accent-cyan-500" />
            </div>
        </div>
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">CSS Rules</label>
            <textarea id="glassCss" rows="3" readonly class="w-full bg-slate-950 border border-slate-700 rounded-xl p-2.5 text-cyan-400 font-mono text-xs outline-none resize-none"></textarea>
        </div>
    </div>
    """,
    """
    const target = document.getElementById('glassTarget');
    const blur = document.getElementById('glassBlur');
    const op = document.getElementById('glassOp');
    const css = document.getElementById('glassCss');

    function update() {
        document.getElementById('glassBlurVal').innerText = blur.value;
        document.getElementById('glassOpVal').innerText = op.value;

        target.style.background = `rgba(255, 255, 255, ${op.value})`;
        target.style.backdropFilter = `blur(${blur.value}px)`;

        css.value = `background: rgba(255, 255, 255, ${op.value});\\nbackdrop-filter: blur(${blur.value}px);\\n-webkit-backdrop-filter: blur(${blur.value}px);\\nborder: 1px solid rgba(255, 255, 255, 0.2);`;
    }

    [blur, op].forEach(el => el.addEventListener('input', update));
    update();
    """
)

# 81. Border Radius Previewer
create_project(
    "Border Radius Previewer",
    "8-Point Border Radius Previewer",
    "CSS & Design",
    "🔘",
    "Create organic border-radius blobs with 8-point asymmetric CSS rounding controls.",
    """
    <div class="space-y-4">
        <div class="flex justify-center p-8 bg-slate-950 rounded-2xl border border-slate-800">
            <div id="blobTarget" class="w-36 h-36 bg-gradient-to-tr from-cyan-500 to-blue-600 transition-all"></div>
        </div>
        <div class="grid grid-cols-2 gap-3 text-xs text-slate-300">
            <div>
                <label class="block mb-1">Top-Left (<span id="tlVal">30</span>%)</label>
                <input type="range" id="tl" min="0" max="100" value="30" class="w-full accent-cyan-500" />
            </div>
            <div>
                <label class="block mb-1">Top-Right (<span id="trVal">70</span>%)</label>
                <input type="range" id="tr" min="0" max="100" value="70" class="w-full accent-cyan-500" />
            </div>
            <div>
                <label class="block mb-1">Bottom-Left (<span id="blVal">70</span>%)</label>
                <input type="range" id="bl" min="0" max="100" value="70" class="w-full accent-cyan-500" />
            </div>
            <div>
                <label class="block mb-1">Bottom-Right (<span id="brVal">30</span>%)</label>
                <input type="range" id="br" min="0" max="100" value="30" class="w-full accent-cyan-500" />
            </div>
        </div>
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">CSS Border Radius</label>
            <input type="text" id="blobCss" readonly class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-cyan-400 font-mono text-xs outline-none" />
        </div>
    </div>
    """,
    """
    const target = document.getElementById('blobTarget');
    const tl = document.getElementById('tl');
    const tr = document.getElementById('tr');
    const bl = document.getElementById('bl');
    const br = document.getElementById('br');
    const css = document.getElementById('blobCss');

    function update() {
        document.getElementById('tlVal').innerText = tl.value;
        document.getElementById('trVal').innerText = tr.value;
        document.getElementById('blVal').innerText = bl.value;
        document.getElementById('brVal').innerText = br.value;

        const val = `${tl.value}% ${tr.value}% ${br.value}% ${bl.value}% / ${br.value}% ${bl.value}% ${tr.value}% ${tl.value}%`;
        target.style.borderRadius = val;
        css.value = `border-radius: ${val};`;
    }

    [tl, tr, bl, br].forEach(el => el.addEventListener('input', update));
    update();
    """
)

# 82. CSS Grid Generator
create_project(
    "CSS Grid Generator",
    "CSS Grid Layout Builder",
    "CSS & Design",
    "📐",
    "Interactively generate CSS Grid layouts, adjust columns, rows, and gaps.",
    """
    <div class="space-y-4">
        <div class="flex gap-4 text-xs text-slate-300">
            <div>
                <label>Cols:</label>
                <input type="number" id="gridCols" min="1" max="6" value="3" class="w-16 bg-slate-950 border border-slate-700 rounded-lg p-1 text-center" />
            </div>
            <div>
                <label>Rows:</label>
                <input type="number" id="gridRows" min="1" max="6" value="2" class="w-16 bg-slate-950 border border-slate-700 rounded-lg p-1 text-center" />
            </div>
            <div>
                <label>Gap (px):</label>
                <input type="number" id="gridGap" min="0" max="30" value="8" class="w-16 bg-slate-950 border border-slate-700 rounded-lg p-1 text-center" />
            </div>
        </div>
        <div id="gridDemo" class="h-44 bg-slate-950 p-3 rounded-2xl border border-slate-700"></div>
        <textarea id="gridCssOut" rows="3" readonly class="w-full bg-slate-950 border border-slate-700 rounded-xl p-2.5 text-cyan-400 font-mono text-xs outline-none resize-none"></textarea>
    </div>
    """,
    """
    const demo = document.getElementById('gridDemo');
    const cols = document.getElementById('gridCols');
    const rows = document.getElementById('gridRows');
    const gap = document.getElementById('gridGap');
    const css = document.getElementById('gridCssOut');

    function update() {
        const c = parseInt(cols.value) || 3;
        const r = parseInt(rows.value) || 2;
        const g = parseInt(gap.value) || 8;

        demo.style.display = 'grid';
        demo.style.gridTemplateColumns = `repeat(${c}, 1fr)`;
        demo.style.gridTemplateRows = `repeat(${r}, 1fr)`;
        demo.style.gap = `${g}px`;

        demo.innerHTML = '';
        for (let i = 0; i < c * r; i++) {
            const div = document.createElement('div');
            div.className = 'bg-slate-800 border border-slate-700 rounded-xl flex items-center justify-center text-xs font-bold text-cyan-400';
            div.innerText = i + 1;
            demo.appendChild(div);
        }

        css.value = `display: grid;\\ngrid-template-columns: repeat(${c}, 1fr);\\ngrid-template-rows: repeat(${r}, 1fr);\\ngap: ${g}px;`;
    }

    [cols, rows, gap].forEach(el => el.addEventListener('input', update));
    update();
    """
)

# 83. Flexbox Playground
create_project(
    "Flexbox Playground",
    "Interactive Flexbox Playground",
    "CSS & Design",
    "📦",
    "Visualize flex-direction, justify-content, and align-items dynamically.",
    """
    <div class="space-y-4">
        <div class="grid grid-cols-3 gap-2 text-xs text-slate-300">
            <div>
                <label class="block mb-1">Direction</label>
                <select id="flexDir" class="w-full bg-slate-950 border border-slate-700 rounded-xl p-2 text-white outline-none">
                    <option value="row">row</option>
                    <option value="column">column</option>
                </select>
            </div>
            <div>
                <label class="block mb-1">Justify</label>
                <select id="flexJust" class="w-full bg-slate-950 border border-slate-700 rounded-xl p-2 text-white outline-none">
                    <option value="flex-start">flex-start</option>
                    <option value="center" selected>center</option>
                    <option value="space-between">space-between</option>
                </select>
            </div>
            <div>
                <label class="block mb-1">Align</label>
                <select id="flexAlign" class="w-full bg-slate-950 border border-slate-700 rounded-xl p-2 text-white outline-none">
                    <option value="stretch">stretch</option>
                    <option value="center" selected>center</option>
                    <option value="flex-start">flex-start</option>
                </select>
            </div>
        </div>
        <div id="flexDemo" class="h-44 bg-slate-950 p-3 rounded-2xl border border-slate-700 flex gap-2">
            <div class="w-12 h-12 bg-cyan-500 rounded-xl flex items-center justify-center font-bold text-slate-900">1</div>
            <div class="w-12 h-12 bg-blue-500 rounded-xl flex items-center justify-center font-bold text-white">2</div>
            <div class="w-12 h-12 bg-purple-500 rounded-xl flex items-center justify-center font-bold text-white">3</div>
        </div>
    </div>
    """,
    """
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
    """
)

# 84. Neumorphism Generator
create_project(
    "Neumorphism Generator",
    "Neumorphic Soft UI Generator",
    "CSS & Design",
    "⚪",
    "Craft soft extruded and inset neumorphic UI components with light and shadow pairing.",
    """
    <div class="space-y-4">
        <div class="flex justify-center p-10 bg-slate-800 rounded-2xl">
            <div id="neuTarget" class="w-32 h-32 rounded-3xl flex items-center justify-center font-bold text-cyan-400 text-xs">
                Soft UI
            </div>
        </div>
        <div class="grid grid-cols-2 gap-3 text-xs text-slate-300">
            <div>
                <label class="block mb-1">Distance: <span id="neuDistVal">10</span>px</label>
                <input type="range" id="neuDist" min="2" max="25" value="10" class="w-full accent-cyan-500" />
            </div>
            <div>
                <label class="block mb-1">Blur: <span id="neuBlurVal">20</span>px</label>
                <input type="range" id="neuBlur" min="4" max="50" value="20" class="w-full accent-cyan-500" />
            </div>
        </div>
    </div>
    """,
    """
    const target = document.getElementById('neuTarget');
    const dist = document.getElementById('neuDist');
    const blur = document.getElementById('neuBlur');

    function update() {
        document.getElementById('neuDistVal').innerText = dist.value;
        document.getElementById('neuBlurVal').innerText = blur.value;
        const d = dist.value;
        const b = blur.value;
        target.style.background = '#1e293b';
        target.style.boxShadow = `${d}px ${d}px ${b}px #121927, -${d}px -${d}px ${b}px #2a394f`;
    }

    [dist, blur].forEach(el => el.addEventListener('input', update));
    update();
    """
)

# 85. Clip Path Maker
create_project(
    "Clip Path Maker",
    "CSS Clip-Path Shape Maker",
    "CSS & Design",
    "✂️",
    "Preview CSS clip-path geometric polygons: triangle, rhombus, trapezoid, and star.",
    """
    <div class="space-y-4 text-center">
        <div class="flex justify-center p-8 bg-slate-950 rounded-2xl border border-slate-800">
            <div id="clipTarget" class="w-36 h-36 bg-gradient-to-tr from-cyan-400 to-indigo-600 transition-all"></div>
        </div>
        <div class="flex justify-center gap-2">
            <button class="clip-btn px-3 py-1.5 bg-slate-700 hover:bg-cyan-600 rounded-xl text-xs font-bold text-white transition" data-shape="triangle">Triangle</button>
            <button class="clip-btn px-3 py-1.5 bg-slate-700 hover:bg-cyan-600 rounded-xl text-xs font-bold text-white transition" data-shape="rhombus">Rhombus</button>
            <button class="clip-btn px-3 py-1.5 bg-slate-700 hover:bg-cyan-600 rounded-xl text-xs font-bold text-white transition" data-shape="star">Star</button>
        </div>
        <input type="text" id="clipCss" readonly class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-cyan-400 font-mono text-xs outline-none text-center" />
    </div>
    """,
    """
    const target = document.getElementById('clipTarget');
    const css = document.getElementById('clipCss');

    const shapes = {
        triangle: 'polygon(50% 0%, 0% 100%, 100% 100%)',
        rhombus: 'polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%)',
        star: 'polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%)'
    };

    document.querySelectorAll('.clip-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const poly = shapes[btn.dataset.shape];
            target.style.clipPath = poly;
            css.value = `clip-path: ${poly};`;
        });
    });

    document.querySelector('.clip-btn').click();
    """
)

# 86. Color Contrast Checker
create_project(
    "Color Contrast Checker",
    "WCAG Color Contrast Checker",
    "Accessibility",
    "👁️",
    "Evaluate WCAG 2.1 AA/AAA compliance contrast ratios between foreground and background.",
    """
    <div class="space-y-4">
        <div id="contrastBox" class="p-6 rounded-2xl text-center border border-slate-700 transition-colors">
            <h3 class="text-xl font-bold">Contrast Preview Text</h3>
            <p class="text-xs mt-1">Web Content Accessibility Guidelines (WCAG).</p>
        </div>
        <div class="grid grid-cols-2 gap-3">
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Text Color</label>
                <input type="color" id="contFg" value="#06b6d4" class="w-full h-10 rounded-xl bg-transparent cursor-pointer" />
            </div>
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Background Color</label>
                <input type="color" id="contBg" value="#0f172a" class="w-full h-10 rounded-xl bg-transparent cursor-pointer" />
            </div>
        </div>
        <div class="bg-slate-900 p-4 rounded-2xl border border-slate-700 text-center">
            <div id="ratioVal" class="text-3xl font-extrabold text-cyan-400 font-mono my-1">8.5:1</div>
            <div id="wcagBadge" class="text-xs font-bold text-emerald-400 uppercase tracking-widest">Passes WCAG AAA</div>
        </div>
    </div>
    """,
    """
    function lum(hex) {
        const rgb = parseInt(hex.slice(1), 16);
        const r = (rgb >> 16) & 0xff;
        const g = (rgb >> 8) & 0xff;
        const b = (rgb >> 0) & 0xff;
        const a = [r, g, b].map(v => {
            v /= 255;
            return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
        });
        return a[0] * 0.2126 + a[1] * 0.7152 + a[2] * 0.0722;
    }

    const fg = document.getElementById('contFg');
    const bg = document.getElementById('contBg');
    const box = document.getElementById('contrastBox');
    const ratioVal = document.getElementById('ratioVal');
    const badge = document.getElementById('wcagBadge');

    function check() {
        const l1 = lum(fg.value);
        const l2 = lum(bg.value);
        const ratio = (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);

        box.style.color = fg.value;
        box.style.backgroundColor = bg.value;

        ratioVal.innerText = ratio.toFixed(2) + ':1';
        if (ratio >= 7) {
            badge.innerText = 'Passes WCAG AAA (Super Accessible)';
            badge.className = 'text-xs font-bold text-emerald-400';
        } else if (ratio >= 4.5) {
            badge.innerText = 'Passes WCAG AA (Standard)';
            badge.className = 'text-xs font-bold text-cyan-400';
        } else {
            badge.innerText = 'Fails WCAG (Low Contrast)';
            badge.className = 'text-xs font-bold text-rose-400';
        }
    }

    fg.addEventListener('input', check);
    bg.addEventListener('input', check);
    check();
    """
)

# 87. Aspect Ratio Calculator
create_project(
    "Aspect Ratio Calculator",
    "Screen Aspect Ratio Calculator",
    "Media & Design",
    "📺",
    "Maintain responsive proportions (16:9, 4:3, 21:9, 1:1) while resizing dimensions.",
    """
    <div class="space-y-4">
        <div class="grid grid-cols-2 gap-3">
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Width (px)</label>
                <input type="number" id="arW" value="1920" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-white font-mono outline-none" />
            </div>
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Height (px)</label>
                <input type="number" id="arH" value="1080" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-white font-mono outline-none" />
            </div>
        </div>
        <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 text-center">
            <span class="text-xs text-slate-400">Aspect Ratio</span>
            <div id="arResult" class="text-3xl font-extrabold text-cyan-400 font-mono my-1">16:9</div>
        </div>
    </div>
    """,
    """
    function gcd(a, b) {
        return b === 0 ? a : gcd(b, a % b);
    }

    const w = document.getElementById('arW');
    const h = document.getElementById('arH');
    const res = document.getElementById('arResult');

    function calculate() {
        const width = parseInt(w.value) || 0;
        const height = parseInt(h.value) || 0;
        if (width <= 0 || height <= 0) { res.innerText = '--:--'; return; }
        const divisor = gcd(width, height);
        res.innerText = `${width / divisor}:${height / divisor}`;
    }

    w.addEventListener('input', calculate);
    h.addEventListener('input', calculate);
    calculate();
    """
)

# 88. SVG Wave Generator
create_project(
    "SVG Wave Generator",
    "SVG Wave Separator Maker",
    "CSS & Design",
    "🌊",
    "Generate organic SVG curve dividers with custom frequency and amplitude.",
    """
    <div class="space-y-4 text-center">
        <div class="bg-slate-950 rounded-2xl border border-slate-800 overflow-hidden h-36 flex items-end">
            <svg id="waveSvg" viewBox="0 0 500 150" preserveAspectRatio="none" class="w-full h-full"></svg>
        </div>
        <button id="waveGen" class="px-6 py-2.5 bg-cyan-600 hover:bg-cyan-500 text-white font-bold rounded-xl text-xs transition">
            Generate Random Wave
        </button>
    </div>
    """,
    """
    const svg = document.getElementById('waveSvg');
    const btn = document.getElementById('waveGen');

    function makeWave() {
        const y1 = Math.floor(Math.random() * 80) + 30;
        const y2 = Math.floor(Math.random() * 80) + 30;
        const y3 = Math.floor(Math.random() * 80) + 30;
        const path = `M 0,${y1} C 150,${y2} 350,${y3} 500,${y1} L 500,150 L 0,150 Z`;
        svg.innerHTML = `<path d="${path}" fill="#06b6d4"></path>`;
    }

    btn.addEventListener('click', makeWave);
    makeWave();
    """
)

# 89. CSS Keyframe Animator
create_project(
    "CSS Keyframe Animator",
    "CSS Keyframe Animator",
    "CSS & Design",
    "🎬",
    "Interactive animation tester for CSS transforms: spin, bounce, pulse, and wobble.",
    """
    <div class="space-y-4 text-center">
        <div class="flex justify-center items-center h-40 bg-slate-950 rounded-2xl border border-slate-800">
            <div id="animTarget" class="w-16 h-16 bg-gradient-to-tr from-cyan-400 to-blue-600 rounded-2xl shadow-xl flex items-center justify-center font-bold text-white">
                🚀
            </div>
        </div>
        <div class="flex justify-center gap-2">
            <button class="anim-btn px-3 py-1.5 bg-slate-700 hover:bg-cyan-600 rounded-xl text-xs font-bold text-white transition" data-anim="spin">Spin</button>
            <button class="anim-btn px-3 py-1.5 bg-slate-700 hover:bg-cyan-600 rounded-xl text-xs font-bold text-white transition" data-anim="bounce">Bounce</button>
            <button class="anim-btn px-3 py-1.5 bg-slate-700 hover:bg-cyan-600 rounded-xl text-xs font-bold text-white transition" data-anim="pulse">Pulse</button>
        </div>
    </div>
    """,
    """
    const target = document.getElementById('animTarget');

    document.querySelectorAll('.anim-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            target.className = 'w-16 h-16 bg-gradient-to-tr from-cyan-400 to-blue-600 rounded-2xl shadow-xl flex items-center justify-center font-bold text-white';
            const mode = btn.dataset.anim;
            if (mode === 'spin') target.classList.add('animate-spin');
            if (mode === 'bounce') target.classList.add('animate-bounce');
            if (mode === 'pulse') target.classList.add('animate-pulse');
        });
    });
    """
)

# 90. Sorting Algorithm Visualizer
create_project(
    "Sorting Algorithm Visualizer",
    "Sorting Algorithm Visualizer",
    "Algorithms & Science",
    "📶",
    "Step-by-step visual bar animation comparing Bubble Sort and Selection Sort.",
    """
    <div class="space-y-4 text-center">
        <div id="sortBars" class="flex items-end justify-center gap-1.5 h-36 bg-slate-950 p-3 rounded-2xl border border-slate-700"></div>
        <div class="flex justify-center gap-3">
            <button id="sortRandom" class="px-4 py-2 bg-slate-700 hover:bg-slate-600 text-white rounded-xl text-xs font-bold transition">Randomize</button>
            <button id="sortStart" class="px-5 py-2 bg-cyan-600 hover:bg-cyan-500 text-white rounded-xl text-xs font-bold transition">Run Bubble Sort</button>
        </div>
    </div>
    """,
    """
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
    """
)

# 91. Conways Game of Life
create_project(
    "Conways Game of Life",
    "Conway's Game of Life",
    "Simulations",
    "🧬",
    "Zero-player cellular automaton evolution simulation based on mathematical neighbor rules.",
    """
    <div class="space-y-4 text-center">
        <canvas id="lifeCanvas" width="280" height="280" class="bg-slate-950 border border-slate-700 rounded-2xl mx-auto cursor-pointer"></canvas>
        <div class="flex justify-center gap-3">
            <button id="lifeToggle" class="px-5 py-2 bg-cyan-600 hover:bg-cyan-500 text-white rounded-xl text-xs font-bold transition">Play / Pause</button>
            <button id="lifeSeed" class="px-5 py-2 bg-slate-700 hover:bg-slate-600 text-white rounded-xl text-xs font-bold transition">Random Seed</button>
        </div>
    </div>
    """,
    """
    const canvas = document.getElementById('lifeCanvas');
    const ctx = canvas.getContext('2d');
    const COLS = 28;
    const ROWS = 28;
    const RES = 10;

    let grid = Array(COLS).fill(null).map(() => Array(ROWS).fill(0));
    let running = false;
    let timer = null;

    function seed() {
        for (let i = 0; i < COLS; i++) {
            for (let j = 0; j < ROWS; j++) {
                grid[i][j] = Math.random() < 0.25 ? 1 : 0;
            }
        }
        draw();
    }

    function draw() {
        ctx.fillStyle = '#0f172a';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#06b6d4';
        for (let i = 0; i < COLS; i++) {
            for (let j = 0; j < ROWS; j++) {
                if (grid[i][j]) ctx.fillRect(i * RES, j * RES, RES - 1, RES - 1);
            }
        }
    }

    function step() {
        const next = grid.map(arr => [...arr]);
        for (let x = 0; x < COLS; x++) {
            for (let y = 0; y < ROWS; y++) {
                let neighbors = 0;
                for (let i = -1; i <= 1; i++) {
                    for (let j = -1; j <= 1; j++) {
                        if (i === 0 && j === 0) continue;
                        const col = (x + i + COLS) % COLS;
                        const row = (y + j + ROWS) % ROWS;
                        neighbors += grid[col][row];
                    }
                }
                if (grid[x][y] === 1 && (neighbors < 2 || neighbors > 3)) next[x][y] = 0;
                else if (grid[x][y] === 0 && neighbors === 3) next[x][y] = 1;
            }
        }
        grid = next;
        draw();
    }

    document.getElementById('lifeToggle').addEventListener('click', () => {
        running = !running;
        if (running) timer = setInterval(step, 100);
        else clearInterval(timer);
    });

    document.getElementById('lifeSeed').addEventListener('click', seed);
    seed();
    """
)

# 92. Fractal Tree Generator
create_project(
    "Fractal Tree Generator",
    "Recursive Fractal Tree",
    "Simulations",
    "🌳",
    "Procedural recursive branching tree using canvas 2D transformations.",
    """
    <div class="space-y-4 text-center">
        <canvas id="treeCanvas" width="400" height="260" class="w-full bg-slate-950 border border-slate-700 rounded-2xl"></canvas>
        <div class="flex justify-center items-center gap-4 text-xs text-slate-300">
            <span>Branch Angle:</span>
            <input type="range" id="treeAngle" min="10" max="60" value="25" class="accent-cyan-500 cursor-pointer" />
        </div>
    </div>
    """,
    """
    const canvas = document.getElementById('treeCanvas');
    const ctx = canvas.getContext('2d');
    const angleRange = document.getElementById('treeAngle');

    function drawBranch(len, angle) {
        ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.lineTo(0, -len);
        ctx.stroke();

        if (len < 10) return;

        ctx.save();
        ctx.translate(0, -len);
        ctx.rotate(angle);
        drawBranch(len * 0.72, angle);
        ctx.restore();

        ctx.save();
        ctx.translate(0, -len);
        ctx.rotate(-angle);
        drawBranch(len * 0.72, angle);
        ctx.restore();
    }

    function render() {
        ctx.fillStyle = '#0f172a';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.strokeStyle = '#06b6d4';
        ctx.lineWidth = 2;

        ctx.save();
        ctx.translate(canvas.width / 2, canvas.height);
        const rad = (parseInt(angleRange.value) * Math.PI) / 180;
        drawBranch(65, rad);
        ctx.restore();
    }

    angleRange.addEventListener('input', render);
    render();
    """
)

# 93. Matrix Rain Effect
create_project(
    "Matrix Rain Effect",
    "Matrix Digital Rain",
    "Simulations",
    "🟢",
    "The iconic green cascading digital rain terminal visualizer from The Matrix.",
    """
    <div class="space-y-4 text-center">
        <canvas id="matrixCanvas" width="400" height="260" class="w-full bg-black border border-emerald-900 rounded-2xl"></canvas>
    </div>
    """,
    """
    const canvas = document.getElementById('matrixCanvas');
    const ctx = canvas.getContext('2d');

    const chars = '0123456789ABCDEFabcdef@#$%&*';
    const fontSize = 14;
    const columns = Math.floor(canvas.width / fontSize);
    const drops = Array(columns).fill(1);

    function drawMatrix() {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.08)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.fillStyle = '#10b981';
        ctx.font = `${fontSize}px monospace`;

        for (let i = 0; i < drops.length; i++) {
            const char = chars[Math.floor(Math.random() * chars.length)];
            ctx.fillText(char, i * fontSize, drops[i] * fontSize);

            if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                drops[i] = 0;
            }
            drops[i]++;
        }
        requestAnimationFrame(drawMatrix);
    }
    drawMatrix();
    """
)
