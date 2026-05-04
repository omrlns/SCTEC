function mostrarSaudacao() {
    const nome = document.getElementById("nome").value;
    const perido = parseInt(document.getElementById("periodo").value, 10);
    const mensagem = document.getElementById("mensagem");
    mensagem.innerHTML = saudacaoPersonalizada(nome, perido);
}

function saudacaoPersonalizada(nome, perido) {
    if (perido < 12) {
        return `Olá ${nome}, bom dia!`;
    }
    else if (perido > 12 && perido < 18) {
        return `Olá ${nome}, boa tarde!`;
    }
    else if (perido > 18) {
        return `Olá ${nome}, boa noite!`;
    } 
    else {
        return "";
    }
}