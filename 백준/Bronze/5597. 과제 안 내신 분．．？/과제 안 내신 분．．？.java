import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        boolean[] tf = new boolean[30];
        for(int i=0; i<28; i++){
            tf[Integer.parseInt(br.readLine())-1] = true;
        }
        for(int i=0; i<30; i++){
            if(tf[i]==false)bw.write(Integer.toString(i+1)+"\n");
        }
        bw.close();
    }
}