import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a1=0, b=0;
        for(int i=0; i<2; i++){
            String a[] = st.nextToken().split("");
            String result = Character.toString(a[2].charAt(0))+
                    Character.toString(a[1].charAt(0))+
                    Character.toString(a[0].charAt(0));
            if(i==0) a1 = Integer.parseInt(result);
            else b = Integer.parseInt(result);
        }
        bw.write(Integer.toString(a1>b?a1:b));
        bw.close();
    }
}