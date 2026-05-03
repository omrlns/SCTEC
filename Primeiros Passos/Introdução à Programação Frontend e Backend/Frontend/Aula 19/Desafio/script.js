function traduzir() {
    let idioma = document.getElementById("idiomas").value;
    let saudacao = "";

    switch (idioma) {
        case "portugues":
            saudacao = "Olá, seja bem-vindo(a)!"
            break;
        case "ingles":
            saudacao = "Hello, welcome!"
            break;
        case "alemao":
            saudacao = "Hallo, willkommen!"
            break;
        case "espanhol":
            saudacao = "¡Hola, bienvenido(a)!"
            break;
        case "frances":
            saudacao = "Bonjour, bienvenue!"
            break;
        case "italiano":
            saudacao = "Ciao, benvenuto(a)!"
            break;
        case "grego":
            saudacao = "Γεια σας, καλώς ορίσατε!"
            break;
        case "russo":
            saudacao = "Привет, добро пожаловать!"
            break;
        case "japones":
            saudacao = "こんにちは、ようこそ！"
            break;
        case "chines":
            saudacao = "你好，欢迎！"
            break;
    }

    // lógica para exibir na tela
    const container = document.getElementById("resultado");
    const campoTexto = document.getElementById("texto-saudacao");
    const campoBandeira = document.getElementById("bandeira-pais");

    if (saudacao !== "") {
        campoTexto.innerText = saudacao;
        container.style.display = "block"; // torna o container visível
    }

}