const tituloElemento = document.querySelector("h1");
// tituloElemento.innerText = "SCTEC - Aula 04";
// tituloElemento.innerHTML = "<span>SCTEC - Aula 04</span>";

const secaoSobreElemento = document.getElementById("sobre");
secaoSobreElemento.innerHTML = "<h4> - INTERATIVIDADE WEB COM JAVASCRIPT - <h4/>";

const buttonElemento = document.querySelector(".btn");
// buttonElemento.classList.add("inativo");

// secaoSobreElemento.innerHTML = "<h6>loremloremloremloremlorem</h6>"
const subtitulo = document.createElement("h6");
subtitulo.innerText = "< loremloremloremloremlorem >";
secaoSobreElemento.appendChild(subtitulo);

const inputTask = document.querySelector("#campoNome");
const buttonEnviar = document.querySelector("#botaoClique");

const secaoListElemento = document.getElementById("list");


buttonEnviar.addEventListener("click", (event) => {
    const valorInput = inputTask.value; // pega o valor que foi passado no input

    if (valorInput === "") {
        alert("POR FAVOR, digite uma tarefa!");
    } else {
        const spanElemento = document.createElement("span");
        spanElemento.classList.add("item-tarefa");
        // spanElemento.style.display = "block";
        // spanElemento.style.marginBottom = "8px";
        spanElemento.innerText = valorInput;
        
        secaoListElemento.appendChild(spanElemento);
        
        inputTask.value = "";
    }
});