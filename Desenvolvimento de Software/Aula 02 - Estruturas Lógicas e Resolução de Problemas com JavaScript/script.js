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

console.log("")

// estruturas de repetição
for (let i = 0; i < 10; i++) {
    console.log(i + 1);
}

