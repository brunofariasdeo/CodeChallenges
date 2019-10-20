function warnTheSheep(queue) {
    for (i=0; i<queue.length;i++){
      if (queue[i] == "wolf"){
        if (i+1 === queue.length){
          return "Pls go away and stop eating my sheep";
        }
        else{
          return `Oi! Sheep number ${queue.length-(i+1)}! You are about to be eaten by a wolf!`
        }
      }
    }
  }