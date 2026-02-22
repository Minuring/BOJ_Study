import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.TreeMap;

public class Main {

    public static void main(String[] args) throws Exception {
        var br = new BufferedReader(new InputStreamReader(System.in));
        var nk = br.readLine().split(" ");
        var n = Integer.parseInt(nk[0]);
        var k = Integer.parseInt(nk[1]);

        var jewels = new PriorityQueue<Jewel>();
        for (int i = 0; i < n; i++) {
            var mv = br.readLine().split(" ");
            var m = Integer.parseInt(mv[0]);
            var v = Integer.parseInt(mv[1]);
            var jewel = new Jewel(m, v);
            jewels.offer(jewel);
        }

        var bags = new TreeMap<Integer, Integer>(); // 무게, 개수
        for (int i = 0; i < k; i++) {
            var c = Integer.parseInt(br.readLine());
            bags.put(c, bags.getOrDefault(c, 0) + 1);
        }

        long sum = 0;
        while (!jewels.isEmpty() && !bags.isEmpty()) {
            var jewel = jewels.poll();

            var bagWeight = bags.ceilingKey(jewel.weight);
            if (bagWeight == null) continue;
            var bagCount = bags.get(bagWeight);
            bags.replace(bagWeight, bagCount - 1);
            if (bagCount - 1 == 0) bags.remove(bagWeight);

            sum += jewel.value;
        }

        System.out.println(sum);
    }

    static class Jewel implements Comparable<Jewel> {
        int weight;
        int value;

        public Jewel(int m, int v) {
            weight = m;
            value = v;
        }

        @Override
        public int compareTo(Jewel other) {
            var comp = other.value - this.value;
            if (comp == 0) {
                comp = this.weight - other.weight;
            }
            return comp;
        }
    }
}
