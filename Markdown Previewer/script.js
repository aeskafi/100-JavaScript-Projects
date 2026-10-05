
    const input = document.getElementById('mdInput');
    const output = document.getElementById('mdOutput');

    function parseMarkdown(md) {
        let html = md
            .replace(/^### (.*$)/gim, '<h3 class="text-lg font-bold text-cyan-400 mt-2 mb-1">$1</h3>')
            .replace(/^## (.*$)/gim, '<h2 class="text-xl font-bold text-cyan-300 mt-3 mb-1">$1</h2>')
            .replace(/^# (.*$)/gim, '<h1 class="text-2xl font-black text-white mt-4 mb-2">$1</h1>')
            .replace(/^\> (.*$)/gim, '<blockquote class="border-l-4 border-cyan-500 pl-3 my-2 text-slate-400 italic">$1</blockquote>')
            .replace(/\*\*(.*?)\*\*/gim, '<strong class="font-bold text-cyan-400">$1</strong>')
            .replace(/\*(.*?)\*/gim, '<em class="italic">$1</em>')
            .replace(/`(.*?)`/gim, '<code class="bg-slate-800 text-cyan-300 px-1 py-0.5 rounded text-xs font-mono">$1</code>')
            .replace(/\[(.*?)\]\((.*?)\)/gim, '<a href="$2" target="_blank" class="text-cyan-400 underline hover:text-cyan-300">$1</a>')
            .replace(/^\- (.*$)/gim, '<li class="ml-4 list-disc text-slate-300">$1</li>')
            .replace(/\n/gim, '<br/>');
        return html;
    }

    input.addEventListener('input', () => {
        output.innerHTML = parseMarkdown(input.value);
    });
    output.innerHTML = parseMarkdown(input.value);
    