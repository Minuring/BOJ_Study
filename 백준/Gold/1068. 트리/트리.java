import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {

    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        var n = Integer.parseInt(scanner.nextLine());
        var split = scanner.nextLine().split(" ");
        var toRemove = Integer.parseInt(scanner.nextLine());


        var nodes = new MyNode[n];
        var root = (MyNode) null;
        for (int i = 0; i < n; i++) {
            nodes[i] = new MyNode(i);
        }
        for (int i = 0; i < n; i++) {
            var parent = Integer.parseInt(split[i]);
            if (parent == -1) {
                root = nodes[i];
            } else {
                nodes[i].setParent(nodes[parent]);
                nodes[parent].childs.add(nodes[i]);
            }
        }

        assert root != null;
        if (nodes[toRemove] == root) {
            System.out.println("0");
            return;
        }

        nodes[toRemove].parent.childs.remove(nodes[toRemove]);
        System.out.println(root.countLeaf());
    }

    private static class MyNode {
        int id;
        MyNode parent;
        Set<MyNode> childs = new HashSet<>();

        public MyNode(int id) {
            this.id = id;
        }

        public void setParent(MyNode node) {
            this.parent = node;
        }

        public int countLeaf() {
            if (childs.isEmpty()) {
                return 1;
            }

            int count = 0;
            for (var child : childs) {
                count += child.countLeaf();
            }
            return count;
        }

        @Override
        public String toString() {
            return String.format("MyNode[id=%d]", id);
        }
    }
}
