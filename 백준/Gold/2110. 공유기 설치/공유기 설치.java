

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int c = sc.nextInt();

        int[] houses = new int[n];
        for (int i = 0; i < n; i++) {
            houses[i] = sc.nextInt();
        }

        Arrays.sort(houses);

        int left = 1;  // 최소 거리
        int right = houses[n - 1] - houses[0];  // 가능한 최대 거리
        int answer = 0;

        while (left <= right) {
            int mid = (left + right) / 2; // 현재 시도할 거리
            if (canInstall(houses, c, mid)) {
                answer = mid;      // 가능하다면 일단 저장
                left = mid + 1;    // 더 큰 거리 시도
            } else {
                right = mid - 1;   // 설치 불가능 → 더 줄여
            }
        }

        System.out.println(answer);
    }

    // 거리 distance로 공유기 c개 이상 설치할 수 있는가?
    private static boolean canInstall(int[] houses, int c, int distance) {
        int count = 1;  // 첫 집에 공유기 설치하고
        int lastInstalled = houses[0];

        for (int i = 1; i < houses.length; i++) {
            if (houses[i] - lastInstalled >= distance) {
                count++;
                lastInstalled = houses[i];
            }
        }

        return count >= c;
    }
}
