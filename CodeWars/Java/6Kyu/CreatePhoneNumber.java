// URL: https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/java

import java.util.stream.*;
import java.util.Arrays;

public class CreatePhoneNumber {
  public static String createPhoneNumber(int[] numbers) {
    String numbersString = Arrays.stream(numbers)
        .mapToObj(String::valueOf)
        .collect(Collectors.joining(""));

    return new StringBuilder()
        .append("(" + numbersString.substring(0,3) + ") ")
        .append(numbersString.substring(3,6) + "-")
        .append(numbersString.substring(6,10))
        .toString();
  }

  public static void main(String[] args) {
      System.out.println(createPhoneNumber(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}));

    }
}