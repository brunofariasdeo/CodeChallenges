public class ReversedSequence {

    public static int[] reverse(int n) {
        int[] array = new int[n];

        for (int i = 0; i < n; i++) {
            array[i] = n - i;
        }

        return array;
    }

    public static void main(String[] args) {
        System.out.println(reverse(1));
    }
}