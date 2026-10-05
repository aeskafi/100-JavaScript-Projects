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
    <div class="w-full max-w-2xl bg-slate-800 border border-slate-700 rounded-3xl shadow-2xl p-6 sm:p-8 backdrop-blur-md">
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

# 16. Markdown Previewer
create_project(
    "Markdown Previewer",
    "Live Markdown Previewer",
    "Text & Analysis",
    "📝",
    "Real-time markdown parsing with instant HTML preview for headers, lists, code, and links.",
    """
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Markdown Source</label>
            <textarea id="mdInput" rows="12" class="w-full bg-slate-950 border border-slate-700 rounded-2xl p-3 text-sm text-slate-100 font-mono focus:ring-2 focus:ring-cyan-500 outline-none resize-none"># Hello World\\n\\nThis is a **live markdown** previewer.\\n\\n- Rapid MVP Development\\n- Modern Vanilla JS\\n- Clean Dark Theme\\n\\n> Built with passion by [Arham Eskafi](https://arham.dev).</textarea>
        </div>
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Rendered HTML</label>
            <div id="mdOutput" class="h-64 md:h-[18rem] overflow-y-auto bg-slate-950 border border-slate-700 rounded-2xl p-4 text-sm text-slate-200 prose prose-invert"></div>
        </div>
    </div>
    """,
    """
    const input = document.getElementById('mdInput');
    const output = document.getElementById('mdOutput');

    function parseMarkdown(md) {
        let html = md
            .replace(/^### (.*$)/gim, '<h3 class="text-lg font-bold text-cyan-400 mt-2 mb-1">$1</h3>')
            .replace(/^## (.*$)/gim, '<h2 class="text-xl font-bold text-cyan-300 mt-3 mb-1">$1</h2>')
            .replace(/^# (.*$)/gim, '<h1 class="text-2xl font-black text-white mt-4 mb-2">$1</h1>')
            .replace(/^\\> (.*$)/gim, '<blockquote class="border-l-4 border-cyan-500 pl-3 my-2 text-slate-400 italic">$1</blockquote>')
            .replace(/\\*\\*(.*?)\\*\\*/gim, '<strong class="font-bold text-cyan-400">$1</strong>')
            .replace(/\\*(.*?)\\*/gim, '<em class="italic">$1</em>')
            .replace(/`(.*?)`/gim, '<code class="bg-slate-800 text-cyan-300 px-1 py-0.5 rounded text-xs font-mono">$1</code>')
            .replace(/\\[(.*?)\\]\\((.*?)\\)/gim, '<a href="$2" target="_blank" class="text-cyan-400 underline hover:text-cyan-300">$1</a>')
            .replace(/^\\- (.*$)/gim, '<li class="ml-4 list-disc text-slate-300">$1</li>')
            .replace(/\\n/gim, '<br/>');
        return html;
    }

    input.addEventListener('input', () => {
        output.innerHTML = parseMarkdown(input.value);
    });
    output.innerHTML = parseMarkdown(input.value);
    """
)

# 17. Slug Generator
create_project(
    "Slug Generator",
    "URL Slug Generator",
    "Text & Analysis",
    "🔗",
    "Convert any title or sentence into an SEO-friendly, clean URL slug.",
    """
    <div class="space-y-4">
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Enter Text or Article Title</label>
            <input type="text" id="slugInput" value="100 JavaScript Projects for High Speed Web Apps!" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:ring-2 focus:ring-cyan-500 outline-none" />
        </div>
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Generated Slug</label>
            <div class="flex gap-2">
                <input type="text" id="slugOutput" readonly class="flex-1 bg-slate-900 border border-slate-700 rounded-xl px-4 py-2.5 text-cyan-400 font-mono font-medium outline-none" />
                <button id="copySlug" class="px-4 py-2 bg-slate-700 hover:bg-cyan-600 text-white font-medium rounded-xl text-xs transition">Copy</button>
            </div>
        </div>
    </div>
    """,
    """
    const input = document.getElementById('slugInput');
    const output = document.getElementById('slugOutput');
    const copyBtn = document.getElementById('copySlug');

    function generateSlug() {
        const str = input.value;
        const slug = str
            .toLowerCase()
            .trim()
            .replace(/[^\\w\\s-]/g, '')
            .replace(/[\\s_-]+/g, '-')
            .replace(/^-+|-+$/g, '');
        output.value = slug;
    }

    copyBtn.addEventListener('click', () => {
        navigator.clipboard.writeText(output.value);
        copyBtn.innerText = 'Copied!';
        setTimeout(() => copyBtn.innerText = 'Copy', 1500);
    });

    input.addEventListener('input', generateSlug);
    generateSlug();
    """
)

