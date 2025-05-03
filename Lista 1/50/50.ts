/*
Fazer  um  programa  que  sorteie  um  número  de  0  a  100  e  que  permita  que  o  usuário  (sem  conhecer  o  número 
sorteado)  tente  acertar.  Caso  não  acerte,  o  programa  deve  imprimir  uma  mensagem  informando  se  o  número 
sorteado é maior ou menor que a tentativa feita. Ao acertar o número, o programa deve imprimir a quantidade de 
tentativas feitas. 
*/ 

let random: number = Math.random() * 100
let listaTentativa: number[] = []

while(true){
    let tentativa = parseInt(prompt("Faça uma tentativa:") || "0")

    if(random === tentativa){
        listaTentativa.push(tentativa)
        console.log("Você acertou")
        break;
    } else{
        console.log("Você errou! Tente novamente!")
        listaTentativa.push(tentativa)
    }
}

console.log("Todos os chutes: ", dados(listaTentativa))

function dados(lista : number[]){
    let dados: string = ""
    lista.forEach((elemento) => {
        dados+= elemento + ","
    })
    return dados;
}