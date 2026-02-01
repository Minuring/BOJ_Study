import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        var split = scanner.nextLine().split(" ");
        var n = Integer.parseInt(split[0]);
        var k = Integer.parseInt(split[1]);

        var countries = new ArrayList<Country>();
        for (int i = 0; i < n; i++) {
            var spl = scanner.nextLine().split(" ");
            var countryId = Integer.parseInt(spl[0]);
            var gold = Integer.parseInt(spl[1]);
            var silver = Integer.parseInt(spl[2]);
            var bronze = Integer.parseInt(spl[3]);
            var country = new Country(countryId, gold, silver, bronze);
            countries.add(country);
        }

        var toFind = countries.stream()
                .filter(c -> c.id == k)
                .findAny().orElseThrow();

        Collections.sort(countries);
        var rank = countries.indexOf(toFind);
        System.out.println(rank);
    }

    static class Country implements Comparable<Country> {
        int id;
        int gold, silver, bronze;

        public Country(int id, int g, int s, int b) {
            this.id = id;
            gold = g;
            silver = s;
            bronze = b;
        }

        public int compareTo(Country c) {
            var compare = Integer.compare(this.gold, c.gold);
            if (compare != 0) {
                return compare;
            }

            compare = Integer.compare(this.silver, c.silver);
            if (compare != 0) {
                return compare;
            }

            return Integer.compare(this.bronze, c.bronze);
        }
    }
}
