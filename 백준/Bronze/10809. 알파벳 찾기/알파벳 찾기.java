import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();
        int idx=-1;
        for(char i='a'; i<='z'; i++){
            for(int j=0; j<str.length(); j++){
                if(i==str.charAt(j)) {
                    idx=j; break;
                }
            }
            bw.write((idx==-1?Integer.toString(-1):Integer.toString(idx))+" ");
            idx=-1;
        }
        bw.close();
    }
}