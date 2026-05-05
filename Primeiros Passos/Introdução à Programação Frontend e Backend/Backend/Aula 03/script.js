// setTimeout e setInterval

function alerta() {
    // console.log("Alerta!");
}

// 1º modelo
setTimeout(alerta, 3000);

// 2º modelo
setTimeout(() => {
    // console.log("Alerta!");
}, 3000);


setInterval(() => {
    // console.log("Alerta!");
}, 3000);

console.log("---------- ÍNICIO DA EXECUÇÃO ----------")

function buscaDadosDoServidor() {
    // código que busca dados do servidor
    return new Promise((resolve, reject) => {
        console.log("Buscando Dados no Servidor...");

        setTimeout(() => {
            let sucesso = Math.random() > 0.5;

            if (sucesso) {
                resolve("Dados Recebidos com Sucesso!");
            } else {
                reject("Falha ao Buscar Dados no Servidor!");
            }
        }, 2000);
    });
}

buscaDadosDoServidor().then((mensagem) => {
    // console.log(mensagem);
}).catch((erro) => {
//   console.log(erro);  
});

const funcaoAssincrona = async () => {
    try {
        const resultado = await buscaDadosDoServidor();
        console.log(resultado);
    }
    catch(erro) {
        console.log(erro)
    }
}

funcaoAssincrona();

console.log("---------- FIM DA EXECUÇÃO ----------")