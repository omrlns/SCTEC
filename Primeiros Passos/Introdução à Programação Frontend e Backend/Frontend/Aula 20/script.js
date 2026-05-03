const grupoA = ["Crystian", "Lauren", "Marlon", "Taíse"];
const grupoB = ["Davi", "Eduardo", "Lucas", "Vitor"];
const numeros = [3, 5, 29, 30];
const lista = ["Macarrão", "Lentilha", "Frango", "Farofa", "Iogurte", "Cenoura", "Pão", "Pasta de Amendoim", "Ovo"];

console.log(grupoA, grupoB);
console.log(`${grupoA[2]} <3 ${grupoA[3]}`);
console.log(numeros);
console.log(lista);
lista[3] = "Chocolate";

console.log(lista); // após a alteração, a lista vai imprimir "chocolate" na posição [3], ao invés de farofa

lista.push("Tomate");

console.log(lista); // após a inserção, a lista vai imprimir "tomate" no final da lista, como um novo item que contempla a lista

lista.pop(); // remove o último item da lista

console.log((lista).length); // retorna o tamanho da lista

console.log(); // saída: 9