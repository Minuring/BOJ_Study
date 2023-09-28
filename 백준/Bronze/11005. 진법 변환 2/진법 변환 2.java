import java.io.*;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        byte B = Byte.parseByte(st.nextToken());

        StringBuffer sb = new StringBuffer("");
        while(N>0){
            if((N%B)>9){
                sb.append(Character.toString(N%B+'A'-10));
            }else sb.append(N%B);
            N /= B;
        }
        bw.write(sb.reverse().toString());
        bw.close();
    }
}
