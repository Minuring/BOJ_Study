import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        char n =br.readLine().charAt(0);
        bw.write(Integer.toString(Character.hashCode(n)));
        bw.close();
        br.close();
    }
}