/*
    Dados dois vetores x e y, ambos com n elementos, determinar o produto escalar desses vetores. Ou seja, realizar 
    a soma de todos dos resultados da multiplicação de x[i] por y[i].
*/

class quarentaeseis{
    public static void main(String []args){
        int[] x = {5,4,8,9,6,4,3};
        int[] y = {8,9,6,3,4,2,8};

        int produtoEscalar = 0;

        for(int i = 0; i < x.length; i++){
            produtoEscalar += x[i] * y[i];
        }

        System.out.println("Produto escalar = " + produtoEscalar);
    }
}