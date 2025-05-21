//  Fazer um programa que leia uma frase e imprima somente as vogais. 

const frase = prompt("Digite uma frase sem acentos!").toLowerCase()
const vogais = ["a","e","i","o","u"] // poderia colocar letras com acento
let vogaisNaFrase = ""

for(i= 0 ; i < frase.length; i++){
    for(j= 0 ; j < vogais.length; j++){
        if(frase[i] === vogais[j]){
           vogaisNaFrase += frase[i]
        }
    }
}

console.log(vogaisNaFrase)