/* 
Durante  uma  corrida  de  automóveis  com  N  voltas  de  duração  foram  anotados  para  um  piloto,  na  ordem,  os 
tempos registrados em cada volta. Fazer um programa para ler os tempos das N voltas, calcular e imprimir: 
i. melhor tempo; 
ii. a volta em que o melhor tempo ocorreu; 
iii. tempo médio das N voltas; 
*/

let qutVoltas:number = 0
let tempoVoltas:number[] = []
let melhorVolta:number = 0
let somaTempo:number = 0

while(true){
    qutVoltas = parseInt(prompt("Digite a quantidade de voltas: ") || "0")
    if(isNaN(qutVoltas)){
        alert("Digite a quantidade de voltas para a contagem!")
        continue;
    }
    
    break;
}

for(let i =0; i < qutVoltas; i++){
    tempoVoltas[i] = parseFloat(prompt(`Digite o tempo da ${i+1} volta:`) || "0")
    
    if(isNaN(tempoVoltas[i])){
        alert("Digite um valor válido!")
        continue;
    }

    if(tempoVoltas[i] < 0.0){
        alert("Número inválido!")
        continue;
    }
}

let melhorTempo:number = tempoVoltas[0]

for(let i=0; i < qutVoltas; i++){
    if(tempoVoltas[i] < melhorTempo){
        melhorTempo = tempoVoltas[i]
        melhorVolta = i + 1
    }
    somaTempo += tempoVoltas[i]
}

console.log(`Melhor tempo foi ${melhorTempo} minutos na volta ${melhorVolta}.  O tempo médio das voltas é de ${somaTempo / qutVoltas}`)