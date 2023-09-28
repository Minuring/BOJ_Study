import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        long num = 666;
        for(int i=1; i<N; i++){
            num = getNext(num);
        }
        bw.write(Long.toString(num));
        bw.close();
    }
    public static long getNext(long now){
        long num = now;
        int count =0;
        long tmp=num;
        while(count!=3){
            tmp ++;
            num = tmp;
            count = 0;
            while(num>0 && count!=3){
                if(num%10 == 6) count++;
                else count=0;
                num /= 10;
            }
        }
        return tmp;
    }
}
