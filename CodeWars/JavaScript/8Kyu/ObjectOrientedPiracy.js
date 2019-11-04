// URL: https://www.codewars.com/kata/regular-ball-super-ball/train/javascript
class Ship {
  constructor(draft, crew) {
    this.draft = draft;
    this.crew = crew;
  }

  isWorthIt(){
    if ((this.draft - this.crew*1.5) > 20){
      return true;
    }
    else{
      return false;
    }
  }
}

var titanic = new Ship(15, 10);
console.log(titanic.isWorthIt());