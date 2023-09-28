import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        byte N = Byte.parseByte(br.readLine());
        bw.write(String.format("%.0f",Math.pow(get(N),2)));
        bw.close();
    }
    public static int get(int N){
        int sum=2;
        while(N-->0){
            sum = sum*2-1;
        }
        return sum;
    }
}
//3, 5, 9, 17, 33, 65,
