// Formula Reference
// (0°C × 9 / 5) + 32 = 32°F
// 0°C + 273.15 = 273.15K

function showValue(val, slidernum) {
    /* setup variables for the elements of our slider */
    var thumb = document.getElementById("sliderthumb" + slidernum);
    var shell = document.getElementById("slidershell" + slidernum);
    var track = document.getElementById("slidertrack" + slidernum);
    var fill = document.getElementById("sliderfill" + slidernum);
    var slider = document.getElementById("slider" + slidernum);
    var pc = val / (slider.max - slider.min); /* the percentage slider value */
    var thumbsize = 30; /* must match the thumb size in your css */
    var bigval = 300; /* widest or tallest value depending on orientation */
    var smallval = 30; /* narrowest or shortest value depending on orientation */
    var tracksize = bigval - thumbsize;
    var fillsize = 12;
    var filloffset = 7;
    var bordersize = 2;
    var loc = pc * tracksize;

    // document.getElementById("blur").setAttribute("stdDeviation", val / 10);
    thumb.style.top = "0px";
    thumb.style.left = loc + "px";
    fill.style.top = filloffset + bordersize + "px";
    fill.style.left = "0px";
    fill.style.width = loc + (thumbsize / 2) + "px";
    fill.style.height = fillsize + "px";
    shell.style.height = smallval + "px";
    shell.style.width = bigval + "px";
    track.style.height = fillsize + "px"; /* adjust for border */
    track.style.width = bigval - 4 + "px"; /* adjust for border */
    track.style.left = "0px";
    track.style.top = filloffset + bordersize + "px";

    document.getElementById("c").innerText = Math.floor(val) + " °C";
    document.getElementById("f").innerText = ((Math.floor(val) * 9 / 5) + 32) + " °F";
    document.getElementById("k").innerText = (Math.floor(val) + 273.15) + " °K";
}
/* we often need a function to set the slider values on page load */
function setValue(val, num) {
    document.getElementById("slider" + num).value = val;
    showValue(val, num);
}

setValue(0, 1);

