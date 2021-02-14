// URL: https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/java

public class Mumbling {

  public static String accum(String s) {
    String mumbleString = "";

    for (int i = 0; i < s.length(); i++) {
      mumbleString += Character.toString(s.charAt(i)).toUpperCase()
          + Character.toString(s.charAt(i)).toLowerCase().repeat(i) + "-";
    }

    return mumbleString.substring(0, mumbleString.length() - 1);
  }
}