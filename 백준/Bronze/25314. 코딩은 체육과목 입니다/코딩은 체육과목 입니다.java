import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String tmp=br.readLine();
        int n = Integer.parseInt(tmp)/4;
        for(int i=0; i<n; i++) System.out.print("long ");
        System.out.print("int");
    }
}