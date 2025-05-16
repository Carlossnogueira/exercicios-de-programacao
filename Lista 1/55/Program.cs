namespace cinquentaecinco;

/*
    Fazer  um  programa  que  leia  uma  frase  de  até  50  caracteres  e  imprima  a  frase  sem  os  espaços  em  branco. 
    Imprimir também a quantidade de espaços em branco da frase.
*/
class Program
{
    static void Main(string[] args)
    {
        string frase = "";
        string fraseSemEspaco = "";
        int espaços = 0;

        while (true)
        {
            Console.WriteLine("Digite uma frase com até 50 caracteres: ");
            frase = Console.ReadLine() ?? "null";

            if (frase == "null")
            {
                Console.WriteLine("Entre com um valor válido!");
                continue;
            }

            if (frase.Length > 50)
            {
                Console.WriteLine("Frase muito grande! Digite novamente:");
                continue;
            }

            break;
        }

        for (int i = 0; i < frase.Length; i++)
        {
            if (frase[i] == ' ')
            {
                espaços++;
            }

            if (frase[i] != ' ') // queria que frase[i] fosse diferente de ' ' 
            {
                fraseSemEspaco += frase[i];
            }
        }

        Console.WriteLine($"Frase sem espaços: {fraseSemEspaco}");
        Console.WriteLine($"Quantidade de espaços: {espaços}");

    }
}
