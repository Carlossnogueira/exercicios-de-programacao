/*
Faça um programa que dada a idade de um nadador, classifique-o em uma das seguintes categorias: 
- Infantil A = 5 a 7 anos 
- Infantil B = 8 a 11 anos 
- Juvenil A = 12 a 13 anos 
- Juvenil B = 14 a 17 anos 
- Adultos = Maiores de 18 anos
*/

let idade = parseInt(prompt("Entre a idade do nadador:") || "0");

if (idade >= 5 && idade <= 7) {
    console.log("Categoria Infantil A");
} else if (idade >= 8 && idade <= 11) {
    console.log("Categoria Infantil B");
} else if (idade >= 12 && idade <= 13) {
    console.log("Categoria Juvenil A");
} else if (idade >= 14 && idade <= 17) {
    console.log("Categoria Juvenil B");
} else if (idade >= 18) {
    console.log("Categoria Adultos");
} else {
    console.log("Sem categoria.");
}
