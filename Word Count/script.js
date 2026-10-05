function getByteLength(str) {
    return new Blob([str]).size;
}

function analyzeText() {
    const text = document.getElementById('text').value;

    const chars = text.length;

    // Word count (splits by whitespace, filters out empty tokens)
    const wordsArray = text.trim().match(/\S+/g);
    const words = wordsArray ? wordsArray.length : 0;

    // Sentence count (. ! ? followed by space or end of string)
    const sentencesArray = text.match(/[^.!?]+[.!?]+(\s|$)/g);
    const sentences = sentencesArray ? sentencesArray.length : (chars > 0 ? 1 : 0);

    // Paragraph count (separated by double newlines or single non-empty newlines)
    const paragraphsArray = text.split(/\n+/).map(p => p.trim()).filter(p => p.length > 0);
    const paragraphs = paragraphsArray.length;

    // Reading time: average 200 words per minute
    const readingMinutes = Math.ceil(words / 200);
    const readingTime = words === 0 ? '0m' : `${readingMinutes}m`;

    // Byte size formatting
    const bytes = getByteLength(text);
    let byteFormatted = `${bytes} B`;
    if (bytes >= 1024 * 1024) {
        byteFormatted = `${(bytes / (1024 * 1024)).toFixed(2)} MB`;
    } else if (bytes >= 1024) {
        byteFormatted = `${(bytes / 1024).toFixed(2)} KB`;
    }

    document.getElementById('words').innerText = words.toLocaleString();
    document.getElementById('chars').innerText = chars.toLocaleString();
    document.getElementById('sentences').innerText = sentences.toLocaleString();
    document.getElementById('paragraphs').innerText = paragraphs.toLocaleString();
    document.getElementById('readingTime').innerText = readingTime;
    document.getElementById('byteSize').innerText = byteFormatted;
}

function init() {
    const textarea = document.getElementById('text');
    const clearBtn = document.getElementById('clearBtn');

    textarea.addEventListener('input', analyzeText);
    clearBtn.addEventListener('click', () => {
        textarea.value = '';
        analyzeText();
        textarea.focus();
    });

    analyzeText();
}

window.addEventListener('DOMContentLoaded', init);