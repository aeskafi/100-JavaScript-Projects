document.getElementById('calculator').onclick = function () {

    var today = new Date().getFullYear();
    var age = document.getElementById('age').value;

    if ((age > today) || (age < 1900)) {

        document.getElementById("ageInDays").remove();

        var h1 = document.createElement('h1');
        var result = document.createTextNode('Mmmmm.');
        h1.setAttribute('id', 'ageInDays');
        h1.className = 'text-2xl text-red-600/70';
        h1.appendChild(result);
        document.getElementById('result').appendChild(h1);

    } else {

        document.getElementById("ageInDays").remove();

        var h1 = document.createElement('h1');
        var result = document.createTextNode('You are ' + ((today - age) * 365) + ' days old.');
        h1.setAttribute('id', 'ageInDays');
        h1.className = 'text-2xl text-green-600/80';
        h1.appendChild(result);
        document.getElementById('result').appendChild(h1);
    }

}