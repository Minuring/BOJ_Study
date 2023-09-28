import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a,b,c,d,e,f;
        a= Integer.parseInt(st.nextToken()); b= Integer.parseInt(st.nextToken());
        c= Integer.parseInt(st.nextToken()); d= Integer.parseInt(st.nextToken());
        e= Integer.parseInt(st.nextToken()); f= Integer.parseInt(st.nextToken());

        for(int x=-999; x<=999; x++){
            for(int y=-999; y<=999; y++){
                if((a*x+b*y)==c && (d*x+e*y)==f){
                    bw.write(String.format("%d %d",x,y));
                    break;
                }
            }
        }
        bw.close();
    }
}