# 18. Case Converter
create_project(
    "Case Converter",
    "Case Converter Suite",
    "Text & Analysis",
    "🔡",
    "Switch text between UPPERCASE, lowercase, camelCase, PascalCase, snake_case, and kebab-case.",
    """
    <div class="space-y-4">
        <textarea id="caseInput" rows="4" class="w-full bg-slate-950 border border-slate-700 rounded-2xl p-3 text-sm text-slate-100 font-mono focus:ring-2 focus:ring-cyan-500 outline-none resize-none">Hello World From Walk Cook Live</textarea>
        <div class="grid grid-cols-2 sm:grid-cols-3 gap-2">
            <button class="case-btn px-3 py-2 bg-slate-700 hover:bg-slate-600 rounded-xl text-xs font-medium text-slate-200 transition" data-case="upper">UPPERCASE</button>
            <button class="case-btn px-3 py-2 bg-slate-700 hover:bg-slate-600 rounded-xl text-xs font-medium text-slate-200 transition" data-case="lower">lowercase</button>
            <button class="case-btn px-3 py-2 bg-slate-700 hover:bg-slate-600 rounded-xl text-xs font-medium text-slate-200 transition" data-case="title">Title Case</button>
            <button class="case-btn px-3 py-2 bg-slate-700 hover:bg-slate-600 rounded-xl text-xs font-medium text-slate-200 transition" data-case="camel">camelCase</button>
            <button class="case-btn px-3 py-2 bg-slate-700 hover:bg-slate-600 rounded-xl text-xs font-medium text-slate-200 transition" data-case="snake">snake_case</button>
            <button class="case-btn px-3 py-2 bg-slate-700 hover:bg-slate-600 rounded-xl text-xs font-medium text-slate-200 transition" data-case="kebab">kebab-case</button>
        </div>
    </div>
    """,
    """
    const input = document.getElementById('caseInput');
    const buttons = document.querySelectorAll('.case-btn');

    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            const val = input.value;
            const mode = btn.dataset.case;
            if (mode === 'upper') input.value = val.toUpperCase();
            if (mode === 'lower') input.value = val.toLowerCase();
            if (mode === 'title') input.value = val.replace(/\\w\\S*/g, (txt) => txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase());
            if (mode === 'camel') {
                input.value = val.toLowerCase().replace(/[^a-zA-Z0-9]+(.)/g, (m, chr) => chr.toUpperCase());
            }
            if (mode === 'snake') {
                input.value = val.match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
                    .map(x => x.toLowerCase()).join('_');
            }
            if (mode === 'kebab') {
                input.value = val.match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
                    .map(x => x.toLowerCase()).join('-');
            }
        });
    });
    """
)

