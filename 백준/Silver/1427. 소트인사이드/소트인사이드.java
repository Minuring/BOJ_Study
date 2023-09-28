import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        char[] s = br.readLine().toCharArray();
        Arrays.sort(s);
        for(int i=s.length-1; i>=0; i--){
            bw.write(s[i]);
        }
        bw.close();
    }
}
