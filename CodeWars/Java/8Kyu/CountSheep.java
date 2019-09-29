public class CountSheep {
	public static int countSheeps(Boolean[] arrayOfSheeps) {
		int sheepsCount = 0;
		for(int i = 0; i < arrayOfSheeps.length; i++){
			if (arrayOfSheeps[i] != null){
				if (arrayOfSheeps[i] == true) {
					sheepsCount += 1;
				}
			}
		}
		return sheepsCount;
		}
	
	public static void main(String[] args) {
		Boolean[] my_array = {true,  true, false, null};
		System.out.println(countSheeps(my_array));
		}
}