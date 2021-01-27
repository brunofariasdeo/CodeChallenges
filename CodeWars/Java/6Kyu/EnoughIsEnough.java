// URL: https://www.codewars.com/kata/554ca54ffa7d91b236000023/solutions/java

import java.lang.*;
import java.util.*;

public class EnoughIsEnough {

  public static int[] deleteNth(int[] elements, int maxOccurrences) {
    HashMap<Integer, Integer> numbers = new HashMap<Integer, Integer>();

    int[] newArray = new int[0];

    for (int i = 0; i < elements.length; i++) {
      if (numbers.containsKey(elements[i])) {
        numbers.put(elements[i], numbers.get(elements[i]) + 1);
      } else {
        numbers.put(elements[i], 1);
      }

      if (numbers.get(elements[i]) <= maxOccurrences) {
        newArray = Arrays.copyOf(newArray, newArray.length + 1);
        newArray[newArray.length - 1] = elements[i];
      }

    }
    return newArray;
  }

  public static void main(String[] args) {
    System.out.println(deleteNth(new int[] { 20, 37, 20, 21 }, 1));
  }
}