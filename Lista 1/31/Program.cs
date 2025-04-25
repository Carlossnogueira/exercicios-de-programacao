/*
Escrever um programa que leia um conjunto de números positivos, e exiba se o número lido é par ou ímpar. Exiba 
ao final a soma total dos números pares lidos e também a soma dos números ímpares lidos. Suporemos que o 
número de elementos deste conjunto não é conhecido, e que um número negativo será utilizado para sinalizar o 
fim dos dados. 
*/

List<int> numerosPositivos = new List<int>();
List<int> numerosPares = new List<int>();
List<int> numerosImpares = new List<int>();

int quantolist = numerosImpares.Count(); 

int somaDosPares = 0;
int somaDosImpares = 0;

while (true)
{
    Console.WriteLine("Digite um número positivo (ou um número negativo para encerrar): ");
    int entrada = int.Parse(Console.ReadLine());

    if(entrada < 0)
    {
        break;
    }

    numerosPositivos.Add(entrada);

    if (entrada % 2 != 0)
    {
        Console.WriteLine($"Numero {entrada} é impar");
        numerosImpares.Add(entrada);
        somaDosImpares += entrada;
    }
    else 
    {
        Console.WriteLine($"Numero {entrada} é par");
        numerosPares.Add(entrada);
        somaDosPares += entrada;
    }
}

Console.WriteLine($"A soma dos pares é {somaDosPares} e dos ímpares é: {somaDosImpares}");