namespace cinquentaeseis;
/*
Fazer  um  programa  para  ler  um  vetor  de  inteiros  positivos  de  50  posições.  Imprimir  a  quantidade  de  números 
pares e de múltiplos de 5.
*/
class Program
{
    static void Main(string[] args)
    {

        int[] numbers = new int[50];
        List<int> numbersList = new List<int>();
        int result = 0;

        // Utilizarei o Random para popular o array
        Random random = new Random();

        for (int i = 0; i < numbers.Length; i++)
        {
            numbers[i] = random.Next(1, 100);
            numbersList.Add(numbers[i]);

            if (numbers[i] % 2 == 0 && numbers[i] % 5 == 0)
            {
                result++;
            }
        }

        Console.WriteLine($"Quantidade de números pares e multiplos de 5: {result}");

        string numbersInString = "";
        foreach (var item in numbersList)
        {
            numbersInString += item + " ";
        }
        Console.WriteLine($"Lista de números do array: {numbersInString}");


    }
}
