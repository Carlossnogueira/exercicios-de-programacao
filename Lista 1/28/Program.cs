// Faça um programa que gera e escreve os números ímpares dos números lidos entre 100 e 200

Console.WriteLine("Digite um número entre 100 e 200:");
int numero = int.Parse(Console.ReadLine());

if(numero > 200 || numero == 0 || numero < 100){
    Console.WriteLine("Número inválido.");
    Environment.Exit(0);
}

// 100 
for(int i = numero; i < 201; i++)
{
    if(i % 2 > 0.1){
        Console.WriteLine(i);
    }
}

if(numero == 200){
    Console.WriteLine("Sem números pares");
}