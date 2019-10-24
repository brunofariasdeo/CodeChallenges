import javax.swing.*;
import java.math.*;

public class YoureASquare {
	public static boolean isSquare(int n) {
	    double root = Math.sqrt(n);
	    double rootRounded = Math.round(root);
	    if (Math.pow(rootRounded, 2)==n){
		      return true;
	    }
	    else {
		      return false;
	    }
}
	public static void main(String[] args) {
		boolean a = isSquare(65701352);
		System.out.println(a);
	}
}
