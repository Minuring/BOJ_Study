import java.io.*;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st =new StringTokenizer(br.readLine());
        byte count[] = {1,1,2,2,2,8};
        for(byte i=0; i<6; i++){
            byte n = Byte.parseByte(st.nextToken());
            bw.write(Byte.toString((byte) (count[i]-n))+" ");
        }
        bw.close();
    }
}