# 19. Password Generator
create_project(
    "Password Generator",
    "Secure Password Generator",
    "Security & Crypto",
    "🔐",
    "Generate random, cryptographically secure passwords with entropy strength estimation.",
    """
    <div class="space-y-4">
        <div class="flex gap-2">
            <input type="text" id="passOut" readonly class="flex-1 bg-slate-950 border border-slate-700 rounded-xl px-4 py-3 text-cyan-400 font-mono text-lg tracking-wider outline-none" />
            <button id="copyPass" class="px-4 py-2 bg-slate-700 hover:bg-cyan-600 text-white font-medium rounded-xl text-xs transition">Copy</button>
            <button id="refreshPass" class="px-4 py-2 bg-cyan-600 hover:bg-cyan-500 text-white font-medium rounded-xl text-xs transition">↻ New</button>
        </div>
        <div>
            <div class="flex justify-between text-xs text-slate-300 mb-1">
                <span>Length</span>
                <span id="lenVal">16</span>
            </div>
            <input type="range" id="passLen" min="6" max="32" value="16" class="w-full accent-cyan-500 cursor-pointer" />
        </div>
        <div class="grid grid-cols-2 gap-2 text-xs text-slate-300">
            <label class="flex items-center gap-2"><input type="checkbox" id="incUpper" checked class="accent-cyan-500" /> Uppercase (A-Z)</label>
            <label class="flex items-center gap-2"><input type="checkbox" id="incLower" checked class="accent-cyan-500" /> Lowercase (a-z)</label>
            <label class="flex items-center gap-2"><input type="checkbox" id="incNums" checked class="accent-cyan-500" /> Numbers (0-9)</label>
            <label class="flex items-center gap-2"><input type="checkbox" id="incSyms" checked class="accent-cyan-500" /> Symbols (!@#$)</label>
        </div>
    </div>
    """,
    """
    const passOut = document.getElementById('passOut');
    const copyPass = document.getElementById('copyPass');
    const refreshPass = document.getElementById('refreshPass');
    const passLen = document.getElementById('passLen');
    const lenVal = document.getElementById('lenVal');

    const chars = {
        upper: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        lower: 'abcdefghijklmnopqrstuvwxyz',
        nums: '0123456789',
        syms: '!@#$%^&*()_+~|}{[]:;?><,./-='
    };

    function generate() {
        let pool = '';
        if (document.getElementById('incUpper').checked) pool += chars.upper;
        if (document.getElementById('incLower').checked) pool += chars.lower;
        if (document.getElementById('incNums').checked) pool += chars.nums;
        if (document.getElementById('incSyms').checked) pool += chars.syms;

        if (!pool) { passOut.value = 'Select at least one set'; return; }

        const len = parseInt(passLen.value);
        lenVal.innerText = len;
        let pass = '';
        const arr = new Uint32Array(len);
        window.crypto.getRandomValues(arr);
        for (let i = 0; i < len; i++) {
            pass += pool[arr[i] % pool.length];
        }
        passOut.value = pass;
    }

    copyPass.addEventListener('click', () => {
        navigator.clipboard.writeText(passOut.value);
        copyPass.innerText = 'Copied!';
        setTimeout(() => copyPass.innerText = 'Copy', 1500);
    });

    [passLen, refreshPass, document.getElementById('incUpper'), document.getElementById('incLower'), document.getElementById('incNums'), document.getElementById('incSyms')].forEach(el => el.addEventListener('input', generate));
    generate();
    """
)

# 20. Lorem Ipsum Generator
create_project(
    "Lorem Ipsum Generator",
    "Lorem Ipsum Dummy Text",
    "Text & Analysis",
    "📄",
    "Generate custom placeholder paragraphs, words, and sentences for rapid prototyping.",
    """
    <div class="space-y-4">
        <div class="flex items-center gap-3">
            <label class="text-xs font-medium text-slate-300">Paragraphs:</label>
            <input type="number" id="loremCount" min="1" max="10" value="3" class="w-20 bg-slate-950 border border-slate-700 rounded-xl px-3 py-1.5 text-center text-white outline-none" />
            <button id="genLorem" class="px-4 py-2 bg-cyan-600 hover:bg-cyan-500 text-white font-medium rounded-xl text-xs transition">Generate</button>
            <button id="copyLorem" class="px-4 py-2 bg-slate-700 hover:bg-slate-600 text-white font-medium rounded-xl text-xs transition">Copy</button>
        </div>
        <div id="loremOutput" class="h-64 overflow-y-auto bg-slate-950 border border-slate-700 rounded-2xl p-4 text-sm text-slate-300 space-y-3 leading-relaxed"></div>
    </div>
    """,
    """
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
    """
)

