import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());
        while(T-- > 0){
            int q=0, d=0, n=0, p=0;
            int N = Integer.parseInt(br.readLine());
            q = N/25; N%=25;
            d = N/10; N%=10;
            n = N/5; N%=5;
            p = N;
            bw.write(String.format("%d %d %d %d\n",q,d,n,p));
        }
        bw.close();
    }
}
