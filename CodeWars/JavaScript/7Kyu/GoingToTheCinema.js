// URL: https://www.codewars.com/kata/562f91ff6a8b77dfe900006e/train/javascript

function movie(card, ticket, perc) {
    hasPassed = false;
    
    systemA = 0;
    systemB = card;
    count = 1;
    
    while(hasPassed === false){
      systemA += ticket  
      systemB += ticket*(perc**count);

      if(systemA>Math.ceil(systemB)){
        hasPassed = true;

        return count;
      }
      
      count += 1
    }
  };
  
console.log(movie(500, 15, 0.9));