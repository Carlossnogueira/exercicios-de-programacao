/*
Faça um programa que exiba as opções: 
1 – Conversão de Graus Celsius em Graus Fahrenheit 
2 – Conversão de Graus Fahrenheit em Graus Celsius 
3 – Peso ideal do homem 
4 – Peso ideal da mulher 
O programa só deve encerrar quando o usuário digitar  ́S ́ para a pergunta “Deseja encerrar o programa?” 
Obs.: Nas opções 3 e 4 informar se o usuário está acima ou abaixo do peso ideal. 
*/

int opcao = 0;
float c, f, peso, altura, imc = 0.0f;

while (true)
{
    Console.WriteLine("Escolha uma opção:\n1 – Conversão de Graus Celsius em Graus Fahrenheit\n2 – Conversão de Graus Fahrenheit em Graus Celsius\n3 – Peso ideal do homem\n4 – Peso ideal da mulher");

    try
    {
        opcao = int.Parse(Console.ReadLine());
    }
    catch (Exception)
    {
        Console.WriteLine("valor inválido!");
        continue;
    }

    switch (opcao)
    {
        case 1:
            Console.WriteLine("Digite os Graus Celsius para conversão");
            c = float.Parse(Console.ReadLine());
            f = (c * 9 / 5) + 32;
            Console.WriteLine($"Fahrenheit: {f}");
            break;
        case 2:
            Console.WriteLine("Digite os Fahrenheits para conversão");
            f = float.Parse(Console.ReadLine());
            c = 5.0f / 9.0f * (f - 32);
            Console.WriteLine($"Graus Celsius: {c}");
            break;
        case 3:
        case 4:
            Console.WriteLine("Digite o peso:");
            peso = float.Parse(Console.ReadLine());
            Console.WriteLine($"PESO: {peso}");
            Console.WriteLine("Digite a altura:");
            altura = float.Parse(Console.ReadLine());
            Console.WriteLine($"ALTURA {altura}");
            imc = peso / (altura * altura);
            if (imc >= 18.5 && imc <= 24.9)
            {
                Console.WriteLine($"IMC {Math.Round(imc, 2)}");
                Console.WriteLine("Está no peso ideal!");
            }
            else if (imc < 18.5)
            {
                Console.WriteLine($"IMC {Math.Round(imc, 2)}");
                Console.WriteLine("Está abaixo do peso!");
            }
            else
            {
                Console.WriteLine($"IMC {Math.Round(imc, 2)}");
                Console.WriteLine("Está acima do peso!");
            }
            break;
    }

    Console.WriteLine("Deseja encerrar o programa? (S/s)");
    string opcaoEncerrar = Console.ReadLine().ToLower();
    if (opcaoEncerrar == "s")
    {
        Environment.Exit(0);
    }
    else
    {
        continue;
    }
}