// URL: https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/javascript

function score( dice ) {
  const counts = {};
  const points = {
    '1':{1: 100, 3: 1000},
    '2':{3: 200},
    '3':{3: 300},
    '4':{3: 400},
    '5':{1: 50, 3: 500},
    '6':{3: 600}
  }

  let score = 0;

  for (const num of dice) {
    counts[num] = counts[num] ? counts[num] + 1 : 1;
  }

  for (const number in counts){

    if ((counts[number] / 3) >= 1){
      score += points[number][3];

      if(points[number][1]){
        score+=(counts[number] - 3) * points[number][1];
      }

    }
    else{
      if(points[number][1]){
        score+=(counts[number]) * points[number][1];
      }
    }
  }

  return score;
}

console.log(score([6, 6, 6, 2, 2]));