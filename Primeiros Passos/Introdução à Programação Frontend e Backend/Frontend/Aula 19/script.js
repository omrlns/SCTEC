function trocarCor() {
    const elementA = document.getElementById("element-a");
    const elementB = document.getElementById("element-b");
    const elementC = document.getElementById("element-c");

    elementA.style.backgroundColor = "red";
    elementB.style.backgroundColor = "yellow";
    elementC.style.backgroundColor = "green";

}

function resetarCor() {
    const elementA = document.getElementById("element-a");
    const elementB = document.getElementById("element-b");
    const elementC = document.getElementById("element-c");

    elementA.style.backgroundColor = "";
    elementB.style.backgroundColor = "";
    elementC.style.backgroundColor = "";
}
