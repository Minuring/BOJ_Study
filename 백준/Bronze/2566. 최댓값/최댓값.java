import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        byte[][] table = new byte[9][9];
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int max=0, row=0, col=0;
        for(int i=0; i<9; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j=0; j<9; j++){
                int num = Integer.parseInt(st.nextToken());
                if(num > max){
                    max = num;
                    row = i; col = j;
                }
            }
        }
        bw.write(String.format("%d\n%d %d",max,row+1,col+1));
        bw.close();
    }
}
