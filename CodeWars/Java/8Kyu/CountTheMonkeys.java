public class CountTheMonkeys {
	public static int[] monkeyCount(final int n){
		int[]count = new int[n];
		for(int i = 0; i < n; i++){
			count[i] = i+1;
			System.out.println(count[i]);
		}
		return count;
		}
	
	public static void main(String[] args) {
			int n = 15;
			System.out.println(monkeyCount(n));
		}
}