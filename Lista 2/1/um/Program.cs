/*
Implementar  uma  classe  Caneta  que  deve  possuir  como  características  marca,  cor  e  tamanho.  Nesta  classe 
devem ser implementados os  métodos construtores, getters, setters e toString. Em uma  outra classe 
chamada  CanetaTesteVetor  deverá  ser  criado  um  vetor  para  armazenar  no  máximo  50  objetos  do  tipo 
Caneta. O programa deverá exibir o seguinte menu para o usuário:  

1 – Cadastrar caneta 
2 – Exibir todas as canetas 
3 – Exibir quantidade de canetas cadastradas 
4 – Consultar quantidade de canetas de uma determinada cor (digitada pelo usuário) 
0 - Sair
*/

using um;

CanetaTesteVetor canetas = new CanetaTesteVetor();
int entrada = 6;
Cores corDois;
Cores cor;

while (true)
{
    Console.WriteLine("---MENU DE OPÇÕES---");
    Console.WriteLine("1 – Cadastrar caneta \n2 – Exibir todas as canetas\n3 – Exibir quantidade de canetas cadastradas\n4 – Consultar quantidade de canetas de uma determinada cor\n0 - Sair");

    try
    {
        entrada = int.Parse(Console.ReadLine());
    }
    catch
    {
        Console.WriteLine("Entrada inválida!");
        continue;
    }

    switch (entrada)
    {
        case 1:
            Console.WriteLine("Digite a marca:");
            string marca = Console.ReadLine();

            while (true)
            {

                Console.WriteLine("Digite a cor (AZUL,VERMELHO,PRETO):");
                string corEntrada = Console.ReadLine().ToUpper();
                if (corEntrada == "AZUL")
                {
                    cor = Cores.AZUL;
                    break;
                }
                else if (corEntrada == "VERMELHO" || corEntrada == "VERMELHA")
                {
                    cor = Cores.VERMELHA;
                    break;
                }
                else if (corEntrada == "PRETO" || corEntrada == "PRETA")
                {
                    cor = Cores.PRETA;
                    break;
                }
                else
                {
                    Console.WriteLine("Cor inválida!");
                }
            }

            Console.WriteLine("Digite o tamanho:");
            string tamanho = Console.ReadLine();

            Caneta caneta = new Caneta(marca, cor, tamanho);
            canetas.cadastrarCaneta(caneta);
            break;

        case 2:
            canetas.exibirCanetas();
            break;
        case 3:
            canetas.exibirQuantidade();
            break;
        case 4:
            while (true)
            {
                Console.WriteLine("Digite a cor (AZUL,VERMELHO,PRETO):");
                string corEntradaDois = Console.ReadLine().ToUpper();
                if (corEntradaDois == "AZUL")
                {
                    corDois = Cores.AZUL;
                    break;
                }
                else if (corEntradaDois == "VERMELHO" || corEntradaDois == "VERMELHA")
                {
                    corDois = Cores.VERMELHA;
                    break;
                }
                else if (corEntradaDois == "PRETO" || corEntradaDois == "PRETA")
                {
                    corDois = Cores.PRETA;
                    break;
                }
                else
                {
                    Console.WriteLine("Cor inválida!");
                }
            }
            canetas.exibirPorCor(corDois);
            break;
        case 0:
            Console.WriteLine("Finalizando");
            Environment.Exit(0);
            break;
    }

}