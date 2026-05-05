class Carro {
    constructor(marca, modelo, ano, cor) {
        // propriedades da classe
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
        this.cor = cor;
    }

    mostrarCarro() {
        let carro = {
            "marca": this.marca,
            "modelo": this.modelo,
            "ano": this.ano,
            "cor": this.cor
        }

        console.log(`INFORMAÇÕES DO CARRO
\nMARCA: ${carro['marca']}
\nMODELO: ${carro['modelo']}
\nANO: ${carro['ano']}
\nCOR: ${carro['cor']}`)
    }
}

const meuCarro = new Carro("Porsche", "911 Turbo", "2026", "Vermelho");
meuCarro.mostrarCarro()