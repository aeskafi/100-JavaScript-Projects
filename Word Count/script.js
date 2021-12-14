function init() {
    var text = document.getElementById('text');
    var button = document.getElementById('pushIt');
    text.addEventListener('keyup', counting, false);
    button.addEventListener('click', () => { text.value = ""; reset() });
    counting();
}

function byteLength(str) {
    // returns the byte length of an utf8 string
    var s = str.length;
    for (var i = str.length - 1; i >= 0; i--) {
        var code = str.charCodeAt(i);
        if (code > 0x7f && code <= 0x7ff) s++;
        else if (code > 0x7ff && code <= 0xffff) s += 2;
        if (code >= 0xDC00 && code <= 0xDFFF) i--; //trail surrogate
    }
    return s;
}

function counting(e) {
    var chars, words, sentences, byteSize = "";
    chars = text.value && text.value.length;
    words = text.value.match(/(\w+)/g) !== null ? text.value.match(/(\w+)/g).length : 0;
    sentences = text.value.match(/[\w|\)][.?!](\s|$)/g) !== null ? text.value.match(/[\w|\)][.?!](\s|$)/g).length : 0;

    var g = text.value.split("\n\n").length;
    paragraphs = 0;
    var strip_whitespace = /\s+/gi;
    while (g >= 0) {
        g--;
        var tmp = text.value.split("\n\n")[g];
        tmp = tmp ? tmp.replace(strip_whitespace, "") : tmp;
        if (tmp && tmp.length > 1) {
            paragraphs++;
        }
    }

    byteSize = text.value && byteLength(text.value);

    reset(e, byteSize || 0, chars || 0, words, sentences, paragraphs);
}

function reset(e, byteSize = 0, chars = 0, words = 0, sentences = 0, paragraphs = 0) {
    document.getElementById('chars').innerText = `Characters: ${chars}`;
    document.getElementById('words').innerText = `Words: ${words}`;
    document.getElementById('sentences').innerText = `Sentences: ${sentences}`;
    document.getElementById('paragraphs').innerText = `Paragraphs: ${paragraphs}`;
    document.getElementById('byteSize').innerText = `Size: ${byteSize} (Byte)`;
    text.focus();
}

window.addEventListener('DOMContentLoaded', init);