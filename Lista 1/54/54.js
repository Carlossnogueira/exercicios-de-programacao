/*
 Dado dois vetores, A (5 elementos) e B (8 elementos), faça um programa  que imprima todos os elementos 
comuns aos dois vetores. 
*/ 

const vet = [1, 2, 3, 4, 5];
const vet2 = [7, 8, 9, 6, 4, 3, 1, 5];

let msmElemento = [];

for (let i = 0; i < vet.length; i++) {
    for (let j = 0; j < vet2.length; j++) {
        if (vet[i] === vet2[j]) {
            msmElemento.push(vet[i]);
            break; 
        }
    }
}

console.log("Elementos comuns:", msmElemento);