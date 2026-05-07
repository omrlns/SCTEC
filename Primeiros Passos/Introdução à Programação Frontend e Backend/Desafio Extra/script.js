// seleção dos elementos do DOM
const formElemento = document.getElementById("contactForm");
const feedbackElemento = document.getElementById("formFeedback");

// ouvinte de evento para o envio do formulário
formElemento.addEventListener("submit", (event) => {
    // previne o comportamento padrão de recarregar a página
    event.preventDefault();

    // limpa mensagens de feedback anteriores
    feedbackElemento.textContent = "";
    feedbackElemento.className = "feedback_mensagem";

    // captura dos valores dos campos (Requisito 5)
    const nome = document.getElementById("nome").value.trim();
    const email = document.getElementById("email").value.trim();
    const mensagem = document.getElementById("mensagem").value.trim();

    // validação básica de campos (Requisito 5: obrigatório e formato) [cite: 176]
    let erros = [];

    if (nome === "") {
        erros.push("O campo Nome é obrigatório.");
    }

    // validação simples de formato de email (presença de @ e .)
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (email === "") {
        erros.push("O campo Email é obrigatório.");
    } else if (!emailRegex.test(email)) {
        erros.push("Por favor, insira um formato de e-mail válido.");
    }

    if (mensagem === "") {
        erros.push("O campo Mensagem é obrigatório.");
    }

    // processamento do resultado da validação
    if (erros.length > 0) {
        // exibe o primeiro erro encontrado
        feedbackElemento.textContent = erros[0];
        feedbackElemento.classList.add("error");
        console.error("Falha na validação do formulário:", erros);
    } else {
        // simulação de sucesso (já que é apenas front-end)
        feedbackElemento.textContent = "Obrigado! Sua mensagem para a Belinha foi enviada com sucesso.";
        feedbackElemento.classList.add("success");
        console.log("Dados do Formulário prontos para envio:", { nome, email, mensagem });
        
        formElemento.reset();
    }
});