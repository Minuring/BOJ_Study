import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        short N = Short.parseShort(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int score[] = new int[N];
        byte max = 0;
        for(int i=0; i<N; i++){
            score[i] = Integer.parseInt(st.nextToken());
            if(score[i] > max) max = (byte)score[i];
        }
        float sum=0;
        for(int i=0; i<N; i++){
            sum += (float)score[i]/max*100;
        }
        bw.write(Float.toString(sum/N));
        bw.close();
    }
}