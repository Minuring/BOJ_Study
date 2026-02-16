import java.util.Scanner;

public class Main {

    static class MyStack {
        private final char[] arr;
        private int top = -1;

        public MyStack(int size) {
            this.arr = new char[size];
        }

        public void push(char c) {
            arr[++top] = c;
        }

        public int size() {
            return top + 1;
        }

        public boolean containsLast(String str) {
            if (size() < str.length()) {
                return false;
            }
            for (int i = 0; i < str.length(); i++) {
                var i_stack = this.size() - str.length() + i;
                if (arr[i_stack] != str.charAt(i)) {
                    return false;
                }
            }
            return true;
        }

        public void removeLastN(int n) {
            top -= n;
        }

        public String asString() {
            var sb = new StringBuilder();
            for (int i = 0; i <= top; i++) {
                sb.append(arr[i]);
            }
            return sb.toString();
        }
    }

    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        var str = scanner.nextLine();
        var bomb = scanner.nextLine();

        var chars = str.toCharArray();
        var stack = new MyStack(str.length());
        for (var ch : chars) {
            stack.push(ch);
            while (stack.containsLast(bomb)) {
                stack.removeLastN(bomb.length());
            }
        }

        var result = stack.asString();
        System.out.println(result.isEmpty() ? "FRULA" : result);
    }
}
