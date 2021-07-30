function maxBall(v0) {
  speedConverted = v0/3.6;
  heights = [];
  
  for(let i = 0; i<=speedConverted/2; i=i+0.1){
    height = speedConverted*(i) - 0.5*9.81*(i)*(i); 
    
    heights.push(height);
  }
  
  return heights.indexOf(Math.max( ...heights ));
}

console.log(maxBall(15));