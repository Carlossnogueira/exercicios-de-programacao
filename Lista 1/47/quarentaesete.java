/*
    Considere um vetor de 10 números inteiros positivos maiores que zero e um único número inteiro, também positivo
    e maior que zero. Faça um programa para:
    a. ler pelo teclado o vetor;
    b. ler pelo teclado o número X;
    c. dizer quantos números no vetor são maiores que X, menores que X e iguais a X
*/

import java.util.Scanner;

public class quarentaesete{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] vetor = new int[10];
        int x = 0;
        int maiores = 0;
        int menores = 0;
        int iguais = 0;

        System.out.println("Digite o numero inteiro maior do que 0 para X:");
        try{
            int entrada = sc.nextInt();
            if(entrada > 0){
                x = entrada;
            }
        } catch(Exception e){
            System.out.println("Entrada inválida!");
        }

        for(int i =0; i < vetor.length; i++){
            System.out.println("Digite o número para o vetor na posição: " + i);
            
            while (!sc.hasNextInt()) {
                System.out.println("Entrada inválida! Digite um número inteiro:");
                sc.next();
            }

            int entradaNumero = sc.nextInt();
            vetor[i] = entradaNumero;
            
            if(vetor[i] > x){
                maiores++;
            } else if(vetor [i] < x){
                menores++;
            } else {
                iguais++;
            }
        }

        sc.close();
        System.out.println("Maiores: " + maiores + " Menores: " + menores + " Iguais " + iguais);

    }
}