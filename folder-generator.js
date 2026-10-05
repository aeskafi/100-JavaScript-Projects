const fs = require('fs');
const path = require('path');

const ignoreList = ['.git', 'node_modules', '.github', 'dist', 'build', 'scripts'];
const repoTitle = '100 JavaScript Projects';

const root = __dirname;
const directories = fs.readdirSync(root).filter(file => {
    const fullPath = path.join(root, file);
    return fs.statSync(fullPath).isDirectory() && !ignoreList.includes(file);
}).sort((a, b) => a.localeCompare(b));

console.log(`Found ${directories.length} micro-apps.`);

function getMeta(dir) {
    const lower = dir.toLowerCase();
    let category = 'Utilities';
    let icon = '⚡';

    if (lower.includes('calc') || lower.includes('interest') || lower.includes('loan') || lower.includes('tip') || lower.includes('discount') || lower.includes('currency') || lower.includes('percentage') || lower.includes('matrix') || lower.includes('quadratic') || lower.includes('factorial') || lower.includes('statistic') || lower.includes('prime') || lower.includes('age') || lower.includes('counter')) {
        category = 'Math & Finance';
        icon = '🧮';
    } else if (lower.includes('timer') || lower.includes('clock') || lower.includes('stopwatch') || lower.includes('pomodoro')) {
        category = 'Time & Focus';
        icon = '⏳';
    } else if (lower.includes('convert') || lower.includes('morse') || lower.includes('roman') || lower.includes('binary') || lower.includes('unit') || lower.includes('temp')) {
        category = 'Converters';
        icon = '🔄';
    } else if (lower.includes('text') || lower.includes('word') || lower.includes('markdown') || lower.includes('slug') || lower.includes('case') || lower.includes('lorem') || lower.includes('palindrome') || lower.includes('emoji')) {
        category = 'Text & Strings';
        icon = '✍️';
    } else if (lower.includes('game') || lower.includes('toe') || lower.includes('scissors') || lower.includes('snake') || lower.includes('mole') || lower.includes('hangman') || lower.includes('simon') || lower.includes('puzzle') || lower.includes('hanoi') || lower.includes('mine') || lower.includes('connect') || lower.includes('quiz') || lower.includes('2048') || lower.includes('guess') || lower.includes('flip') || lower.includes('scramble') || lower.includes('reaction')) {
        category = 'Games & Puzzles';
        icon = '🎮';
    } else if (lower.includes('audio') || lower.includes('piano') || lower.includes('drum') || lower.includes('sound') || lower.includes('metro') || lower.includes('noise') || lower.includes('speech')) {
        category = 'Audio & Music';
        icon = '🎵';
    } else if (lower.includes('css') || lower.includes('shadow') || lower.includes('glass') || lower.includes('radius') || lower.includes('grid') || lower.includes('flex') || lower.includes('neu') || lower.includes('clip') || lower.includes('contrast') || lower.includes('ratio') || lower.includes('wave') || lower.includes('animat')) {
        category = 'CSS & Design';
        icon = '🎨';
    } else if (lower.includes('canvas') || lower.includes('paint') || lower.includes('pixel') || lower.includes('draw') || lower.includes('particle') || lower.includes('firework') || lower.includes('palette') || lower.includes('gradient') || lower.includes('meme') || lower.includes('ascii')) {
        category = 'Graphics & Canvas';
        icon = '🖌️';
    } else if (lower.includes('todo') || lower.includes('note') || lower.includes('kanban') || lower.includes('habit') || lower.includes('expense') || lower.includes('bookmark') || lower.includes('flashcard') || lower.includes('speed') || lower.includes('typing') || lower.includes('affirmation')) {
        category = 'Productivity';
        icon = '🚀';
    } else if (lower.includes('life') || lower.includes('tree') || lower.includes('matrix') || lower.includes('sort')) {
        category = 'Simulations';
        icon = '🧬';
    } else if (lower.includes('pass') || lower.includes('base64') || lower.includes('url') || lower.includes('rot13') || lower.includes('obfusc') || lower.includes('validator') || lower.includes('json') || lower.includes('regex') || lower.includes('diff')) {
        category = 'Security & DevTools';
        icon = '🔐';
    }

    return { category, icon };
}

