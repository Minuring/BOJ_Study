import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        // 코드 작성
        var br = new BufferedReader(new InputStreamReader(System.in));
        var n = Integer.parseInt(br.readLine());

        var stack = new Stack();
        for(int i=0; i<n; i++) {
            String cmd = br.readLine();
            if (cmd.startsWith("push")) {
                int x = Integer.parseInt(cmd.split(" ")[1]);
                stack.push(x);

            } else if(cmd.startsWith("pop")) {
                System.out.println(stack.pop());
            } else if(cmd.startsWith("size")) {
                System.out.println(stack.size());
            } else if(cmd.startsWith("empty")) {
                System.out.println(stack.isEmpty() ? 1 : 0);
            } else {
                System.out.println(stack.top());
            }
        }
    }
}

class Stack {
    int[] arr = new int[10000];
    int top = -1; // top위치

    public void push(int x) {
        arr[++top] = x;
    }

    public int pop() {
        if (isEmpty()) return -1;

        int x = arr[top];
        top--;
        return x;
    }

    public int size() {
        return top + 1;
    }

    public boolean isEmpty() {
        return top < 0;
    }

    public int top() {
        if (isEmpty()) return -1;
        return arr[top];
    }
}