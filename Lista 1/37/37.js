/*
Faça um programa de conversão de base numérica. O programa deverá apresentar uma tela de entrada com as 
seguintes opções: 
1 – Adição 
2 – Subtração 
3 – Multiplicação 
4 – Divisão 
Informe a opção: 
 
A  partir  da  opção  escolhida,  o  programa  deverá  solicitar  para  que  o  usuário  digite  dois  números.  Em  seguida,  o 
programa  deve  exibir  o  resultado  da  opção  indicada  pelo  usuário  e  perguntar  ao  usuário  se  ele  deseja  voltar  ao 
menu  principal.  Caso  a  resposta  seja   ́S ́  ou   ́s ́,  deverá  voltar  ao  menu,  caso  contrário  deverá  encerrar  o 
programa.
*/ 

let primeiroNumero = 0;
let segundoNumero = 0;
let resultado = 0;

while(true){
    let opcao = parseInt(prompt("1 – Adição\n 2 – Subtração\n 3 – Multiplicação\n 4 – Divisão\n Informe a opção:"));

    if(opcao <=0 || opcao >= 5){
        alert("Opção inválida!");
        continue;
    }

    primeiroNumero = parseFloat(prompt("Digite o primeiro número"));
    segundoNumero = parseFloat(prompt("Digite o segundo número"));

    if(isNaN(primeiroNumero)  && isNaN(segundoNumero)){
        alert("Entrada invalida inválida!");
        continue;
    }
  
    switch (opcao){
        case 1:
            resultado = primeiroNumero + segundoNumero;
            alert(`A soma dos números é de : ${resultado}`);
        break;
        case 2:
            resultado = primeiroNumero - segundoNumero;
            alert(`A subtração dos números é de : ${resultado}`);
        break;
        case 3:
            resultado = primeiroNumero * segundoNumero;
            alert(`A multiplicação dos números é de : ${resultado}`);
        break;
        case 4:
            resultado = primeiroNumero / segundoNumero;
            alert(`A divisão dos números é de : ${resultado.toFixed(2)}`);
        break;
    }

    let recomecar = prompt("Deseja voltar ao inicio? ('s' para recomeçar)").toLowerCase();

    if(recomecar == "s"){
        continue
    } else{
        break;
    }
     
}