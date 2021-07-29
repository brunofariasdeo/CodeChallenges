// URL: https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce/solutions/java

import java.util.*;

class Kata {
  public static String multiTable(int num) {

    ArrayList<String> multiplicationTable = new ArrayList<String>();

    for (int i = 1; i <= 10; i++) {
      multiplicationTable.add(String.format("%d * %d = %d", i, num, i * num));
    }

    String joinedString = String.join("\n", multiplicationTable);

    return joinedString;
  }
}