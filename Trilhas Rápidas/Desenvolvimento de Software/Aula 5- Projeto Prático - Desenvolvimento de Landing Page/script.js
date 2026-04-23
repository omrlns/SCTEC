const formElemento = document.querySelector("form");
const inputsElementos = document.querySelectorAll("input");
const textAreaElemento = document.querySelector("textarea");

formElemento.addEventListener("submit", (event) => {
    event.preventDefault();

    let valores = [];

    inputsElementos.forEach((input) => {
        valores.push(input.value);
        // console.log(input.value);
    });

    valores.push(textAreaElemento.value);

    console.log("Dados do Formulário: ", valores);
});
