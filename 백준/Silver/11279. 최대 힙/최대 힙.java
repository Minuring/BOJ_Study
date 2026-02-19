import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {

    public static void main(String[] args) throws Exception {
        var reader = new BufferedReader(new InputStreamReader(System.in));
        var n = Integer.parseInt(reader.readLine());
        var inputs = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            var num = Integer.parseInt(reader.readLine());
            inputs.add(num);
        }


        var pq = new PriorityQueue<Integer>(Comparator.reverseOrder());
        for (var num : inputs) {
            if (num == 0) {
                var polled = pq.poll();
                System.out.println(polled == null ? 0 : polled);
            } else {
                pq.add(num);
            }
        }
    }
}
