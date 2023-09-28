import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        char[] arr = br.readLine().toCharArray();
        int time=0;
        for(int i=0; i<arr.length; i++){
            if(arr[i] < 'D') time+=3;
            else if(arr[i]<'G') time+=4;
            else if(arr[i]<'J') time+=5;
            else if(arr[i]<'M') time+=6;
            else if(arr[i]<'P') time+=7;
            else if(arr[i]<'T') time+=8;
            else if(arr[i]<'W') time+=9;
            else time+=10;
        }
        bw.write(Integer.toString(time));
        bw.close();
    }
}