import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N=Integer.parseInt(st.nextToken());
        int M=Integer.parseInt(st.nextToken());
        int[] basket = new int[N];
        Arrays.fill(basket,0);
        for(int x=0; x<M; x++){
            st = new StringTokenizer(br.readLine());
            int i=Integer.parseInt(st.nextToken());
            int j=Integer.parseInt(st.nextToken());
            int k=Integer.parseInt(st.nextToken());
            for(int y=i-1; y<j; y++){
                basket[y] = k;
            }
        }
        StringBuilder sb= new StringBuilder();
        for(int i:basket) sb.append(i+" ");
        bw.write(sb.toString());
        bw.close();
    }
}