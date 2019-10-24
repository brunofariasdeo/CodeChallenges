
public class CatYearsDogYears {
	public static int[] humanYearsCatYearsDogYears(final int humanYears) {
		int catYears;
		int dogYears;
		
		
		if (humanYears == 1){
	        catYears = 15; 
	        dogYears = 15;
		}
		else if (humanYears == 2){
	        catYears = 15 + 9;
	        dogYears = 15 + 9;
	    }
	    else {
	        catYears = 15 + 9 + (humanYears-2)*4;
	        dogYears = 15 + 9 + (humanYears-2)*5;
	    }
		
	    return new int[]{humanYears, catYears, dogYears};
	  }
	
	public static void main(String[] args) {
		int n = 1;
		System.out.println(humanYearsCatYearsDogYears(n));
	}
}
