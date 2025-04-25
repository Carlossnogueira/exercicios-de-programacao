// entrada
let maior:number | null = null
let menor:number | null = null

// loop
while(true){
    // entrada do valor
    let entrada:number = parseInt(prompt("Valor") || "0")

    // caso seja digitado algo sem ser numerico
    if(isNaN(entrada)){
        break
    }

    // se a entrada for 0
     if(entrada === 0){
        break;
    }

    // se o numero começar como 'vazio', coloca a entrada inicial
    if(maior === null || menor === null){
        maior = entrada
        menor = entrada
    } 
    // se não, fazemos as comparações
    else {
        if(entrada > maior){
                maior = entrada
            }
        if(entrada < menor){
            menor = entrada
        }
    }
 
}

console.log(`maior: ${maior}, menor: ${menor}`)