# 21. Base64 Encoder Decoder
create_project(
    "Base64 Encoder Decoder",
    "Base64 Encoder & Decoder",
    "Security & Crypto",
    "🔒",
    "Encode raw strings to Base64 or decode Base64 data back to clear text.",
    """
    <div class="space-y-4">
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Plain Text</label>
            <textarea id="b64Text" rows="3" class="w-full bg-slate-950 border border-slate-700 rounded-2xl p-3 text-sm text-slate-100 font-mono outline-none resize-none">Hello, Arham!</textarea>
        </div>
        <div class="flex gap-2 justify-center">
            <button id="b64Encode" class="px-4 py-2 bg-cyan-600 hover:bg-cyan-500 text-white rounded-xl text-xs font-bold transition">↓ Encode to Base64</button>
            <button id="b64Decode" class="px-4 py-2 bg-slate-700 hover:bg-slate-600 text-white rounded-xl text-xs font-bold transition">↑ Decode to Text</button>
        </div>
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Base64 Encoded</label>
            <textarea id="b64Cipher" rows="3" class="w-full bg-slate-950 border border-slate-700 rounded-2xl p-3 text-sm text-cyan-400 font-mono outline-none resize-none"></textarea>
        </div>
    </div>
    """,
    """
    const textEl = document.getElementById('b64Text');
    const cipherEl = document.getElementById('b64Cipher');

    document.getElementById('b64Encode').addEventListener('click', () => {
        try {
            cipherEl.value = btoa(unescape(encodeURIComponent(textEl.value)));
        } catch(e) {
            cipherEl.value = 'Encoding error: ' + e.message;
        }
    });

    document.getElementById('b64Decode').addEventListener('click', () => {
        try {
            textEl.value = decodeURIComponent(escape(atob(cipherEl.value)));
        } catch(e) {
            textEl.value = 'Invalid Base64 string';
        }
    });

    document.getElementById('b64Encode').click();
    """
)

# 22. URL Encoder Decoder
create_project(
    "URL Encoder Decoder",
    "URL Component Encoder",
    "Security & Crypto",
    "🌐",
    "Percent-encode special URI components and decode query strings safely.",
    """
    <div class="space-y-4">
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Decoded URL / Query</label>
            <textarea id="urlRaw" rows="3" class="w-full bg-slate-950 border border-slate-700 rounded-2xl p-3 text-sm text-slate-100 font-mono outline-none resize-none">https://arham.dev/search?q=100 JavaScript Projects & tags=fast</textarea>
        </div>
        <div class="flex gap-2 justify-center">
            <button id="urlEncBtn" class="px-4 py-2 bg-cyan-600 hover:bg-cyan-500 text-white rounded-xl text-xs font-bold transition">↓ Encode URL</button>
            <button id="urlDecBtn" class="px-4 py-2 bg-slate-700 hover:bg-slate-600 text-white rounded-xl text-xs font-bold transition">↑ Decode URL</button>
        </div>
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Encoded URL</label>
            <textarea id="urlEnc" rows="3" class="w-full bg-slate-950 border border-slate-700 rounded-2xl p-3 text-sm text-cyan-400 font-mono outline-none resize-none"></textarea>
        </div>
    </div>
    """,
    """
    const raw = document.getElementById('urlRaw');
    const enc = document.getElementById('urlEnc');

    document.getElementById('urlEncBtn').addEventListener('click', () => {
        enc.value = encodeURIComponent(raw.value);
    });
    document.getElementById('urlDecBtn').addEventListener('click', () => {
        try {
            raw.value = decodeURIComponent(enc.value);
        } catch(e) {
            raw.value = 'Malformed URI sequence';
        }
    });
    document.getElementById('urlEncBtn').click();
    """
)

