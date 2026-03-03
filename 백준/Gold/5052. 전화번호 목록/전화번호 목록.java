import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {

    public static void main(String[] args) throws Exception {
        var br = new BufferedReader(new InputStreamReader(System.in));
        var t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            var n = Integer.parseInt(br.readLine());

            var trie = new Trie();
            var consistency = true;
            for (int j = 0; j < n; j++) {
                var number = br.readLine();
                trie.add(number);
                if (consistency && !trie.test(number)) {
                    consistency = false;
                }
            }

            System.out.println(consistency ? "YES" : "NO");
        }
    }

    static class Trie {

        static class Node {

            char c;
            String value;
            Map<Character, Node> childs = new HashMap<>();

            public Node(char c) {
                this.c = c;
            }
        }

        final Node root = new Node('\0');

        public void add(String x) {
            var chars = x.toCharArray();
            var e = root;
            var seq = 0;

            for (; seq < chars.length; seq++) {
                var ch = chars[seq];
                if (!e.childs.containsKey(ch)) {
                    break;
                }

                e = e.childs.get(ch);
            }

            for (; seq < chars.length; seq++) {
                var newEntry = new Node(chars[seq]);
                e.childs.put(chars[seq], newEntry);
                e = newEntry;
            }

            e.value = x;
        }

        public boolean test(String x) {
            var chars = x.toCharArray();
            var e = root;
            for (int i = 0; i < chars.length; i++) {
                var ch = chars[i];
                e = e.childs.get(ch);

                // 마지막이 아닌데 값이 존재하면
                if (i < chars.length - 1 && e.value != null) {
                    return false;
                }
            }

            return e.childs.isEmpty();
        }
    }
}
