// URL: https://www.codewars.com/kata/554b4ac871d6813a03000035/train/java

import java.util.Arrays;

public class HighestAndLowest {
    public static String highAndLow(String numbers) {
        String[] stringArray = numbers.split(" ");
        int[] intArray = new int[stringArray.length];

        for (int i = 0; i < stringArray.length; i++) {
            intArray[i] = Integer.parseInt(stringArray[i]);
        }

        Arrays.sort(intArray);

        return String.format("%d %d", intArray[0], intArray[intArray.length - 1]);
    }

    public static void main(String[] args) {
        System.out.println(highAndLow("1 2"));
    }
}