public class ConvertAStringToANumber {
  public static int stringToNumber(String str) {
    int number = Integer.parseInt(str);		
    return number;
  }
  public static void main(String[] args) {
	String str = "10";
	System.out.println(stringToNumber(str));
  }
}
