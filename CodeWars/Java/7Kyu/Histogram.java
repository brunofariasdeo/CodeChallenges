import java.util.Arrays;

public class Histogram {
	public static String histogram(final int results[]) {
		String[]result = new String[results.length+1];
		for(int i = (results.length-1); i >= 0; i--){
			if (results[i] != 0) {
				result[5-i] = (i+1) + "|" + "#".repeat(results[i]) + " " + results[i];
			}
			else {
				result[5-i] = (i+1) + "|" + "#".repeat(results[i]);
			}
		}
	    return String.join("\n", result);
	  }
	
	public static void main(String[] args) {
		int[] my_array = {10, 8, 6, 6, 8, 12};
		System.out.println(histogram(my_array));
		}
}

//"6|##### 5\n"+
//"5|\n"+
//"4|# 1\n"+
//"3|########## 10\n"+
//"2|### 3\n"+
//"1|####### 7\n";