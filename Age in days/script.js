const calculateAgeInDays = () => {
    const ageInput = document.getElementById('age');
    const resultElement = document.getElementById('ageInDays');
    const currentYear = new Date().getFullYear();
    const birthYear = parseInt(ageInput.value, 10);

    if (isNaN(birthYear) || birthYear < 1900 || birthYear > currentYear) {
        resultElement.innerText = 'Please enter a valid birth year (1900 - present).';
        resultElement.className = 'text-xl font-medium text-rose-500 text-center mt-4 transition-all';
        return;
    }

    const birthDate = new Date(birthYear, 0, 1);
    const today = new Date();
    const diffTime = Math.abs(today - birthDate);
    const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));

    resultElement.innerText = `You are approximately ${diffDays.toLocaleString()} days old! 🎉`;
    resultElement.className = 'text-2xl font-semibold text-emerald-600 text-center mt-4 transition-all';
};

document.getElementById('calculator').addEventListener('click', calculateAgeInDays);
document.getElementById('age').addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
        calculateAgeInDays();
    }
});