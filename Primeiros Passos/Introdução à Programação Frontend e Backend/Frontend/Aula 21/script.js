const carros = ["Ferrari Puro Sangue", "Lamborghini Urus", "Porshe 911 Turbo", "BMW X5"];
const conteudo = document.getElementById("conteudo");

let dados = "";
let i = 0;

while(i < 4) {
    dados += "<p>" + carros[i] + "</p>";
    i++;
}

const secao = document.createElement("div");
secao.innerHTML = "<h2>Loop While</h2>" + dados;
conteudo.appendChild(secao);