# 23. JSON Formatter and Validator
create_project(
    "JSON Formatter and Validator",
    "JSON Formatter & Validator",
    "Developer Tools",
    "{ }",
    "Format, minify, and validate JSON payloads with clear syntax error locations.",
    """
    <div class="space-y-4">
        <textarea id="jsonInput" rows="8" class="w-full bg-slate-950 border border-slate-700 rounded-2xl p-3 text-sm text-cyan-400 font-mono outline-none resize-none">{"project":"100-JavaScript-Projects","creator":"Arham Eskafi","awesome":true,"stars":100}</textarea>
        <div class="flex gap-2">
            <button id="jsonFormat" class="px-4 py-2 bg-cyan-600 hover:bg-cyan-500 text-white rounded-xl text-xs font-bold transition">Beautify (Indent 2)</button>
            <button id="jsonMinify" class="px-4 py-2 bg-slate-700 hover:bg-slate-600 text-white rounded-xl text-xs font-bold transition">Minify</button>
            <button id="jsonValidate" class="px-4 py-2 bg-emerald-600 hover:bg-emerald-500 text-white rounded-xl text-xs font-bold transition">Validate</button>
        </div>
        <div id="jsonStatus" class="text-xs font-mono font-medium text-slate-400">Ready</div>
    </div>
    """,
    """
    const input = document.getElementById('jsonInput');
    const status = document.getElementById('jsonStatus');

    document.getElementById('jsonFormat').addEventListener('click', () => {
        try {
            const obj = JSON.parse(input.value);
            input.value = JSON.stringify(obj, null, 2);
            status.innerText = 'Valid JSON formatted successfully!';
            status.className = 'text-xs font-mono font-medium text-emerald-400';
        } catch(e) {
            status.innerText = 'Error: ' + e.message;
            status.className = 'text-xs font-mono font-medium text-rose-400';
        }
    });

    document.getElementById('jsonMinify').addEventListener('click', () => {
        try {
            const obj = JSON.parse(input.value);
            input.value = JSON.stringify(obj);
            status.innerText = 'Minified successfully!';
            status.className = 'text-xs font-mono font-medium text-emerald-400';
        } catch(e) {
            status.innerText = 'Error: ' + e.message;
            status.className = 'text-xs font-mono font-medium text-rose-400';
        }
    });

    document.getElementById('jsonValidate').addEventListener('click', () => {
        try {
            JSON.parse(input.value);
            status.innerText = '✓ Valid JSON structure!';
            status.className = 'text-xs font-mono font-medium text-emerald-400';
        } catch(e) {
            status.innerText = '✗ Syntax Error: ' + e.message;
            status.className = 'text-xs font-mono font-medium text-rose-400';
        }
    });
    """
)

# 24. Text to Speech
create_project(
    "Text to Speech",
    "Browser Text to Speech",
    "Audio & Voice",
    "🗣️",
    "Read text aloud using browser SpeechSynthesis with speed, pitch, and voice controls.",
    """
    <div class="space-y-4">
        <textarea id="ttsText" rows="4" class="w-full bg-slate-950 border border-slate-700 rounded-2xl p-3 text-sm text-slate-100 outline-none resize-none">Hello! Welcome to 100 JavaScript Projects, built for fast web explorers.</textarea>
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Select Voice</label>
            <select id="ttsVoice" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-white text-xs outline-none"></select>
        </div>
        <div class="grid grid-cols-2 gap-3">
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Pitch</label>
                <input type="range" id="ttsPitch" min="0.5" max="2" value="1" step="0.1" class="w-full accent-cyan-500 cursor-pointer" />
            </div>
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Rate / Speed</label>
                <input type="range" id="ttsRate" min="0.5" max="2" value="1" step="0.1" class="w-full accent-cyan-500 cursor-pointer" />
            </div>
        </div>
        <div class="flex gap-2">
            <button id="ttsPlay" class="flex-1 py-3 bg-cyan-600 hover:bg-cyan-500 text-white font-bold rounded-xl text-sm transition">▶ Speak</button>
            <button id="ttsStop" class="px-6 py-3 bg-slate-700 hover:bg-rose-600 text-white font-bold rounded-xl text-sm transition">⏹ Stop</button>
        </div>
    </div>
    """,
    """
    const textEl = document.getElementById('ttsText');
    const voiceSelect = document.getElementById('ttsVoice');
    const pitch = document.getElementById('ttsPitch');
    const rate = document.getElementById('ttsRate');
    let voices = [];

    function populateVoices() {
        voices = speechSynthesis.getVoices();
        voiceSelect.innerHTML = voices.map((v, i) => `<option value="${i}">${v.name} (${v.lang})</option>`).join('');
    }

    speechSynthesis.onvoiceschanged = populateVoices;
    populateVoices();

    document.getElementById('ttsPlay').addEventListener('click', () => {
        speechSynthesis.cancel();
        const ut = new SpeechSynthesisUtterance(textEl.value);
        if (voices[voiceSelect.value]) ut.voice = voices[voiceSelect.value];
        ut.pitch = parseFloat(pitch.value);
        ut.rate = parseFloat(rate.value);
        speechSynthesis.speak(ut);
    });

    document.getElementById('ttsStop').addEventListener('click', () => {
        speechSynthesis.cancel();
    });
    """
)

