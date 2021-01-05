// URL: https://www.codewars.com/kata/5a68ffe3e626c5e85700002d/train/java

import java.util.*;

public class ThereWasAnOldLadyWhoSwalloedAFly {
  public static List<String> oldLadySwallows(final List<String> animals) {
    List<String> animalsOrder = Arrays.asList("fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse");
    ArrayList<String> autopsy = new ArrayList<String>();

    for (int i = 0; i < animals.size(); i++) {
      String currentAnimal = animals.get(i);
      autopsy.add(currentAnimal);

      if (animalsOrder.indexOf(currentAnimal) - 1 >= 0) {
        String previousAnimal = animalsOrder.get(animalsOrder.indexOf(currentAnimal) - 1);

        if (autopsy.contains(previousAnimal)) {
          ArrayList<String> filteredAutopsy = autopsy;
          filteredAutopsy.removeIf(animal -> animal.contains(previousAnimal));
          autopsy = filteredAutopsy;
        }
      }

      if (animalsOrder.indexOf(currentAnimal) + 1 < animalsOrder.size()) {
        String nextAnimal = animalsOrder.get(animalsOrder.indexOf(currentAnimal) + 1);

        if (autopsy.contains(nextAnimal)) {
          ArrayList<String> filteredAutopsy = autopsy;
          autopsy.removeIf(animal -> animal.contains(currentAnimal));
          autopsy = filteredAutopsy;
        }
      }

      if (currentAnimal == "horse") {
        return autopsy;
      }
    }

    return autopsy;
  }

  public static void main(String[] args) {
    System.out.println(oldLadySwallows(Arrays.asList(new String[] { "fly", "spider", "bird" })));
  }
}