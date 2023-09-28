import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int basket[] = new int[N];
        for(int i=0; i<N; i++) basket[i] = i+1;
        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int a=Integer.parseInt(st.nextToken());
            int b=Integer.parseInt(st.nextToken());
            int tmp = basket[a-1];
            basket[a-1] = basket[b-1];
            basket[b-1] = tmp;
        }
        for(int i:basket) bw.write(Integer.toString(i)+" ");
        bw.close();
    }
}