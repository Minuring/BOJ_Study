import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] basket= new int[N];
        for(int i=0; i<N; i++)basket[i]=i+1;

        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            rev(basket,a,b);
        }
        for(int i=0; i<N; i++) bw.write(Integer.toString(basket[i])+" ");
        bw.close();
    }
    public static void rev(int[] arr,int a,int b){
        int tmp[] = new int[b-a+1];
        for(int i=0; i<b-a+1; i++){
            tmp[i] = arr[b-i-1];
        }
        for(int i=0; i<b-a+1; i++) arr[a-1+i] = tmp[i];
    }
}