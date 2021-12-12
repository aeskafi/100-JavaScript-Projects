const operatorButtons = ["AC", "±", "%", "+", "7", "8", "9", "x", "4", "5", "6", "-", "1", "2", "3", "+", "0", ".", "="];
// <input type="button" id="ac" value="AC" onclick="alert('hello');" />
operatorButtons.forEach(element => {
    var btn = document.createElement('button');

    // zero button need to be wider than another buttons
    if (element === "0") btn.style.gridColumn = 'span 2';

    var btnCaption = document.createTextNode(element);
    btn.appendChild(btnCaption);
    btn.className = "text-white text-4xl border-white border-2 bg-slate-500";

    document.getElementById("operatorContainer").appendChild(btn);
});
