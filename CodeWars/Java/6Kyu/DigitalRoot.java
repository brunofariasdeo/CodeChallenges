// URL: https://www.codewars.com/kata/541c8630095125aba6000c00/train/java

import java.util.stream.*;
import java.util.Arrays;

public class DigitalRoot {
  public static int digital_root(int n) {
    boolean digitalRootFound = false;

    while (digitalRootFound == false) {
      String[] m = Integer.toString(n).split("");
      int[] arr = new int[m.length];

      for (int i = 0; i < m.length; i++) {
        arr[i] = Integer.parseInt(m[i]);
      }

      n = sum(arr);

      if (Integer.toString(n).length() == 1) {
        digitalRootFound = true;
      }
    }

    return n;
  }

  public static int sum(int[] n) {
    return IntStream.of(n).sum();
  }

  public static void main(String[] args) {
    System.out.println(digital_root(523));
  }
}