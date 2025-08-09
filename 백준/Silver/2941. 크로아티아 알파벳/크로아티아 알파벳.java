import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
    	var br = new BufferedReader(new InputStreamReader(System.in));
    	var croatiaAlphabets = List.of(
    		"dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="
    	);

    	var input = br.readLine();

    	for(var ca : croatiaAlphabets) {
    		input = input.replaceAll(ca, "*");
		}

		System.out.print(input.length());
    }
}