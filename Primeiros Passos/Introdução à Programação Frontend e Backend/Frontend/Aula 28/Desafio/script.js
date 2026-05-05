document.getElementById('btnValidar').addEventListener('click', function() {

    const email = document.getElementById('email').value;
    const telefone = document.getElementById('telefone').value;
    const senha = document.getElementById('senha').value;

    const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    
    // telefone: aceita (XX) 9XXXX-XXXX ou XXXXXXXXXXX (10 ou 11 dígitos)
    const regexTelefone = /^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$/;
    
    // senha: mínimo 6 caracteres, pelo menos uma letra e um número
    const regexSenha = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$/;

    let mensagens = [];

    if (!regexEmail.test(email)) {
        mensagens.push("E-MAIL INVÁLIDO.");
    }

    if (!regexTelefone.test(telefone)) {
        mensagens.push("TELEFONE INVÁLIDO: \n       (USE O FORMATO: (99) 99999-9999).");
    }

    if (!regexSenha.test(senha)) {
        mensagens.push("SENHA PRECISA TER NO MÍN. 6 CARACTERES, LETRAS E NÚMEROS.");
    }

    // resultado para o usuário
    if (mensagens.length === 0) {
        alert("Sucesso! Todos os campos foram preenchidos corretamente.");
    } else {
        alert(`ERRO NA VALIDAÇÃO: \n* ${mensagens.join("\n* ")}`)
    }
});