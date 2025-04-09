/*
 Escreva um programa que leia: 
- a quantidade de números que deverá processar; 
- os números que deverá processar,e calcule e exiba, para cada número a ser processado o seu fatorial. 
Lembrete: O fatorial de um número N é dado pela fórmula: N! = 1 * 2 * 3 * 4 * 5 * ... * N
*/

int numero = 0;
int resultado = 1;

Console.WriteLine("Digite a quantidade e números a ser processada: ");
        
        try
        {
            numero = int.Parse(Console.ReadLine());
        } 
        catch 
        {
            Console.WriteLine("Entrada inválida");
            Environment.Exit(0);
        }

for(int i = 1; i <= numero; i++)
{
  resultado *= i; // 1 2 6 24 120
  Console.WriteLine(resultado);
}

Console.WriteLine($"O fatorial de {numero} é = {resultado}");

