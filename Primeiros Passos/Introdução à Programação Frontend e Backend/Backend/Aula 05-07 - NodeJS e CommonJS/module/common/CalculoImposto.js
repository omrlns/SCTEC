let taxa = 0.10;

exports.valor = function(x) {
    return x * taxa;
}

exports.adicionar = function(x) {
    return x + (x * taxa);
}