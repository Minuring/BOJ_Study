import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.HashSet;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        HashSet<Integer> cards = new HashSet<>(N);
        for (int i = 0; i < N; i++) {
            cards.add(in.nextInt());
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int M = in.nextInt();
        for (int i = 0; i < M; i++) {
            bw.write((cards.contains(in.nextInt())?1:0)+" ");
        }
        bw.close();
    }
}