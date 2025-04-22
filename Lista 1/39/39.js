/*
Faça um programa que leia um número inteiro e mostre uma mensagem indicando se este número é par ou ímpar, 
e  se  é  positivo  ou  negativo.  O  programa  só  deve  parar  de  rodar  quando  o  usuário  responder  "S"  na  seguinte 
pergunta, "Deseja encerrar o programa?" .
*/ 

while(true){
    let numero = parseInt(prompt("Digite um número inteiro: "));

    if(numero => 0){
        alert(`O número ${numero} é positivo!`);
    } else {
        alert(`O número ${numero} é negativo!`);
    }

    if(numero % 2 > 0.1){
        alert(`O número ${numero} é impar!`);
    } else {
        alert(`O número ${numero} é par!`);
    }

    let opcao = prompt("Deseja encerrar o programa? (S/s)").toLocaleLowerCase();

    if(opcao == "s"){
        break;
    } else{
        continue;
    }

}