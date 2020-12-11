// URL: https://www.codewars.com/kata/5a25ac6ac5e284cfbe000111/train/java

import java.util.*;

public class ColouredTriangles {

    public static char triangle(final String row) {
        Hashtable<String, String> combinations = new Hashtable<String, String>() {
            {
                put("GG", "G");
                put("RR", "R");
                put("BB", "B");
                put("BG", "R");
                put("GR", "B");
                put("BR", "G");
            }
        };

        List<String> colorsList = new LinkedList<String>(Arrays.asList(row.split("")));

        boolean lastCharacterFound = false;

        while (lastCharacterFound == false) {

            for (int i = 0; i < colorsList.size(); i++) {

                if ((i + 1) >= colorsList.size()) {

                    if (colorsList.size() == 1) {
                        return colorsList.get(0).charAt(0);
                    } else {
                        colorsList.remove(i);

                        if (colorsList.size() == 1) {
                            return colorsList.get(0).charAt(0);
                        }
                    }
                } else {

                    String firstColor = colorsList.get(i);

                    String secondColor = colorsList.get(i + 1);

                    String[] combination = { firstColor, secondColor };
                    Arrays.sort(combination);

                    colorsList.set(i, combinations.get(String.format("%s%s", combination[0], combination[1])));
                }
            }
        }

        return colorsList.get(0).charAt(0);
    }

    public static void main(String[] args) {
        System.out.println(triangle("RGBG"));
    }
}