import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        byte N = Byte.parseByte(br.readLine());
        for(byte i=0; i<N; i++){
            String line = br.readLine();
            bw.write(Character.toString(line.charAt(0))+
                    Character.toString(line.charAt(line.length()-1))+"\n");
            bw.flush();
        }
        bw.close();
    }
}