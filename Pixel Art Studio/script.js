
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
    