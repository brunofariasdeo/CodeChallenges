// URL: https://www.codewars.com/kata/5635e7cb49adc7b54500001c/train/java

public class ATM {
	public static int solve(int n) {
		int[] notesAvailable = { 10,20,50,100,200,500 };

	    boolean enoughNotes = false;
	    int numberOfNotes = 0;
	    int count = 5;

	    while (enoughNotes==false){

	        if ((n % notesAvailable[count]) == 0){
	            numberOfNotes += n/notesAvailable[count];
	            enoughNotes = true;
	           
	        }
	        else{
	            numberOfNotes += (n/notesAvailable[count]);
	            n = n - ((n/notesAvailable[count]))*(notesAvailable[count]);
	        }

	        if(count == 0 && enoughNotes == false){
	            return -1;
	        }
	        
	        count -= 1;
	    }
	    return numberOfNotes;
	}
	
	public static void main(String[] args) {
		System.out.println(solve(500));
	}
}
