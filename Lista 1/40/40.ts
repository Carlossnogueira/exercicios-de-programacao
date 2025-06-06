/*
A  Secretaria  de  Meio  Ambiente  que  controla  o  índice  de  poluição  mantém  03  grupos  de  indústrias  que  são 
altamente  poluentes  do  meio  ambiente.  O  índice  de  poluição  aceitável  varia  de  0,05  até  0,25.  Se  o  índice  sobe 
para 0,3 as indústrias do 1º  grupo são intimadas a suspenderem suas atividades, se o índice crescer para 0,4 as 
industrias do 1º  e 2º  grupo  são intimadas a suspenderem suas atividades, se o índice atingir 0,5 todos os grupos 
devem  ser  notificados  a  paralisarem  suas  atividades.  Faça  um  programa  que  leia  o  índice  de  poluição  medido  e 
emita  a  notificação  adequada  aos  diferentes  grupos  de  empresas.  O  algoritmo  só  deve  parar  de  rodar  quando  o 
usuário responder "S" na seguinte pergunta, "Deseja encerrar o programa?".
*/

while(true){
    let input: number = parseFloat(prompt("Type the index of pollution") || "0");

    if(input <= 0.2){
        alert("All of industries can work!");
    }

    if(input == 0.3){
        alert("The industry of group one needs to stop its activity!");
    } 

    if (input == 0.4){
        alert("The industry of group one and two needs to stop its activity!");
    }

    if(input == 0.5){
        alert("All industries need to stop their activities!");
    }

    let exit: string = prompt("Need to finish?(S)")?.toLocaleLowerCase() || "0";
    
    if(exit == 'S'){
        break;
    } else{
        continue;
    }

}