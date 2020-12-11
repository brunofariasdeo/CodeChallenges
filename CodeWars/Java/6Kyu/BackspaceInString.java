// URL: https://www.codewars.com/kata/5727bb0fe81185ae62000ae3/train/java

public class BackspaceInString {
    public static String cleanString(String s) {
        String stringWithBackspace = "";

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '#') {
                if (stringWithBackspace.length() > 0) {
                    stringWithBackspace = stringWithBackspace.substring(0, stringWithBackspace.length() - 1);
                }
            } else {
                stringWithBackspace += s.charAt(i);
            }
        }

        return stringWithBackspace;
    }

    public static void main(String[] args) {
        System.out.println(cleanString("abc#d##c"));
        System.out.println(cleanString("abc####d##c#"));
    }
}