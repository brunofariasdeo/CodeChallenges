import java.util.*;

public class GreedIsGood {
  public static int greedy(int[] dice) {
    HashMap<String, Integer> counts = new HashMap<String, Integer>();

    HashMap<String, HashMap<Integer, Integer>> points = new HashMap<String, HashMap<Integer, Integer>>();

    HashMap<Integer, Integer> points1 = new HashMap<Integer, Integer>();
    points1.put(1, 100);
    points1.put(3, 1000);
    points.put("1", points1);

    HashMap<Integer, Integer> points2 = new HashMap<Integer, Integer>();
    points2.put(3, 200);
    points.put("2", points2);

    HashMap<Integer, Integer> points3 = new HashMap<Integer, Integer>();
    points3.put(3, 300);
    points.put("3", points3);

    HashMap<Integer, Integer> points4 = new HashMap<Integer, Integer>();
    points4.put(3, 400);
    points.put("4", points4);

    HashMap<Integer, Integer> points5 = new HashMap<Integer, Integer>();
    points5.put(1, 50);
    points5.put(3, 500);
    points.put("5", points5);

    HashMap<Integer, Integer> points6 = new HashMap<Integer, Integer>();
    points6.put(3, 600);
    points.put("6", points6);

    for (int number : dice) {
      String parsedNumber = Integer.toString(number);

      if (counts.containsKey(parsedNumber)) {
        counts.put(parsedNumber, counts.get(parsedNumber) + 1);
      } else {
        counts.put(parsedNumber, 1);
      }
    }

    int score = 0;

    for (String number : counts.keySet()) {
      if ((counts.get(number) / 3) >= 1) {
        score += points.get(number).get(3);

        if (points.get(number).containsKey(1)) {
          score += (counts.get(number) - 3) * points.get(number).get(1);
        }

      } else {
        if (points.get(number).containsKey(1)) {
          score += (counts.get(number)) * points.get(number).get(1);
        }
      }
    }

    return score;
  }

  public static void main(String[] args) {
    System.out.println(greedy(new int[] { 5, 1, 3, 4, 1 }));
  }
}