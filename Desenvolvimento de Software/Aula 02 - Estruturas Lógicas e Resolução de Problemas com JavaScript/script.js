// estruturas condicionais
// == (igual a)
// === (estritamente igual a)
// >, < (maior que, menor que)
// >=, <= (maior ou igual, menor ou igual)
// != (diferente de)
// !== (estritamente diferente de)

console.log(`"1" == 1: ${"1" == 1}`);
console.log(`"1" === 1: ${"1" === 1}`);
console.log(`20 > 20: ${20 > 20}`);
console.log(`20 <= 20: ${20 <= 20}`);
console.log(`1 != 2: ${1 != 2}`);
console.log(`1 !== "1": ${1 !== "1"}`);
console.log("");

let idade = 22;

// múltiplas decisões
if (idade === 18) {
    console.log("Você acabou de ficar maior de idade!");
} else if (idade > 18){
    console.log("É maior de idade!");
} else {
    console.log("É menor de idade!");
}

console.log("");

let periodo = "matutino";

// casos
switch (periodo) {
    case "matutino":
        console.log("Você estuda de manhã! Bom dia!")
        break;
    case "vespertino":
        console.log("Você estuda de tarde! Boa tarde!")
        break;
    case "noturno":
        console.log("Você estuda de noite! Boa noite!")
        break;
    default:
        console.log("Ah, você não estuda!")
        break;
}

console.log("");

// estruturas de repetição
for (let i = 0; i < 10; i++) {
    console.log(i + 1);
}

let frutas = ["Maracujá", "Maçã", "Uva", "Abacaxi", "Laranja"]

console.log(frutas) // imprime todas as frutas no console
console.log(frutas[0]) // Maracujá

console.log("");

// uma forma de percorrer todos os itens de uma lista
for (i in frutas) {
    console.log(frutas[i]);
}

console.log("");

console.log(`Tamanho da "Lista" de Frutas: ${frutas.length}`); // informa o tamanho da  lista

console.log("");

frutas.push("Banana"); // adicionando uma nova fruta na lista (por padrão, o novo item é adicionado ao final da lista)
console.log(frutas);

console.log("");

frutas.pop(); // remove um valor da lista (por padrão, remove o último item adicionado (pilha))
console.log(frutas);

let contador = 0;

console.log("");

while (contador <= 10) {
    if (contador > 0) {
        console.log(`Valor do Contador: ${contador}`);
    }
    contador += 1;
}

// function é uma palavra reservada
function quebraDeLinha() {
    console.log("");
}

quebraDeLinha();