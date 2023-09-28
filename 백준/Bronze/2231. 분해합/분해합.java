import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        for(int i=1; i<=N; i++){
            if(i==N) System.out.print("0");
            int sum=i, tmp=i;
            while(tmp>0){
                sum += tmp%10;
                tmp = tmp/10;
            }
            if(sum == N){
                System.out.print(i); break;
            }
        }
    }
}
