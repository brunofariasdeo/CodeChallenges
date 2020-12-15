// URL: https://www.codewars.com/kata/593c9175933500f33400003e/train/java

public class ReturnTheFirstmMultiplesOfn {
    public static int[] multiples(int m, int n) {
        int[] multiplesArray = new int[m];
        int count = 0;

        for (int i = n; i <= Math.abs(m * n); i = i + n) {
            multiplesArray[count] = i;

            if (Math.abs(i) == Math.abs(m * n)) {
                break;
            }

            count += 1;
        }

        return multiplesArray;
    }

    public static void main(String[] args) {
        System.out.println(multiples(3, 5));
    }
}
