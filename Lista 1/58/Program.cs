namespace cinquentaenove;

/*
Fazer um programa para armazenar em um vetor, vários números inteiros e positivos e calcular a média. Imprimir 
também o maior. A quantidade de números lidos será definida pelo usuário. 
*/

class Program
{
    static void Main(string[] args)
    {

        int quantidadeNumeros = 0;
        int maiorNumero = 0;
        int somaDosNumeros = 0;

        while (true)
        {
            Console.WriteLine("Digite a quantidade de números");
            string input = Console.ReadLine() ?? "0";

            if (int.TryParse(input, out quantidadeNumeros) && quantidadeNumeros > 0)
            {
                break;
            }
            else
            {
                Console.WriteLine("Quantidade inválida. Digite um número positivo.");
            }
        }

        int[] arrayNumeros = new int[quantidadeNumeros];

        for (int i = 0; i < arrayNumeros.Length; i++)
        {
            Console.WriteLine($"Digite o {i + 1}º número possitivo e inteiro.");
            string temp = Console.ReadLine() ?? "0";
            if (int.TryParse(temp, out int numero) && numero > 0)
            {
                arrayNumeros[i] = numero;
            }
            else
            {
                Console.WriteLine("Número inválido, digite um número possitivo e inteiro.");
                continue;
            }

        }

        for (int i = 0; i < arrayNumeros.Length; i++)
        {
            if (arrayNumeros[i] > maiorNumero)
            {
                maiorNumero = arrayNumeros[i];
            }

            somaDosNumeros += arrayNumeros[i];
        }

        Console.WriteLine("A média dos números digitados é de: " + (somaDosNumeros / quantidadeNumeros));
        Console.WriteLine("O maior número do array é: " + maiorNumero);

    }
}
