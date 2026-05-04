const input = document.getElementById("tarefaInput");
const botao = document.getElementById("btnAdicionar");
const lista = document.getElementById("listaTarefas");

function adicionarTarefa() {
    const novaTarefa = input.value;

    // verifica se o campo não está vazio
    if (novaTarefa.trim() !== "") {

        const novoItem = document.createElement("li");
        novoItem.textContent = novaTarefa;
        lista.appendChild(novoItem);

        input.value = ""; // limpa o campo de input após adicionar a tarefa
        input.focus(); // coloco o foco de volta no input e o prepara para a próxima tarefa

    } else {
        alert("Por favor, digite uma tarefa!")
    } 
}

// adicionando o evento de clique no botão
botao.addEventListener("click", adicionarTarefa);

// adicionar tarefa ao apertar a tecla "enter"
input.addEventListener("keypress", function(evento) {
    if (evento.key === "Enter") {
        adicionarTarefa();
    }
})