const cardsHtml = directories.map((dir, idx) => {
    const meta = getMeta(dir);
    return `
            <a href="${encodeURIComponent(dir)}/index.html" class="project-card group block bg-slate-800/90 hover:bg-slate-800 border border-slate-700/80 hover:border-cyan-500/60 rounded-2xl p-5 transition-all duration-200 hover:-translate-y-1 hover:shadow-xl hover:shadow-cyan-500/10">
                <div class="flex items-start justify-between mb-3">
                    <span class="text-2xl">${meta.icon}</span>
                    <div class="flex items-center gap-1.5">
                        <span class="text-[10px] font-mono text-slate-500 font-bold">#${idx + 1}</span>
                        <span class="text-[10px] font-semibold px-2 py-0.5 rounded-full bg-slate-700/60 text-cyan-400 border border-slate-600/50">${meta.category}</span>
                    </div>
                </div>
                <h3 class="text-base font-bold text-white group-hover:text-cyan-400 transition-colors truncate">${dir}</h3>
                <div class="mt-3 flex items-center text-xs font-semibold text-cyan-400 group-hover:translate-x-1 transition-transform">
                    Launch App →
                </div>
            </a>
    `;
}).join('\n');

const fullHtml = `<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <title>${repoTitle} (100/100) | Arham Eskafi</title>
</head>

<body class="min-h-screen bg-slate-900 text-slate-100 flex flex-col font-sans selection:bg-cyan-500 selection:text-white">
    <!-- Header -->
    <header class="border-b border-slate-800 bg-slate-900/80 backdrop-blur sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 py-4 sm:px-6 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-500 to-blue-600 flex items-center justify-center font-black text-white text-xl shadow-lg shadow-cyan-500/20">
                    100
                </div>
                <div>
                    <h1 class="font-bold text-lg text-white leading-tight">${repoTitle}</h1>
                    <p class="text-xs text-slate-400">Curated by <a href="https://arham.dev" target="_blank" rel="noopener noreferrer" class="text-cyan-400 hover:underline">Arham Eskafi</a></p>
                </div>
            </div>
            <div class="flex items-center gap-3 text-sm">
                <a href="https://arham.dev" target="_blank" rel="noopener noreferrer" class="hidden sm:inline-block px-3 py-1.5 rounded-lg border border-slate-700 text-slate-300 hover:text-white hover:border-slate-500 transition">arham.dev</a>
                <a href="https://youtube.com/@walkcooklive" target="_blank" rel="noopener noreferrer" class="px-3 py-1.5 rounded-lg bg-rose-600 hover:bg-rose-500 text-white font-medium text-xs transition shadow flex items-center gap-1.5">
                    <span>▶ Walk Cook Live</span>
                </a>
            </div>
        </div>
    </header>

    <!-- Hero -->
    <main class="flex-1 max-w-7xl w-full mx-auto px-4 py-10 sm:px-6">
        <div class="text-center max-w-3xl mx-auto mb-10">
            <div class="inline-flex items-center gap-2 px-3 py-1 text-xs font-semibold rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/20 mb-4">
                <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                <span>100 of 100 Micro-Apps Fully Implemented</span>
            </div>
            <h2 class="text-3xl sm:text-5xl font-extrabold text-white tracking-tight">
                100 Vanilla JavaScript & Tailwind Micro-Apps
            </h2>
            <p class="mt-4 text-slate-400 text-base sm:text-lg">
                Complete collection of zero-dependency, ultra-fast interactive utilities, games, audio synthesizers, CSS generators, and math solvers.
            </p>

            <!-- Search input -->
            <div class="mt-8 max-w-md mx-auto relative">
                <input id="searchInput" type="text" placeholder="Search 100 apps by name or category..."
                    class="w-full bg-slate-800/90 border border-slate-700 rounded-2xl pl-11 pr-4 py-3 text-sm text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-cyan-500 transition shadow-lg" />
                <span class="absolute left-4 top-3.5 text-slate-400">🔍</span>
            </div>
        </div>

        <!-- Project Grid -->
        <div id="projectGrid" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
${cardsHtml}
        </div>
    </main>

    <!-- Footer -->
    <footer class="border-t border-slate-800 py-8 mt-12 bg-slate-950/60">
        <div class="max-w-7xl mx-auto px-4 text-center text-sm text-slate-500">
            <p>Crafted by <a href="https://arham.dev" class="text-cyan-400 hover:underline">Arham Eskafi</a> · Documenting the overland tech nomad journey on <a href="https://youtube.com/@walkcooklive" class="text-rose-400 hover:underline">Walk Cook Live</a></p>
        </div>
    </footer>

    <script>
        const searchInput = document.getElementById('searchInput');
        const cards = document.querySelectorAll('.project-card');

        searchInput.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase().trim();
            cards.forEach(card => {
                const text = card.textContent.toLowerCase();
                card.style.display = text.includes(query) ? 'block' : 'none';
            });
        });
    </script>
</body>
</html>
`;

fs.writeFileSync(path.join(root, 'index.html'), fullHtml);
console.log('Successfully generated index.html with all 100 projects!');
