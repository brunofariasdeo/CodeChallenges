// URL https://www.codewars.com/kata/online-rpg-player-to-qualifying-stage/train/javascript
function playerRankUp (points) {
  if (points >= 100){
    return "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up.";
  }
  else{
    return false;
  }
}