# 25. Morse Code Translator
create_project(
    "Morse Code Translator",
    "Morse Code Translator",
    "Converters",
    "📡",
    "Translate plain English text to International Morse Code and back with sound playback.",
    """
    <div class="space-y-4">
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">English Text</label>
            <textarea id="morseText" rows="2" class="w-full bg-slate-950 border border-slate-700 rounded-xl p-3 text-sm text-white uppercase font-mono outline-none resize-none">HELLO WORLD</textarea>
        </div>
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Morse Code (separated by spaces, '/' for word space)</label>
            <textarea id="morseCode" rows="2" class="w-full bg-slate-950 border border-slate-700 rounded-xl p-3 text-sm text-cyan-400 font-mono outline-none resize-none"></textarea>
        </div>
    </div>
    """,
    """
    const MORSE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', '0': '-----', ' ': '/'
    };
    const REVERSE_MORSE = {};
    for (let k in MORSE) REVERSE_MORSE[MORSE[k]] = k;

    const textEl = document.getElementById('morseText');
    const codeEl = document.getElementById('morseCode');

    textEl.addEventListener('input', () => {
        const val = textEl.value.toUpperCase();
        codeEl.value = val.split('').map(c => MORSE[c] || c).join(' ');
    });

    codeEl.addEventListener('input', () => {
        const tokens = codeEl.value.trim().split(/\\s+/);
        textEl.value = tokens.map(t => REVERSE_MORSE[t] || (t === '/' ? ' ' : '')).join('');
    });

    textEl.dispatchEvent(new Event('input'));
    """
)

# 26. ROT13 Cipher
create_project(
    "ROT13 Cipher",
    "ROT13 & Caesar Cipher",
    "Security & Crypto",
    "🔄",
    "Encrypt and decrypt strings using the classic 13-character rotation cipher.",
    """
    <div class="space-y-4">
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Input Text</label>
            <textarea id="rotInput" rows="3" class="w-full bg-slate-950 border border-slate-700 rounded-2xl p-3 text-sm text-slate-100 font-mono outline-none resize-none">Why did the developer cross the road? To get to the other repo!</textarea>
        </div>
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">ROT13 Result</label>
            <textarea id="rotOutput" rows="3" readonly class="w-full bg-slate-950 border border-slate-700 rounded-2xl p-3 text-sm text-cyan-400 font-mono outline-none resize-none"></textarea>
        </div>
    </div>
    """,
    """
    const input = document.getElementById('rotInput');
    const output = document.getElementById('rotOutput');

    function rot13(str) {
        return str.replace(/[a-zA-Z]/g, function (c) {
            return String.fromCharCode((c <= 'Z' ? 90 : 122) >= (c = c.charCodeAt(0) + 13) ? c : c - 26);
        });
    }

    input.addEventListener('input', () => {
        output.value = rot13(input.value);
    });
    output.value = rot13(input.value);
    """
)

