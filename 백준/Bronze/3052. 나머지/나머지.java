import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n[] = new int[10];
        for(int i=0; i<10; i++){
            n[i]=Integer.parseInt(br.readLine())%42;
        }
        int count =0;
        boolean flag = false;
        for(int i=0; i<10; i++){
            flag = false;
            for(int j=i+1; j<10; j++){
                if(n[i]==n[j]){
                    flag=true; break;
                }
            }
            if(flag==false)count++;
        }
        bw.write(Integer.toString(count));
        bw.close();
    }
}