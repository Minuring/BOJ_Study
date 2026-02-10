import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.LinkedList;

public class Main {

    public static void main(String[] args) throws Exception {
        var br = new BufferedReader(new InputStreamReader(System.in));
        var nTestCase = Integer.parseInt(br.readLine());

        for (int i = 0; i < nTestCase; i++) {
            var operations = br.readLine().toCharArray();

            var n = Integer.parseInt(br.readLine());
            var input = br.readLine();
            var strings = new LinkedList<String>();
            if (n > 0) {
                var braceRemoved = input.substring(1, input.length() - 1);
                Collections.addAll(strings, braceRemoved.split(","));
            }

            boolean front = true, error = false;
            for (char operation : operations) {
                if (operation == 'R') {
                    front = !front;
                } else {
                    if (strings.isEmpty()) {
                        error = true;
                        break;
                    }
                    strings.remove(front ? 0 : strings.size() - 1);
                }
            }

            if (error) {
                System.out.println("error");
            } else {
                System.out.println(toString(front, strings));
            }
        }
    }

    private static String toString(boolean front, final LinkedList<String> strings) {
        var iterator = front ? strings.iterator() : strings.descendingIterator();
        if (!iterator.hasNext()) {
            return "[]";
        }

        var sb = new StringBuilder("[");
        while (true) {
            var next = iterator.next();
            sb.append(next);
            if (!iterator.hasNext()) {
                return sb.append("]").toString();
            }
            sb.append(",");
        }
    }
}
