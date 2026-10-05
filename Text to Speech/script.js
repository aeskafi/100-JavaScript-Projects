
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
    