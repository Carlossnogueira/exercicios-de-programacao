
/*
    Leia 2 vetores de inteiros V1 e V2 de N componentes cada (no máximo 50). Determine e imprima quantas vezes 
    que V1 e V2 possuem valores idênticos nas mesmas posições. 
*/



let list1: number[] = []
let list2: number[] = []
let quantNumerosIguais: number = 0
let numerosIguais: string = ""

// Decidi fazer esse exercicio com números aleatórios
function random(){
    let random:number = Math.round(Math.random() * 50)
    return random
}

for(let i = 0;i < 50; i++){
    list1[i] = random()
    list2[i] = random()
    console.log(list1[i])
    console.log(list2[i])
}

for(let i = 0;i < 50; i++){
   if(list1[i] === list2[i]){
    
    quantNumerosIguais++
    numerosIguais += " " + list1[i] + ","
   }
}

console.log(`Quantidade de números iguais: ${quantNumerosIguais}`)
console.log(`Numeros iguais: ${numerosIguais}`)
