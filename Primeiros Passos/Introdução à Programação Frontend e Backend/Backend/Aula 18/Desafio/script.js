function calcularPrecoFinal() {
    const preco = document.getElementById("preco").value;
    const desconto = document.getElementById("desconto").value;

    if (preco >= 0 && desconto >= 0) {
        const precoFinal = preco - (preco * (desconto / 100));
        alert(`
            Preço Original: R$ ${Number(preco).toFixed(2)}
            Desconto: - R$ ${Math.abs(precoFinal - preco).toFixed(2)} (${desconto}% OFF)
            Preço Final: R$ ${precoFinal.toFixed(2)}
            `);
        console.log(`
            Preço Original: R$ ${Number(preco).toFixed(2)}
            Desconto: - R$ ${Math.abs(precoFinal - preco).toFixed(2)} (${desconto}% OFF)
            Preço Final: R$ ${precoFinal.toFixed(2)}
            `);
    }
    else {
        alert("O sistema não aceita valores negativos! Tente novamente!");
        console.log("O sistema não aceita valores negativos! Tente novamente!");
    }
}