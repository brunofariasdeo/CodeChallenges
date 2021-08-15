import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.stream.*;

public class HammingCode {

    public static String encode(String text) {
        List<String> letters = new ArrayList<String>();

        char[] chars = text.toCharArray();

        for (char ch: chars){
            int asciiNumber = (int) ch;

            String binary = Integer.toBinaryString(asciiNumber);

            while(binary.length()<8){
                binary = "0" + binary;
            }

            char[] numbers = binary.toCharArray();

            for (char number: numbers){
                letters.addAll(Collections.nCopies(3, Character.toString(number)));
            }
        }

        return String.join("", letters);
    }

    public static String decode(String text) {
        String letters = "";
        
        for (int i = 0; i < text.length(); i += 3) {
            String threeCharacters = text.substring(i, i + 3);
            
            List<String> threeCharactersList = Arrays.asList(threeCharacters.split(""));

            Map<String, Long> occurrences = 
                threeCharactersList.stream().collect(Collectors.groupingBy(w -> w, Collectors.counting()));
            
            System.out.println("oxe");
            System.out.println(occurrences);

            if (occurrences.containsKey("1")){
                letters += '1';
            }
            else{
                letters += '0';
            }
        }

        List<String> asciLetters = new ArrayList<String>();

        for (int i = 0; i < letters.length(); i += 8) {
            String asciLetter = letters.substring(i, i + 8);
            
            asciLetters.add(Character.toString((char) Integer.parseInt(asciLetter,2)));
        }

        return String.join("", asciLetters);
    }

  public static void main(String[] args) {
    // System.out.println(encode("hey"));
    System.out.println(decode("000111111000111000000000000111111000000111000111000111111111111000000111"));
  }
}