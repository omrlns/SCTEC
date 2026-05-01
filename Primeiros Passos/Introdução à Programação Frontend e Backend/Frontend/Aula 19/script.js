function calcular() {
    let valorX = parseFloat(document.getElementById("valorX").value);
    let valorY = parseFloat(document.getElementById("valorY").value);
    let operador = document.getElementById("operadores").value;
    let resultado;
   
    switch (operador) {
        case "somar":
            resultado = (valorX + valorY).toFixed(2);
            break;
        case "subtrair":
            resultado = (valorX - valorY).toFixed(2);
            break;
        case "multiplicar":
            resultado = (valorX * valorY).toFixed(2);
            break;
        case "dividir":
            if (valorY == 0) {
                resultado = "Divisão por 0 é inválida!";
            } 
            else {
                resultado = (valorX / valorY).toFixed(2);
            }
            break;
        default:
            resultado = "Operador inválido! Tente novamente!"
    }

    document.getElementById("resultado").innerHTML = `Resultado da Operação: ${resultado}`;

}