# 27. Palindrome Checker
create_project(
    "Palindrome Checker",
    "Palindrome Checker",
    "Text & Analysis",
    "🔁",
    "Check if phrases, numbers, or words read identically forwards and backwards.",
    """
    <div class="space-y-4">
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Enter Word or Sentence</label>
            <input type="text" id="palInput" value="A man, a plan, a canal: Panama" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white font-mono focus:ring-2 focus:ring-cyan-500 outline-none" />
        </div>
        <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 text-center">
            <div id="palStatus" class="text-2xl font-bold text-emerald-400">Yes! It's a Palindrome 🎉</div>
            <p id="palClean" class="text-xs text-slate-400 mt-2 font-mono">Normalized: amanaplanacanalpanama</p>
        </div>
    </div>
    """,
    """
    const input = document.getElementById('palInput');
    const status = document.getElementById('palStatus');
    const cleanEl = document.getElementById('palClean');

    function check() {
        const raw = input.value;
        const clean = raw.toLowerCase().replace(/[^a-z0-9]/g, '');
        const reversed = clean.split('').reverse().join('');
        cleanEl.innerText = `Normalized: ${clean}`;
        if (!clean) {
            status.innerText = 'Type something';
            status.className = 'text-2xl font-bold text-slate-400';
            return;
        }
        if (clean === reversed) {
            status.innerText = "Yes! It's a Palindrome! 🎉";
            status.className = 'text-2xl font-bold text-emerald-400';
        } else {
            status.innerText = 'Nope, not a palindrome.';
            status.className = 'text-2xl font-bold text-rose-400';
        }
    }

    input.addEventListener('input', check);
    check();
    """
)

# 28. Text Diff Checker
create_project(
    "Text Diff Checker",
    "Text Diff & Comparison",
    "Developer Tools",
    "🔍",
    "Line-by-line comparison between original and updated text with visual diffs.",
    """
    <div class="space-y-4">
        <div class="grid grid-cols-2 gap-3">
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Original Text</label>
                <textarea id="diffA" rows="5" class="w-full bg-slate-950 border border-slate-700 rounded-xl p-2.5 text-xs text-white font-mono outline-none resize-none">apple\\nbanana\\norange</textarea>
            </div>
            <div>
                <label class="block text-xs font-medium text-slate-300 mb-1">Modified Text</label>
                <textarea id="diffB" rows="5" class="w-full bg-slate-950 border border-slate-700 rounded-xl p-2.5 text-xs text-white font-mono outline-none resize-none">apple\\nblueberry\\norange\\ngrape</textarea>
            </div>
        </div>
        <div id="diffResult" class="bg-slate-950 border border-slate-700 rounded-2xl p-4 text-xs font-mono space-y-1"></div>
    </div>
    """,
    """
    const a = document.getElementById('diffA');
    const b = document.getElementById('diffB');
    const result = document.getElementById('diffResult');

    function compare() {
        const linesA = a.value.split('\\n');
        const linesB = b.value.split('\\n');
        result.innerHTML = '';

        const max = Math.max(linesA.length, linesB.length);
        for (let i = 0; i < max; i++) {
            const la = linesA[i];
            const lb = linesB[i];
            const div = document.createElement('div');
            if (la === lb) {
                div.className = 'text-slate-400';
                div.innerText = `  ${la}`;
            } else {
                if (la !== undefined) {
                    const da = document.createElement('div');
                    da.className = 'text-rose-400 bg-rose-950/40 px-1 rounded';
                    da.innerText = `- ${la}`;
                    result.appendChild(da);
                }
                if (lb !== undefined) {
                    const db = document.createElement('div');
                    db.className = 'text-emerald-400 bg-emerald-950/40 px-1 rounded';
                    db.innerText = `+ ${lb}`;
                    result.appendChild(db);
                }
                continue;
            }
            result.appendChild(div);
        }
    }

    a.addEventListener('input', compare);
    b.addEventListener('input', compare);
    compare();
    """
)

