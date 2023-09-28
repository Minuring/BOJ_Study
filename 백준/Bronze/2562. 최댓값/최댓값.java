import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int max= Integer.MIN_VALUE, idx=0;
        for(int i=0; i<9; i++){
            int n = Integer.parseInt(br.readLine());
            if(n > max) {
                max = n;
                idx = i+1;
            }
        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(String.valueOf(max));
        bw.newLine();
        bw.write(Integer.toString(idx));
        bw.close();
    }
}