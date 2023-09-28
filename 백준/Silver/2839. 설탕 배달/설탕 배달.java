import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        short N = Short.parseShort(br.readLine());
        short count = 0;
        while((short)(N%5)>0){
            count++;
            N -= 3;
        }
        count += (short)N/5;
        N %= 5;
        if(N!=0) bw.write(String.valueOf(-1));
        else bw.write(String.valueOf(count));
        bw.close();
    }
}
