import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int max=Integer.MIN_VALUE, min= Integer.MAX_VALUE;
        for(int i=0; i<n; i++){
            int tmp = Integer.parseInt(st.nextToken());
            if(tmp > max) max = tmp;
            if(tmp < min) min = tmp;
        }

        bw.write(Integer.toString(min)+" "+Integer.toString(max)); // 출력
        bw.close();
    }
}