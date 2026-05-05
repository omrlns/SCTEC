let calculadora = require("./common/Calculadora");

valorX = 10;
valorY = 2;

resultado = calculadora.somar(valorX, valorY);
console.log(`${valorX} + ${valorY} = ${resultado}`);

resultado = calculadora.subtrair(valorX, valorY);
console.log(`${valorX} - ${valorY} = ${resultado}`);

resultado = calculadora.multiplicar(valorX, valorY);
console.log(`${valorX} * ${valorY} = ${resultado}`);

resultado = calculadora.dividir(valorX, valorY);
console.log(`${valorX} / ${valorY} = ${resultado}`);
