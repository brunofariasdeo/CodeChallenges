// URL: https://www.codewars.com/kata/59f11118a5e129e591000134/train/java

import java.util.*;

public class SumOfArraySingles {
    public static int repeats(int[] arr) {
        Hashtable<Integer, Integer> numbers = new Hashtable<Integer, Integer>();

        int sum = 0;

        for (int i = 0; i < arr.length; i++) {
            if (numbers.containsKey(arr[i])) {
                numbers.put(arr[i], numbers.get(arr[i]) + 1);
            } else {
                numbers.put(arr[i], 1);
            }
        }

        Set<Integer> setOfNumbers = numbers.keySet();

        for (Integer key : setOfNumbers) {
            if (numbers.get(key) == 1) {
                sum += key;
            }
        }

        return sum;
    }

    public static void main(String[] args) {
        System.out.println(repeats(new int[] { 4, 5, 7, 5, 4, 8 }));
    }
}
