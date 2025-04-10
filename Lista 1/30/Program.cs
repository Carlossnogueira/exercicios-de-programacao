// Faça um programa para imprimir uma tabuada

Console.WriteLine("Digite qual tabuada será feita:");
int tabuada = int.Parse(Console.ReadLine());

for(int i = 1; i < 11; i++){
    Console.WriteLine($"{tabuada} x {i} = {tabuada*i}");
}