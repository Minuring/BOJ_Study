import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        var split = scanner.nextLine().split(" ");
        var n = Integer.parseInt(split[0]);
        var k = Integer.parseInt(split[1]);

        Country countryToFind = null;
        var countries = new ArrayList<Country>();
        for (int i = 0; i < n; i++) {
            var spl = scanner.nextLine().split(" ");
            var countryId = Integer.parseInt(spl[0]);
            var gold = Integer.parseInt(spl[1]);
            var silver = Integer.parseInt(spl[2]);
            var bronze = Integer.parseInt(spl[3]);
            var country = new Country(countryId, gold, silver, bronze);
            countries.add(country);
            if (countryId == k) countryToFind = country;
        }

        Collections.sort(countries);
        var rank = getRank(countries, countryToFind);
        System.out.println(rank);
    }

    private static int getRank(final List<Country> countries, final Country countryToFind) {
        if (countries.get(0) == countryToFind) return 1;
        var rank = 1;
        for (int i = 1; i < countries.size(); i++) {
            var before = countries.get(i - 1);
            var cur = countries.get(i);
            if (before.compareTo(cur) != 0) rank++;

            if (cur == countryToFind) break;
        }
        return rank;
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
            var compare = -1 * Integer.compare(this.gold, c.gold);
            if (compare != 0) {
                return compare;
            }

            compare = -1 * Integer.compare(this.silver, c.silver);
            if (compare != 0) {
                return compare;
            }

            return -1 * Integer.compare(this.bronze, c.bronze);
        }
    }
}
