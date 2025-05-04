/*
Fazer um programa para ler uma quantidade N de alunos. Ler a nota de cada um dos N alunos e calcular a média 
aritmética  das  notas.  Contar  quantos  alunos  estão  com  a  nota  acima  de  7.0.  Obs.:  Se  nenhum  aluno  tirou  nota 
acima de 5.0, imprimir mensagem: Não há nenhum aluno com nota acima de 5.
*/

let qutAlunos = 0;
let prova1: number[] = []
let prova2: number[] = []
let alunosAprovados: number = 0

while(true){
    qutAlunos = parseInt(prompt('Digite a quantidade de alunos:') || "0")
    if(qutAlunos > 0){
        break;
    } else{
        alert("Entrada inválida")
    }
}

for(let i = 0; i < qutAlunos; i++){
    while(true){
        prova1[i] = parseInt(prompt(`Aluno de número ${i}: Digite a nota da primeira prova do aluno:`) || "0")
        prova2[i] = parseInt(prompt(`Aluno de número ${i}: Digite a nota da segunda prova do aluno:`) || "0")

       if(isNaN(prova1[i]) ||isNaN(prova1[i]) ){
            alert("valor inválido!")
       } else{
        break;
       }
    } 
}

for(let i = 0; i < qutAlunos; i++){
    let temp: number = (prova1[i] + prova2[i]) / 2
    if(temp >= 5){
        alunosAprovados++
    }
}

if(alunosAprovados >= 1){
    console.log(`Alunos aprovados = ${alunosAprovados}`)
} else {
    console.log("Nenhum aluno aprovado")
}