// URL: https://www.codewars.com/kata/57d814e4950d8489720008db/train/java

public class NthPower {
  public static int nthPower(int[] array, int n) {
    int number = (array.length > n) ? (int) Math.pow(array[n], n) : -1;
    return number;
  }
}