import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int seq = 0;
        int accum = 0;
        while (accum < n) {
            accum += ++seq;
        }

        if (seq % 2 == 0) {
            // 좌하
            int diff = accum - n;
            int bunja = seq - diff;
            int bunmo = diff + 1;
            System.out.println(bunja + "/" + bunmo);
        } else {
            int diff = accum - n;
            int bunja = diff + 1;
            int bunmo = seq - diff;
            System.out.println(bunja + "/" + bunmo);
        }
    }
}
