import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        var br = new BufferedReader(new InputStreamReader(System.in));
        var n = Integer.parseInt(br.readLine());
        var underq = new PriorityQueue<Integer>(Comparator.reverseOrder());
        var overq = new PriorityQueue<Integer>();
        for (int i = 0; i < n; i++) {
            var num = Integer.parseInt(br.readLine());
            var q = i % 2 == 0 ? underq : overq;
            q.offer(num);

            if (i > 0 && underq.peek() > overq.peek()) {
                var over = overq.poll();
                var under = underq.poll();
                overq.offer(under);
                underq.offer(over);
            }
            System.out.println(underq.peek());
        }
    }
}
