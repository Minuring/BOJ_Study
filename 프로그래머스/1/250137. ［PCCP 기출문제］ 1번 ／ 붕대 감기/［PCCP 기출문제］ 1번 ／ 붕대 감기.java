import java.util.Arrays;
class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        Player player = new Player(health, bandage[0], bandage[1], bandage[2]);
        int lastAttack = attacks[attacks.length-1][0];
        int seq = 0;
        for (int i=0; i<=lastAttack; i++) {
            if (i == attacks[seq][0]) {
                player.hit(attacks[seq][1]);
                if (seq == attacks.length-1 || player.hp<0) break;
                seq++;
            } else{
                player.heal();
            }
        }
        int answer = player.hp<=0 ? -1 : player.hp;
        return answer;
    }
    
    static class Player {
        int maxHp;
        int hp;
        int skillTime;
        int healPerSec;
        int healPlus;
        
        int continuous = 0;
        public Player(int maxHp, int skillTime, int healPerSec, int healPlus){
            this.maxHp = maxHp;
            this.hp = maxHp;
            this.skillTime = skillTime;
            this.healPerSec = healPerSec;
            this.healPlus = healPlus;
        }
        
        public void hit(int power){
            hp -= power;
            continuous = 0;
        }
        
        public void heal() {
            continuous += 1;
            hp += healPerSec;
            if (continuous == skillTime){
                continuous = 0;
                hp += healPlus;
            }
            
            if(hp > maxHp) hp = maxHp;
        }
    }
}