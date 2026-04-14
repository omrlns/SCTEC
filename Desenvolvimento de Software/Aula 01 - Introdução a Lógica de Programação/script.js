// console.log("Olá, SCTEC!"); // mensagem de saudação sem valor salvo em variável
var mensagem = "Olá, SCTEC!";
// console.log(mensagem); // mensagem de saudação com valor salvo em variável

// tipos de dados
// var é um tipo usado de forma global
// let é um tipo usado por escopo (forma mais recomendada)
let nome = "Marlon";
let idade = 22;
// vardadeiro ou falso (true ou false)
let empregado = true;
const sobrenome = "da Silva";

empregado = false;
// sobrenome = "da Rosa"; // uma variável constante não pode ser reatribuída

console.log("Nome: " + nome + " " + sobrenome);
console.log("Idade: " + idade);
console.log("Empregado: " + empregado);
console.log("");

// operadores aritméticos
let numero1 = 10;
let numero2 = 5;

console.log("Os números escolhidos para as operações são: " + numero1 + " e " + numero2);
console.log("Adição (+): " + (numero1 + numero2));
console.log("Subtração (-): " + (numero1 - numero2));
console.log("Divisão (/): " + (numero1 / numero2));
console.log("Multiplicação (*): " + (numero1 * numero2));
console.log("Divisão Inteira (//): " + ((numero1 / numero2) | 0));
console.log("Resto de Divisão (%): " + (numero1 % numero2));
console.log("");

numero1 = 5
numero2 = 3

// saída de dados com template string
console.log(`Os números escolhidos para as operações são: ${numero1} e ${numero2}`);
console.log(`Adição (+): ${numero1 + numero2}
Subtração (-): ${numero1 - numero2}
Divisão (/): ${(numero1 / numero2).toFixed(2)} 
Multiplicação (*): ${numero1 * numero2}
Divisão Inteira (//): ${(numero1 / numero2) | 0}
Resto de Divisão (%): ${numero1 % numero2}`);
console.log("")
// .toFixed(2) é usado para limitar a quantidade de casas decimais depois da vírgula

// operadores lógicos
// || or (ou) exemplo: true || true = true
// && and (e) exemplo: false && true = false
// ! (não) exemplo: !true = false

let alunoCadastrado = true;
let alunoGraduado = false;

console.log(alunoCadastrado || alunoGraduado);
console.log(alunoCadastrado && alunoGraduado);
console.log(!alunoCadastrado, !alunoGraduado);

