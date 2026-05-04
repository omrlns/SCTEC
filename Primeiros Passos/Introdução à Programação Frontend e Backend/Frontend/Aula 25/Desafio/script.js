function clientePedido() {
    const numPedido = document.getElementById("numPedido").value;

    switch (numPedido) {
        case "1":
            return alert(`Pedido #${numPedido}: PIZZA DE CALABRESA.`);
            break;
        case "2":
            return alert(`Pedido #${numPedido}: PIZZA DE QUATRO QUEIJOS.`);
            break;
        case "3":
            return alert(`Pedido #${numPedido}: PIZZA DE FRANGO COM CATUPIRY.`);
            break;
        case "4":
            return alert(`Pedido #${numPedido}: PIZZA DE BRIGADEIRO.`);
            break;
        default:
            return alert(`Número do Pedido é INVÁLIDO!`);
    }
}