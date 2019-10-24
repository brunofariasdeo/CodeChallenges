
public class CatYearsDogYears2 {
	public static int[] ownedCatAndDog(final int catYears, final int dogYears) {
		int ownedCat;
		int ownedDog;
		
		if (catYears >= 0 && catYears <15) {
	        ownedCat = 0;
		}
		else if (catYears >= 15 && catYears < 24) {
	        ownedCat = 1;
		}
	    else {
	        ownedCat = ((catYears-24)/4)+2;
	    }

	    if (dogYears >= 0 && dogYears <15) {
	        ownedDog = 0;
	    }
	    else if (dogYears >= 15 && dogYears < 24) {
	        ownedDog = 1;
	    }
	    else {
	        ownedDog = ((dogYears-24)/5)+2;
	    }
	    
	    System.out.println(ownedCat);
	    System.out.println(ownedDog);
	    return new int[]{ownedCat, ownedDog};
		
	  }
	
	public static void main(String[] args) {
		int catYears = 1;
		int dogYears = 1;
		System.out.println(ownedCatAndDog(catYears,dogYears));
	}
}
