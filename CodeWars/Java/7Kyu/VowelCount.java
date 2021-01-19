// URL: https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/java

import java.util.*;

public class VowelCount {

  public static int getCount(String str) {
    int vowelsCount = 0;

    List<String> vowels = Arrays.asList("a", "e", "i", "o", "u");

    for (int i = 0; i < str.length(); i++) {
      if (vowels.contains(String.valueOf(str.charAt(i)))) {
        vowelsCount += 1;
      }
    }

    return vowelsCount;
  }

}