import java.util.*;

public class BallUpwards {
  public static int maxBall(int v0) {
    Double speedConverted = v0 / 3.6;
    List<Double> heights = new ArrayList<Double>();

    for (double i = 0; i <= speedConverted / 2; i = i + 0.1) {
      Double height = speedConverted * (i) - 0.5 * 9.81 * (i) * (i);

      heights.add(height);
    }

    return heights.indexOf(Collections.max(heights));
  }

  public static void main(String[] args) {
    System.out.println(maxBall(15));
  }
}