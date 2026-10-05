
    const form = document.getElementById('valForm');
    const user = document.getElementById('vUser');
    const email = document.getElementById('vEmail');
    const pass = document.getElementById('vPass');
    const success = document.getElementById('vSuccess');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        let valid = true;

        if (user.value.trim().length < 3) {
            document.getElementById('vUserErr').innerText = 'Username must be at least 3 characters.';
            document.getElementById('vUserErr').classList.remove('hidden');
            valid = false;
        } else {
            document.getElementById('vUserErr').classList.add('hidden');
        }

        const emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRe.test(email.value)) {
            document.getElementById('vEmailErr').innerText = 'Please enter a valid email address.';
            document.getElementById('vEmailErr').classList.remove('hidden');
            valid = false;
        } else {
            document.getElementById('vEmailErr').classList.add('hidden');
        }

        if (pass.value.length < 8) {
            document.getElementById('vPassErr').innerText = 'Password must be at least 8 characters.';
            document.getElementById('vPassErr').classList.remove('hidden');
            valid = false;
        } else {
            document.getElementById('vPassErr').classList.add('hidden');
        }

        success.classList.toggle('hidden', !valid);
    });
    