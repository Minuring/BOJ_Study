import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class Main {

    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        var nTestCase = Integer.parseInt(scanner.nextLine());

        for (int i = 0; i < nTestCase; i++) {
            Network.NETWORKS.clear();
            var f = Integer.parseInt(scanner.nextLine());
            for (int j = 0; j < f; j++) {
                var split = scanner.nextLine().split(" ");
                var p1 = split[0];
                var p2 = split[1];

                var p1net = Network.byMember(p1);
                var p2net = Network.byMember(p2);
                if (p1net.master.equals(p2net.master)) {
                    System.out.println(p1net.set.size());

                } else {
                    var unioned = p1net.union(p2net);
                    System.out.println(unioned.set.size());
                }
            }
        }
    }

    private static class Network {

        private static final Map<String, Network> NETWORKS = new HashMap<>();

        static Network byMember(String name) {
            NETWORKS.putIfAbsent(name, new Network(name));
            return NETWORKS.get(name);
        }

        private final String master;
        private final Set<String> set = new HashSet<>();

        private Network(String master) {
            this.master = master;
            this.set.add(master);
        }

        public Network union(Network other) {
            if (this.master.equals(other.master)) {
                return this;
            }

            this.set.addAll(other.set);
            for (var name : other.set) {
                NETWORKS.replace(name, this);
            }
            return this;
        }
    }
}
