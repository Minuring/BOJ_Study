import java.util.Scanner;

public class Main {
    //단계별_2차원배열_행렬덧셈
    public static void main(String[] args){
        int N=0, M=0;
        Scanner in = new Scanner(System.in);
        N = in.nextInt(); M = in.nextInt();
        int S[][] = new int[N][M];
        for(int k=0; k<2; k++){
            for(int i=0; i<N; i++){
                for(int j=0; j<M; j++){
                    S[i][j] += in.nextInt();
                }
            }
        }
        for(int[] line:S){
            for(int e:line) System.out.print(e+" ");
            System.out.println();
        }
    }
}
