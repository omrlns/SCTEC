function setBackgroundColor(color) {
    document.body.style.backgroundColor = color;
}

document.getElementById("red-button").addEventListener("click", function () { setBackgroundColor("red") });
document.getElementById("green-button").addEventListener("click", function () { setBackgroundColor("green") });
document.getElementById("blue-button").addEventListener("click", function () { setBackgroundColor("blue") });

document.getElementById("input-box").addEventListener("keypress", function (event) {
    alert(`Tecla Pressionada: ${(event.key).toUpperCase()}`)
});