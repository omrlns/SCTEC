const carros = ["Ferrari Puro Sangue", "Lamborghini Urus", "Porshe 911 Turbo", "BMW X5"];
const conteudo = document.getElementById("conteudo");

let dados;
let i;

function criarSecao(titulo, dados) {
    let secao = document.createElement("div");
    secao.innerHTML = "<h2>" + titulo + "</h2>" + dados;
    conteudo.appendChild(secao);
}

dados = "";
i = 0;

while (i < carros.length) {
    dados += "<p>" + carros[i] + "</p>";
    i++;
}

criarSecao("Loop While", dados);

dados = "";
i = 0;

do {
    dados += "<p>" + carros[i] + "</p>";
    i++;
} while (i < carros.length);

criarSecao("Loop DO-WHILE", dados);


carros.push("Koenigsegg Jesko");

dados = "";

for (i = 0; i < carros.length; i++) {
    dados += "<p>" + carros[i] + "</p>";
}

criarSecao("Loop For", dados);

dados = "";

for (carro of carros) {
    dados += "<p>" + carro + "</p>";
}

criarSecao("Loop For Of", dados);

let veiculoA = { 
    marca: 'Honda', modelo: "Civic Type-R", ano: 2023, cor: "Prata"
}

let veiculoB = { 
    marca: 'Mitsubishi', modelo: "Lancer Evo", ano: 2012, cor: "Preto"
}

let garagem = [];
garagem.push(veiculoA, veiculoB);
console.log(garagem);