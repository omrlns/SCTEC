class Veiculo {
    constructor(fabricante, modelo, ano, cor) {
        // propriedades da classe
        this.fabricante = fabricante;
        this.modelo = modelo;
        this.ano = ano;
        this.cor = cor;
    }

    mostrarDadosVeiculo() {
        console.log(`${this.fabricante} ${this.modelo}, ${this.ano}, ${this.cor}`);
    }

    acelerar() {
        console.log("Acelerando...");
    }
}

class Moto extends Veiculo {
    constructor(fabricante, modelo, ano, cor) {
        super(fabricante, modelo, ano, cor);
    }
}



const minhaMoto = new Moto("Honda", "CB750 Hornet", 2026, "Branco");

minhaMoto.mostrarDadosVeiculo();
minhaMoto.acelerar();


class Carro extends Veiculo {
    constructor(fabricante, modelo, ano, cor, categoria, potencia) {
        super(fabricante, modelo, ano, cor);
        this.categoria = categoria;
        this.potencia = potencia;   
    }

    mostrarDadosVeiculo() {
        console.log(`${this.fabricante} ${this.modelo}, ${this.categoria}, ${this.potencia}, ${this.ano}, ${this.cor}`);
    }

}

const meuCarro = new Carro("Porsche", "911 Turbo", 2026, "Vermelho", "Sport", "771 cv");

meuCarro.mostrarDadosVeiculo();
meuCarro.acelerar();