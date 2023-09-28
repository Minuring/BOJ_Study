import java.io.*;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);

        byte[][] map = new byte[100][100];
        //Arrays.fill(map,0);
        byte N = in.nextByte();
        for(byte i=0; i<N; i++){
            byte x = (byte) (in.nextByte()+10);
            byte y = (byte) (in.nextByte()+10);
            for(byte xpos = (byte) (x-10); xpos<x; xpos++){
                for(byte ypos = (byte) (y-10); ypos<y; ypos++){
                    map[xpos][ypos] = 1;
                }
            }
        }
        int sum=0;
        for(byte[] l : map){
            for(byte b : l) if(b==1) sum++;
        }
        System.out.print(sum);

    }
}
