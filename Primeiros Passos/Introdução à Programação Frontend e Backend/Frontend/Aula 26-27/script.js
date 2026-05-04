const celulas = document.querySelectorAll(".celula");
let vezDoX = true; // isso define que é a vez do "x" jogar;

document.getElementById("btnRestart").addEventListener("click", iniciarJogo)


function iniciarJogo() {
    celulas.forEach(celula => {
        celula.textContent = "";
        celula.addEventListener("click", tratarClique, {once:true});
    })
}

function tratarClique(evento) {
    evento.target.textContent = vezDoX ? "❌" : "⭕";
    vezDoX = !vezDoX;
}

iniciarJogo();