/*
Faça  um  programa  que  leia  as  variáveis  C  e  N,  respectivamente  código  e  número  de  horas  trabalhadas  de  um 
operário. E calcule o salário sabendo-se que ele ganha R$ 10,00 por hora. Quando o número de horas exceder a 
50,  calcule  o  excesso  de  pagamento  armazenando-o  na  variável  E,  caso  contrário  zerar  tal  variável.  A  hora 
excedente de trabalho vale R$ 20,00. No final do processamento imprimir o salário total e o salário excedente. O 
programa  só  deve  parar  de  rodar  quando  o  usuário  responder  "S"  na  seguinte  pergunta,  "Deseja  encerrar  o 
programa?". 
*/

let HoraExtra = 0;
let c = 0;
let n = 0;

while (true) {
    parseInt(prompt("Digite o código do funcionario (Apenas números)"));
    parentInt(prompt("Digite o número de horas trabalhadas"));

    if (n > 50) {
        HoraExtra = n - 50;
    } 
    
    console.log(`O salario do funcionario cujo o código é '${c}' é de:\n
        Salário base: R$${(n * 10).toFixed(2)},\n
        Horas extras: R$${HoraExtra * 20},\n
        Total: R$${((n*10) + HoraExtra * 20).toFixed(2)}.
        `);
    
    let opcao = prompt("Deseja finalizar o programa?").toLowerCase();

    if (opcao == 's'){
        break;
    } else{
        continue;
    }
   
}

