const fs = require('fs');
const path = require('path');

const ignoreList = ['.git', 'node_modules', '.github', 'dist', 'build'];
const repoTitle = '100 JavaScript Projects';

const projectMetadata = {
    'Age in days': {
        title: 'Age in Days Calculator',
        description: 'Calculate your exact age in days since birth year with astronomical precision.',
        category: 'Math & Time',
        icon: '📅'
    },
    'Calculator': {
        title: 'Modern Calculator',
        description: 'Clean responsive calculator with keyboard support, percentage, and negative sign toggling.',
        category: 'Utility',
        icon: '🧮'
    },
    'Countdown Timer': {
        title: 'Countdown Timer',
        description: 'Real-time countdown clock with custom date picker and dynamic target tracking.',
        category: 'Math & Time',
        icon: '⏳'
    },
    'Counter': {
        title: 'Interactive Counter',
        description: 'Minimalist counter with state coloring and keyboard shortcuts (+, -, 0).',
        category: 'Utility',
        icon: '🔢'
    },
    'Percentage Calculator': {
        title: 'Percentage Suite',
        description: 'Three essential percentage formulas: fraction of total, percentage ratio, and delta percentage.',
        category: 'Finance & Math',
        icon: '📊'
    },
    'Temperature Converter': {
        title: 'Temperature Converter',
        description: 'Bi-directional synchronized converter supporting Celsius, Fahrenheit, and Kelvin with slider controls.',
        category: 'Converters',
        icon: '🌡️'
    },
    'Word Count': {
        title: 'Word & Text Analytics',
        description: 'Instant text metrics: word count, character count, paragraphs, estimated reading time, and byte size.',
        category: 'Text & Analysis',
        icon: '✍️'
    }
};

const root = __dirname;
const directories = fs.readdirSync(root).filter(file => {
    const fullPath = path.join(root, file);
    return fs.statSync(fullPath).isDirectory() && !ignoreList.includes(file);
});

const cardsHtml = directories.map(dir => {
    const meta = projectMetadata[dir] || {
        title: dir,
        description: 'Interactive vanilla JavaScript experiment.',
        category: 'General',
        icon: '⚡'
    };

    return `
            <a href="${encodeURIComponent(dir)}/index.html" class="project-card group block bg-slate-800/90 hover:bg-slate-800 border border-slate-700 hover:border-cyan-500/60 rounded-2xl p-6 transition-all duration-200 hover:-translate-y-1 hover:shadow-xl hover:shadow-cyan-500/10">
                <div class="flex items-start justify-between mb-4">
                    <span class="text-3xl">${meta.icon}</span>
                    <span class="text-xs font-semibold px-2.5 py-1 rounded-full bg-slate-700/60 text-cyan-400 border border-slate-600/50">${meta.category}</span>
                </div>
                <h3 class="text-lg font-bold text-white group-hover:text-cyan-400 transition-colors">${meta.title}</h3>
                <p class="text-sm text-slate-400 mt-2 line-clamp-2">${meta.description}</p>
                <div class="mt-4 flex items-center text-xs font-semibold text-cyan-400 group-hover:translate-x-1 transition-transform">
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
    <title>${repoTitle} | Arham Eskafi</title>
</head>

<body class="min-h-screen bg-slate-900 text-slate-100 flex flex-col font-sans selection:bg-cyan-500 selection:text-white">
    <!-- Header -->
    <header class="border-b border-slate-800 bg-slate-900/80 backdrop-blur sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-4 sm:px-6 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-500 to-blue-600 flex items-center justify-center font-black text-white text-xl shadow-lg shadow-cyan-500/20">
                    JS
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
    <main class="flex-1 max-w-6xl w-full mx-auto px-4 py-10 sm:px-6">
        <div class="text-center max-w-2xl mx-auto mb-12">
            <span class="inline-block px-3 py-1 text-xs font-semibold rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/20 mb-4">
                Open-Source Collection
            </span>
            <h2 class="text-3xl sm:text-5xl font-extrabold text-white tracking-tight">
                Vanilla JS & Tailwind Micro-Apps
            </h2>
            <p class="mt-4 text-slate-400 text-base sm:text-lg">
                High-performance, dependency-free interactive tools crafted with clean vanilla JavaScript and modern Tailwind CSS.
            </p>

            <!-- Search input -->
            <div class="mt-8 max-w-md mx-auto relative">
                <input id="searchInput" type="text" placeholder="Search projects by name or category..."
                    class="w-full bg-slate-800/90 border border-slate-700 rounded-2xl pl-11 pr-4 py-3 text-sm text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-cyan-500 transition" />
                <span class="absolute left-4 top-3.5 text-slate-400">🔍</span>
            </div>
        </div>

        <!-- Project Grid -->
        <div id="projectGrid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
${cardsHtml}
        </div>
    </main>

    <!-- Footer -->
    <footer class="border-t border-slate-800 py-8 mt-12 bg-slate-950/60">
        <div class="max-w-6xl mx-auto px-4 text-center text-sm text-slate-500">
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
console.log('Successfully generated index.html');
