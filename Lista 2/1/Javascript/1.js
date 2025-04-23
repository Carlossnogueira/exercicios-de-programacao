class Caneta {
    #marca
    #cor
    #tamanho

    constructor(marca, cor, tamanho) {
        this.#marca = marca
        this.#cor = cor
        this.#tamanho = tamanho
    }

    get marca() { return this.#marca }
    set marca(valor) { this.#marca = valor }

    get cor() { return this.#cor }
    set cor(valor) { this.#cor = valor }

    get tamanho() { return this.#tamanho }
    set tamanho(valor) { this.#tamanho = valor }

    toString() {
        return `Marca: ${this.#marca}, Cor: ${this.#cor}, Tamanho: ${this.#tamanho}`
    }
}


class CanetaTesteVetor{
    #canetas

    constructor(){
        this.#canetas = []
    }

    /**
     * 
     * @param {Caneta} Caneta 
     */
    cadastrarCaneta(Caneta){
        if(this.#canetas.length < 50){
            this.#canetas.push(Caneta)
        } else{
            console.log("Numero maximo atingido")
        }
    }

    exibirCanetas() {
        if (this.#canetas.length === 0) { 
            console.log("Nenhuma caneta cadastrada!");
        } else {
            console.log("Canetas cadastradas:");
            for (let i = 0; i < this.#canetas.length; i++) {
                console.log(`${i}.. ${this.#canetas[i].toString()}`)
            }
        }
    }

    exibirQuantidade(){
        if(this.#canetas.length === 0){
            console.log("0 canetas cadastradas")
        } else{
            console.log(`${this.#canetas.length} caneta(s) cadastradas no total!`)
        }
    }

    /**
     * 
     * @param {string} cor 
     */
    exibirPorCor(cor){
        if (this.#canetas.length === 0) { 
            console.log("Nenhuma caneta cadastrada!")
            return
        }

        let encontrou = false
        const corBusca = cor.toLowerCase();
        for(let i = 0; i < this.#canetas.length; i++){
            if (this.#canetas[i].cor.toLowerCase() === corBusca){
                console.log(`Caneta encontrada! ` + this.#canetas[i].toString())
                encontrou = true;
            }
        }

        if(encontrou === false){
            console.log("Nenhuma caneta encontrada com essa cor.")
        }

    }

}

const estoque_canetas = new CanetaTesteVetor();

while (true) {
    const entrada = prompt(
        "1 – Cadastrar caneta\n" +
        "2 – Exibir todas as canetas\n" +
        "3 – Exibir quantidade de canetas cadastradas\n" +
        "4 – Consultar quantidade de canetas de uma determinada cor\n" +
        "0 – Sair"
    );

    if (entrada === null) break; 

    switch (parseInt(entrada)) {
        case 1:
            const marca = prompt("Digite a marca:");
            const cor = prompt("Digite a cor:");
            const tamanho = prompt("Digite o tamanho:");
            const novaCaneta = new Caneta(marca, cor, tamanho);
            estoque_canetas.cadastrarCaneta(novaCaneta);
            break;

        case 2:
            estoque_canetas.exibirCanetas();
            break;

        case 3:
            estoque_canetas.exibirQuantidade();
            break;

        case 4:
            const corBusca = prompt("Digite a cor:");
            estoque_canetas.exibirPorCor(corBusca);
            break;

        case 0:
            alert("Saindo...");
            break;

        default:
            alert("Opção inválida");
    }

    if (entrada == 0) break;
}
