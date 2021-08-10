// URL: https://www.codewars.com/kata/562f91ff6a8b77dfe900006e/train/java

import java.lang.Math;

public class Movie {
    
    public static int movie(int card, int ticket, double perc) {
        Boolean hasPassed = false;
    
        float systemA = 0;
        float systemB = card;
        int count = 1;

        while(hasPassed == false){
          systemA += ticket;  
          systemB += ticket*(Math.pow(perc, count));

          if(systemA>Math.ceil(systemB)){
            hasPassed = true;

            break;
          }
          
          count += 1;
        }
      
        return count;
    }
}