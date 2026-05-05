class Produto {
    constructor(nome, preco) {
        this.nome = nome;
        this.preco = preco;
    }

    mostrarDetalhes() {
        console.log(`Produto: ${this.nome}\nPreço: R$ ${this.preco}`);
    }
}

const produto = new Produto("Bicicleta", 740.25);
produto.mostrarDetalhes();

class Eletronico extends Produto {
    constructor(nome, preco, garantia) {
        super(nome, preco);
        this.garantia = garantia;
    }

    mostrarDetalhes() {
        console.log(`Produto: ${this.nome}\nPreço: R$ ${this.preco}\nGarantia: ${this.garantia} ano(s).`);
    }
}

const eletronico = new Eletronico("MacBook M4 Air", 7500.00, 1);
eletronico.mostrarDetalhes()