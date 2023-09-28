import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        bw.write(Integer.toString(getMul(N)));
        bw.close();
    }
    public static int getMul(int N){
        int count=1;
        for(int i=2, k=6; i<=N; i+=k, k+=6){
            count++;
        }
        return count;
    }
}

//2~7, 6개,
//8~19 12개,
//20~37 18개,
//38~61 24개,
//62~  30개?
