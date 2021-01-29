// URL: https://www.codewars.com/kata/5941c545f5c394fef900000c/train/java

import java.util.*;

public class Warrior {

  private int level = 1;
  private double experience = 100;
  private String rank = "Pushover";
  private List<String> achievements = new ArrayList<String>();

  public Warrior() {

  }

  public int level() {
    return this.level;
  }

  public int experience() {
    return (int) this.experience;
  }

  public String rank() {
    return this.rank;
  }

  public List<String> achievements() {
    return this.achievements;
  }

  public void setLevel() {
    if (((int) (this.experience / 100)) != this.level) {
      this.level = (int) (this.experience / 100);
    }
    System.out.println("level" + this.level);
    System.out.println("experience" + this.experience);
  }

  public void setRank() {
    List<String> tiers = new ArrayList<>(Arrays.asList("Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage",
        "Elite", "Conqueror", "Champion", "Master", "Greatest"));
    if ((tiers.get((int) (this.level / 10))) != this.rank) {
      this.rank = tiers.get((int) (this.level / 10));
    }
  }

  public void setExperience(double experience) {
    if ((this.experience + experience) <= 10000) {
      this.experience += experience;
    } else {
      this.experience = 10000;
    }
  }

  public int getRank(int level) {
    int rank = (int) (level / 10);
    return rank + 1;
  }

  public String battle(int enemyLevel) {
    List<String> tiers = new ArrayList<>(Arrays.asList("Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage",
        "Elite", "Conqueror", "Champion", "Master", "Greatest"));

    if (!(enemyLevel >= 1 && enemyLevel <= 100)) {
      return "Invalid level";
    } else {
      if (this.level == enemyLevel) {
        this.setExperience(10);
      } else if ((this.level - enemyLevel) == 1) {
        this.setExperience(5);
      } else if ((this.level - enemyLevel) == 2) {
        this.setExperience(0);
      } else if ((this.level - enemyLevel) < 0) {
        int thisRank = this.getRank(this.level);
        int enemyRank = this.getRank(enemyLevel);

        if ((enemyRank - thisRank) < 1 || ((enemyLevel - this.level) < 5)) {
          this.setExperience(20 * Math.pow((enemyLevel - this.level), 2));
        } else {
          return "You've been defeated";
        }
      }
    }

    if ((this.level - enemyLevel) >= 2) {
      this.setLevel();
      this.setRank();
      return "Easy fight";
    } else if ((this.level - enemyLevel) >= 0 && (this.level - enemyLevel) < 2) {
      this.setLevel();
      this.setRank();
      return "A good fight";
    } else if ((this.level - enemyLevel) <= 0) {
      this.setLevel();
      this.setRank();
      return "An intense fight";
    }

    return "dale";
  }

  public String training(String description, int experience, int minimumLevel) {
    if (minimumLevel <= this.level) {
      this.setExperience(experience);
      this.achievements.add(description);
      this.setLevel();
      this.setRank();
      return description;
    } else {
      return "Not strong enough";
    }
  }

  public static void main(String[] args) {
    Warrior tom = new Warrior();
    System.out.println(tom.level());
    System.out.println(tom.experience());
    System.out.println(tom.rank());
    System.out.println(tom.achievements());
    System.out.println(tom.training("Defeated Chuck Norris", 9000, 1));
    System.out.println(tom.experience());
    System.out.println(tom.level());
    System.out.println(tom.rank());
    System.out.println(tom.battle(90));
    System.out.println(tom.experience());
    System.out.println(tom.achievements());
  }
}