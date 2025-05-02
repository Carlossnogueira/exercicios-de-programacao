/*
    Uma  agência  de  publicidade  pediu  à  agência  de  modelos  Luz  &  Beleza  para  encontrar  uma  modelo  que  tenha 
    idade  entre  18  e  20  anos  para  participar  de  uma  campanha  publicitária  milionária  de  produtos  de  beleza.  Foram 
    inscritas 20 candidatas e, ao se inscreverem, forneceram nome e idade. Tais informações foram armazenadas em 
    2  vetores  distintos.  Faça  um  programa  para  imprima  o  vetor  que  contém  os  nomes  das  candidatas  aptas  a 
    concorrer a uma vaga para a campanha milionária.
*/

let candidatas: string[] = []
let idadeCandidatas: number[] = []
const quantidadeCandidatas: number = 20

let i = 0

while (i < quantidadeCandidatas) {
    let candidata: string = prompt("Digite o nome da candidata: ") || "0"
    let idade: number = parseInt(prompt("Digite a idade da candidata: ") || "0")

    if (idade <= 20 && idade >= 18) {
        candidatas[i] = candidata
        idadeCandidatas[i] = idade
        console.log(`Candidata cadastrada: Nome: ${candidatas[i]}, Idade: ${idadeCandidatas[i]}`)
        i++
    } else {
        console.log("A candidata não tem idade permitida! Tente novamente.")
    }
}

console.log("--- Candidatas disponíveis: ---")
for (let i = 0; i < quantidadeCandidatas; i++) {
    console.log(`Nome: ${candidatas[i]}, Idade: ${idadeCandidatas[i]}`)
}