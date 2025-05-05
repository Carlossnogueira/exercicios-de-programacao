/* 
Fazer um programa ler um vetor de inteiros e positivos e imprimir quantas vezes aparece o número 1, 3 e 4, nesta 
ordem. O vetor terá no máximo 100 posições. Sair do programa quando for digitado -1.
*/ 

let numeros:number[] = []
let um:number = 0
let tres:number = 0
let quatro:number = 0
let indice:number = 0

for(let i = 0; i < 100; i++ ){
    while(true){
        
        if(numeros.length <= 100){
            numeros[i] = parseInt(prompt(`Digite um número, digite -1 para finalizar!`) || "0")
        } else{
            alert("Lista cheia!")
            break
        }

        if(numeros[i] < -1){
            alert("Somente numeros positivos!")
            continue;
        }

        if(isNaN(numeros[i])){
            alert("Digite um número válido")!
        }

        if(numeros[i] === -1){
            break
        }

        if(numeros[i] === 1){
            um++
        }

        if(numeros[i] === 3){
            tres++
        }

        if(numeros[i] === 4){
            quatro++
        }
    }
    break;
}

console.log(`Vezes em que o número apareceu: 1 = ${um}, 3 = ${tres} e 4 = ${quatro}`)


