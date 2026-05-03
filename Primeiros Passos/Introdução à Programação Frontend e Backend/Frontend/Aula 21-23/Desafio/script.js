const carros = ["Fusca", "Civic", "Mustang", "Lancer", "Uno"];
const conteudo = document.getElementById("conteudo");

function criarSecao(titulo, dados) {
    let secao = document.createElement("div");
    secao.innerHTML = "<h2>" + titulo + "</h2>" + dados;
    conteudo.appendChild(secao);
}

let i = 0;
let continuar = "S";

do {
    let dadoIndividual = "<p>Carro Atual: " + carros[i] + "</p>";
    criarSecao("Iteração Nº " + (i + 1), dadoIndividual);
    let resposta = prompt("Deseja ver o próximo carro? (S/N):");
    continuar = resposta ? resposta.toUpperCase() : "N";

    i++;
} while (continuar !== "N" && i < carros.length);