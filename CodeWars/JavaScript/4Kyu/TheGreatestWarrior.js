// URL: https://www.codewars.com/kata/the-greatest-warrior/train/javascript

class Warrior{
  constructor(levelAtt=1, experience = 100, rank = "Pushover", achievements = []){
    this.levelAtt = levelAtt;
    this.experienceAtt = experience;
    this.rankAtt = rank
    this.tiers = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
    this.achievementsAtt = []
  }

  level(){
    return this.levelAtt;
  }

  experience(){
    return this.experienceAtt;
  }

  rank(){
    return this.rankAtt;
  }

  achievements(){
    return this.achievementsAtt;
  }


  setLevel(){
    if ((Math.floor(this.experienceAtt/100)) !== this.levelAtt){
      this.levelAtt = Math.floor(this.experienceAtt / 100);
    }
  }

  setRank(){
    if ((this.tiers[Math.floor(this.levelAtt/10)]) != this.rankAtt){
      this.rankAtt = this.tiers[Math.floor(this.levelAtt/10)];
    }
  }

  setExperience (experience){
    if ((this.experienceAtt + experience)<=10000){
      this.experienceAtt += experience;
    }
    else{
      this.experienceAtt = 10000;
    }
  }

  getRank(level){
    let rank = Math.floor(level/10);
    return rank + 1;
  }

  battle(enemyLevel){
    if (!(enemyLevel >= 1 && enemyLevel<=100)){
      return "Invalid level";
    }
    else{
      if (this.levelAtt === enemyLevel){
        this.setExperience(10);
      }
      else if ((this.levelAtt - enemyLevel) === 1){
        this.setExperience(5);
      }
      else if ((this.levelAtt - enemyLevel) === 2){
        this.setExperience(0);
      }
      else if ((this.levelAtt - enemyLevel) < 0){
        let thisRank = [this.getRank(this.levelAtt),this.rankAtt];
        let enemyRank = [this.getRank(enemyLevel),this.tiers [Math.floor(enemyLevel/10)]];

        if ((enemyRank[0] - thisRank[0])< 1 || ((enemyLevel - this.levelAtt) < 5)){
          this.setExperience(20 * ((enemyLevel - this.levelAtt)**2));
        }
        else{
          return "You've been defeated";
        }
      }
    }
    
    if ((this.levelAtt - enemyLevel) >= 2){
      this.setLevel();
      this.setRank();
      return "Easy fight";
    }
    else if ((this.levelAtt - enemyLevel) >= 0 && (this.levelAtt - enemyLevel) < 2){
      this.setLevel();
      this.setRank();
      return "A good fight";
    }
    else if ((this.levelAtt - enemyLevel) <= 0){
      this.setLevel();
      this.setRank();
      return "An intense fight";
    }
  }

  training(value){
    if (value[2] <= this.levelAtt){
      this.setExperience(value[1])
      this.achievementsAtt.push(value[0])
      this.setLevel()
      this.setRank()
      return value[0]
    }
    else{
      return "Not strong enough"
    }
  }
}