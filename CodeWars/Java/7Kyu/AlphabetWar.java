import java.util.*;

public class AlphabetWar {
  public static String alphabetWar(String fight) {
    HashMap<String, Integer> alphabet = new HashMap<String, Integer>();
    alphabet.put("w", -4);
    alphabet.put("p", -3);
    alphabet.put("b", -2);
    alphabet.put("s", -1);
    alphabet.put("m", 4);
    alphabet.put("q", 3);
    alphabet.put("d", 2);
    alphabet.put("z", 1);

    int score = 0;

    for (int i = 0; i < fight.length(); i++) {
      if (alphabet.containsKey(Character.toString(fight.charAt(i)))) {
        score += alphabet.get(Character.toString(fight.charAt(i)));
      }
    }

    if (score > 0) {
      return "Right side wins!";
    } else if (score == 0) {
      return "Let's fight again!";
    } else {
      return "Left side wins!";
    }
  }

  public static void main(String[] args) {
    System.out.println(alphabetWar("z"));
  }
}