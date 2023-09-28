import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String line="";
        while((line=br.readLine())!=null&&!line.isEmpty()){
            bw.write(line);
            bw.newLine();
        }
        bw.close();
    }
}