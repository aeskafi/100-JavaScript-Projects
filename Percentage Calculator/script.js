const init = () => {
    document.getElementById('x_1').focus();

    Array.from(document.getElementsByTagName('button')).forEach(btn => {
        btn.addEventListener('click', (e) => calculateIt(e))
    })

    Array.from(document.getElementsByTagName('input')).forEach(inputs => {
        inputs.value = "";
    })

    Array.from(document.getElementsByClassName('inp')).forEach(result => {
        result.innerText = "";
    })
}

function calculateIt(e) {

    if (e.target.id === 'c_1') {
        // What is x% of y?
        // Math formula is :
        // x * (y/100)
        var x = Math.floor(document.getElementById('x_1').value);
        var y = Math.floor(document.getElementById('y_1').value);
        document.getElementById('z_1').innerText = resolver(
            x, y, "x * (y/100)");
    }

    if (e.target.id === 'c_2') {
        // x is what percent of y ?
        // Math formula is :
        // divide X by Y, and then multiply the result by 100
        var x = Math.floor(document.getElementById('x_2').value);
        var y = Math.floor(document.getElementById('y_2').value);
        document.getElementById('z_2').innerText = resolver(
            x, y, "(x/y) * 100");
    }
    if (e.target.id === 'c_3') {
        // What is the percentage increase/decrease from x to y ?
        // Math formula is :
        // Increment in x , I = y - x ,
        // increment per unit x , i = I/x ,
        // Increment per 100 units of x , P = i . 100 ,
        // So, % increase in x , P = 100 ( y-x)/x.
        var x = Math.floor(document.getElementById('x_3').value);
        var y = Math.floor(document.getElementById('y_3').value);
        document.getElementById('z_3').innerText = resolver(
            x, y, "100 * ((y-x) /x)");
    }

}

function resolver(x, y, formula) {
    return eval(formula.replace(/x/g, x).replace(/y/g, y));
}

window.addEventListener('DOMContentLoaded', init)