# 29. Regex Tester
create_project(
    "Regex Tester",
    "Interactive Regex Playground",
    "Developer Tools",
    "🧪",
    "Test regular expressions live with flags, capture groups, and match counts.",
    """
    <div class="space-y-4">
        <div class="flex gap-2">
            <input type="text" id="regPattern" value="[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}" placeholder="Regex pattern" class="flex-1 bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-white font-mono focus:ring-2 focus:ring-cyan-500 outline-none" />
            <input type="text" id="regFlags" value="g" placeholder="flags" class="w-16 bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-center text-cyan-400 font-mono focus:ring-2 focus:ring-cyan-500 outline-none" />
        </div>
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Test String</label>
            <textarea id="regText" rows="4" class="w-full bg-slate-950 border border-slate-700 rounded-xl p-3 text-sm text-slate-100 font-mono outline-none resize-none">Contact us at arham@arham.dev or support@walkcooklive.com for rapid MVP builds!</textarea>
        </div>
        <div class="bg-slate-900 p-4 rounded-2xl border border-slate-700">
            <div id="regSummary" class="text-xs font-bold text-cyan-400 mb-2">Matches: 2</div>
            <div id="regMatches" class="text-xs font-mono text-slate-300 space-y-1"></div>
        </div>
    </div>
    """,
    """
    const pattern = document.getElementById('regPattern');
    const flags = document.getElementById('regFlags');
    const text = document.getElementById('regText');
    const summary = document.getElementById('regSummary');
    const matchesDiv = document.getElementById('regMatches');

    function testRegex() {
        try {
            const re = new RegExp(pattern.value, flags.value);
            const matches = [...text.value.matchAll(re)];
            summary.innerText = `Matches found: ${matches.length}`;
            summary.className = 'text-xs font-bold text-cyan-400 mb-2';
            matchesDiv.innerHTML = matches.map((m, i) => `<div class="bg-slate-950 p-1.5 rounded border border-slate-800"><span class="text-slate-500">#${i+1}:</span> <span class="text-emerald-400">${m[0]}</span> <span class="text-slate-600">(index ${m.index})</span></div>`).join('');
        } catch(e) {
            summary.innerText = 'Regex Error: ' + e.message;
            summary.className = 'text-xs font-bold text-rose-400 mb-2';
            matchesDiv.innerHTML = '';
        }
    }

    [pattern, flags, text].forEach(el => el.addEventListener('input', testRegex));
    testRegex();
    """
)

# 30. String Obfuscator
create_project(
    "String Obfuscator",
    "JavaScript String Obfuscator",
    "Security & Crypto",
    "🎭",
    "Obfuscate plain text into hexadecimal or unicode escape sequences.",
    """
    <div class="space-y-4">
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Plain Text</label>
            <input type="text" id="obfInput" value="SecretToken123!" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white font-mono focus:ring-2 focus:ring-cyan-500 outline-none" />
        </div>
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Hex Escaped (\\x..)</label>
            <input type="text" id="obfHex" readonly class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-cyan-400 font-mono text-xs outline-none" />
        </div>
        <div>
            <label class="block text-xs font-medium text-slate-300 mb-1">Unicode Escaped (\\u....)</label>
            <input type="text" id="obfUni" readonly class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2 text-emerald-400 font-mono text-xs outline-none" />
        </div>
    </div>
    """,
    """
    const input = document.getElementById('obfInput');
    const hex = document.getElementById('obfHex');
    const uni = document.getElementById('obfUni');

    function obfuscate() {
        const val = input.value;
        hex.value = val.split('').map(c => '\\\\x' + c.charCodeAt(0).toString(16).padStart(2, '0')).join('');
        uni.value = val.split('').map(c => '\\\\u' + c.charCodeAt(0).toString(16).padStart(4, '0')).join('');
    }

    input.addEventListener('input', obfuscate);
    obfuscate();
    """
)

# 31. Emoji Picker and Search
create_project(
    "Emoji Picker and Search",
    "Fast Emoji Search & Copy",
    "Text & Analysis",
    "😀",
    "Instant emoji lookup with click-to-copy clipboard integration.",
    """
    <div class="space-y-4">
        <input type="text" id="emojiSearch" placeholder="Search emojis (e.g. fire, rocket, heart)..." class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:ring-2 focus:ring-cyan-500 outline-none" />
        <div id="emojiGrid" class="grid grid-cols-6 sm:grid-cols-8 gap-2 max-h-64 overflow-y-auto p-2 bg-slate-950 border border-slate-700 rounded-2xl"></div>
        <div id="emojiNotice" class="text-xs text-center text-slate-400">Click any emoji to copy to clipboard!</div>
    </div>
    """,
    """
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
    """
)
