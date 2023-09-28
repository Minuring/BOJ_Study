import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        short[] list = new short[N];
        for(int i=0; i<N; i++){
            list[i] = Short.parseShort(br.readLine());
        }
        Arrays.sort(list);
        for(Short s : list){
            bw.write(Short.toString(s)+"\n");
        }
        bw.close();
    }
}
