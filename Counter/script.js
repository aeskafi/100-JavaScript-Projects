const init = () => {
    let number = document.querySelector('#number');
    let buttons = document.querySelectorAll('button');

    buttons.forEach(function (btn) {
        btn.addEventListener('click', function (e) {
            var counter = number.innerText;
            if (e.target.innerText === '+') counter++; else counter--;
            if (e.target.innerText === 'Reset!') counter = 0;
            number.innerText = counter;
        })
    });
}

window.addEventListener('DOMContentLoaded', init)