
public class FindTheIntegral {
	public static String integrate(int coefficient, int exponent) {
		return ((coefficient/(exponent+1))+"x^"+(exponent+1)); 
    }
	public static void main(String[] args) {
		String a = integrate(3,2);
		System.out.println(a);
	}
}

