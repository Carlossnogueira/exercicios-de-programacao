// Em java também para nunca esquecer! XD

import java.util.Scanner;

public class dezoito {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numero = 0;

        System.out.println("Digite um número:");
        try{
            numero = sc.nextInt(); 
        } catch(Exception e){
            System.out.println("Algo deu errado");
        }

        switch (numero) {
            case 1:
                System.out.println("um");
                break;
            case 2:
                System.out.println("dois");
                break;
            case 3:
                System.out.println("três");
            default:
                System.out.println("Número inválido");
                break;
        }

        sc.close();

    }
}
