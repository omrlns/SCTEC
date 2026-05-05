let pessoa = require("./common/Pessoa");
let soma = require("./common/Soma");
let imposto = require("./common/CalculoImposto");

// marlon = pessoa();

console.log(pessoa());
console.log(soma(2, 3));
console.log(`\nValor do Produto com Imposto: R$ ${imposto.adicionar(10)}`);
console.log(`\nValor do Imposto: R$ ${imposto.valor(10)}`);
console.log(`\nTaxa do Imposto: ${imposto.taxa} %`); // o retorno foi um undefined porque aparentemente essa info é um valor "interno"
