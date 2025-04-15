using System;

namespace um;

public class CanetaTesteVetor
{
    private List<Caneta> canetas = new List<Caneta>();

    public void cadastrarCaneta(Caneta caneta)
    {
        if (canetas.Count() < 50)
        {
            canetas.Add(caneta);
        } 
        else
        {
            Console.WriteLine("Número maximo de canetas atingido!");
        }
    }

    public void exibirCanetas()
    {
        if (canetas.Count == 0)
        {
        Console.WriteLine("Nenhuma caneta cadastrada.");
        return;
        }
    
       
        Console.WriteLine("Canetas cadastradas:");
        foreach (Caneta caneta in canetas)
        {
            Console.WriteLine(caneta.ToString()); 
        }

    }

    public void exibirQuantidade()
    {
        if (canetas.Count() == 0)
        {
            Console.WriteLine("0 canetas cadastradas");
        }
        else
        {
            Console.WriteLine($"{canetas.Count()} caneta(s) cadastradas no total!");
        }
        
    }

    public void exibirPorCor(Cores cor)
    {
        bool encontrou = false;
        foreach(var caneta in canetas)
        {
            if (caneta != null && caneta.Cor == cor)
            {
                Console.WriteLine(caneta.ToString());
                encontrou = true;
            }
        }

        if (!encontrou)
        {
            Console.WriteLine($"Nenhuma caneta da cor {cor} foi encontrada.");
        }

    }

}
