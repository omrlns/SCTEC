// declaração da Promise com setTimeout()
function carregarProduto(id) {
    return new Promise((resolve, reject) => {
        // simula o atraso
        setTimeout(() => {
            if (id > 0) {
                const produto = { id: id, nome: "MacBook M4 Air", preco: 7500.00 };
                resolve(produto);
            } else {
                reject("O ID não corresponde a um produto!");
            }
        }, 2000);
    });
}

// consumo com .then() e manipulação de JSON
carregarProduto(1)
    .then((produto) => {
        try {
            // converte para JSON (string)
            const produtoJSON = JSON.stringify(produto);
            console.log("JSON Gerado:", produtoJSON);
            // reverte para objeto
            const produtoObjeto = JSON.parse(produtoJSON);
            console.log("Objeto Reverttido:", produtoObjeto);
        } catch (erro) {
            console.error(`Erro ao Processar o JSON: ${erro}`);
        }
    })
    .catch((erro) => {
        console.error(`Erro na Promise: ${erro}`)
    });

// refatoração com async/await
async function processarProdutoAsync(id) {
  try {
    console.log("Carregando Produto...");
    
    // aguarda a resolução da Promise
    const produto = await carregarProduto(id);

    // manipulação de JSON
    const produtoJSON = JSON.stringify(produto);
    console.log("JSON (Async/Await):", produtoJSON);

    const produtoObjeto = JSON.parse(produtoJSON);
    console.log("Objeto (Async/Await):", produtoObjeto);

  } catch (erro) {
    // lida com erros de rede (Promise) ou de parse (JSON)
    console.error("Ocorreu um Erro no Processo:", erro);
  }
}

processarProdutoAsync(1);