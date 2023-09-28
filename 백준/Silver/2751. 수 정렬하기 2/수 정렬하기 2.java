import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        ArrayList<Integer> list = new ArrayList<>();
        for(int i=0; i<N; i++){
            list.add(Integer.parseInt(br.readLine()));
        }
        Collections.sort(list);
        Iterator it = list.listIterator();
        for(int i=0; i<N; i++){
            bw.write(Integer.toString((Integer)it.next())+"\n");
        }
        bw.close();
    }
}
