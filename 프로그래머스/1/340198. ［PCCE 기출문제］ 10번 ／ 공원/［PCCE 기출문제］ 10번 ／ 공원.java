import java.util.Arrays;
class Solution {
        public int solution(int[] mats, String[][] park) {
            int answer = -1;
            Arrays.sort(mats);

            for (int i = 0; i < park.length; i++) {
                for (int j = 0; j < park[i].length; j++) {
                    int placed = getSizeAt(park, mats, i, j);
                    answer = Math.max(answer, placed);
                }
            }
            return answer;
        }

        private int getSizeAt(String[][] park, int[] mats, int i, int j) {
            if (!park[i][j].equals("-1")) return -1;
            
            int maxSize = -1;
            int limitY = park.length;
            int limitX = park[i].length;

            for (int matSize : mats) {
                if (limitY < i + matSize || limitX < j + matSize) continue;
                
                int canPlace = 0;
                for (int y = i; y < i + matSize; y++) {
                    for (int x = j; x < j + matSize; x++) {
                        if (!park[y][x].equals("-1")) break;
                        canPlace++;
                    }
                }

                if(canPlace == matSize*matSize) maxSize = Math.max(matSize, maxSize);

            }

            return maxSize;
        }
    }