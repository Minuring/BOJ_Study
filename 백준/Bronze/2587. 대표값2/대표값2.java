import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] arr = new int[5];
        for(int i=0; i<5; i++) arr[i] = Integer.parseInt(br.readLine());
        Arrays.sort(arr);
        int sum=0, mid=0;
        for(int i=0; i<5; i++){
            sum += arr[i];
        }
        bw.write(String.format("%d\n%d",sum/5,arr[2]));
        bw.close();
    }

}
