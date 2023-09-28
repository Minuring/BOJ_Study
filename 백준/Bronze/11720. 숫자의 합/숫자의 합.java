import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        String line[] = br.readLine().split("");
        int sum=0;
        for(int i=0; i<line.length; i++)
            sum += Integer.parseInt(line[i]);
        bw.write(String.valueOf(sum));
        bw.close();
    }
}