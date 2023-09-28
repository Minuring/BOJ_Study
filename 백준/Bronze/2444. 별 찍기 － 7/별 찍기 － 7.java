import java.io.*;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        byte n = Byte.parseByte(br.readLine());
        for(short i=0; i<n; i++){
            for(short j=0; j<n-1-i; j++) bw.write(" ");
            for(short j=0; j<i+1; j++) bw.write("*");
            for(short j=0; j<i; j++) bw.write("*");
            bw.newLine();
            bw.flush();
        }
        for(short i=0; i<n-1; i++){
            for(short j=0; j<i+1; j++) bw.write(" ");
            for(short j=0; j<n-i-1; j++) bw.write("*");
            for(short j=0; j<n-i-2; j++) bw.write("*");
            bw.newLine();
            bw.flush();
        }
        bw.close();
    }
}
