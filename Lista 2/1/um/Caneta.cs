using System;

namespace um;

public class Caneta
{
    public Caneta(string marca,Cores cor,string tamanho)
    {
        this.Marca = marca;
        this.Cor = cor;
        this.Tamanho = tamanho;
    }

    public string Marca {get;set;} = string.Empty;
    public Cores Cor {get;set;}
    public string Tamanho {get;set;}

    public override string ToString()
    {
        return $"Marca: {Marca}, Cor: {Cor}, Tamanho: {Tamanho}";
    }

}
