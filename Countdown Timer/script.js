const exactDate = new Date('Dec 15, 2021 19:28:33').getTime();

var countDown = setInterval(() => {
    var distanceBetween = exactDate - new Date().getTime();
    // console.log(distanceBetween);
    // console.log(Math.floor(distanceBetween % 60000) / 1000);

    var second = Math.floor((distanceBetween % (1000 * 60)) / 1000);
    var minutes = Math.floor((distanceBetween % (1000 * 60 * 60)) / (60 * 1000));
    var hour = Math.floor((distanceBetween % (1000 * 60 * 60 * 24)) / (60 * 60 * 1000));
    var day = Math.floor(distanceBetween / (60 * 60 * 24 * 1000));
    if (distanceBetween < 0) {
        clearInterval(countDown)
    } else {
        document.getElementById('second').innerText = (second < 10 ? "0" : null) + second;
        document.getElementById('minutes').innerText = (minutes < 10 ? "0" : null) + minutes;
        document.getElementById('hour').innerText = (hour < 10 ? "0" : null) + hour;
        document.getElementById('day').innerText = (day < 10 ? "0" : null) + day;
    }

}, 1000);