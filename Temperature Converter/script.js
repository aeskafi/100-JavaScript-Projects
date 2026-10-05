const cInput = document.getElementById('cInput');
const cSlider = document.getElementById('cSlider');
const fInput = document.getElementById('fInput');
const fSlider = document.getElementById('fSlider');
const kInput = document.getElementById('kInput');
const kSlider = document.getElementById('kSlider');

function round(val) {
    return Math.round(val * 100) / 100;
}

function updateFromCelsius(c) {
    const f = (c * 9) / 5 + 32;
    const k = c + 273.15;

    cInput.value = round(c);
    cSlider.value = c;

    fInput.value = round(f);
    fSlider.value = f;

    kInput.value = round(k);
    kSlider.value = k;
}

function updateFromFahrenheit(f) {
    const c = ((f - 32) * 5) / 9;
    const k = c + 273.15;

    cInput.value = round(c);
    cSlider.value = c;

    fInput.value = round(f);
    fSlider.value = f;

    kInput.value = round(k);
    kSlider.value = k;
}

function updateFromKelvin(k) {
    if (k < 0) k = 0;
    const c = k - 273.15;
    const f = (c * 9) / 5 + 32;

    cInput.value = round(c);
    cSlider.value = c;

    fInput.value = round(f);
    fSlider.value = f;

    kInput.value = round(k);
    kSlider.value = k;
}

function init() {
    cSlider.addEventListener('input', (e) => updateFromCelsius(parseFloat(e.target.value)));
    cInput.addEventListener('input', (e) => {
        const val = parseFloat(e.target.value);
        if (!isNaN(val)) updateFromCelsius(val);
    });

    fSlider.addEventListener('input', (e) => updateFromFahrenheit(parseFloat(e.target.value)));
    fInput.addEventListener('input', (e) => {
        const val = parseFloat(e.target.value);
        if (!isNaN(val)) updateFromFahrenheit(val);
    });

    kSlider.addEventListener('input', (e) => updateFromKelvin(parseFloat(e.target.value)));
    kInput.addEventListener('input', (e) => {
        const val = parseFloat(e.target.value);
        if (!isNaN(val)) updateFromKelvin(val);
    });

    // Default initialization to 25°C
    updateFromCelsius(25);
}

window.addEventListener('DOMContentLoaded', init);
