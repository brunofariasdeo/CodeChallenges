// URL: https://www.codewars.com/kata/5949481f86420f59480000e7/train/java

import java.util.*;

public class OddOrEven {
  public static String oddOrEven(int[] array) {
    OptionalInt sum = Arrays.stream(array).reduce((n1, n2) -> n1 + n2);

    return (sum.getAsInt() % 2 == 0) ? "even" : "odd";
  }
}