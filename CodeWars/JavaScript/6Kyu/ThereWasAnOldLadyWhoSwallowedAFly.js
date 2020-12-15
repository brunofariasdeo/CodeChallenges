// URL: https://www.codewars.com/kata/5a68ffe3e626c5e85700002d/train/javascript

var oldLadySwallows = function(animals) {
    const animalsOrder = ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"];
    let autopsy = [];

    for (let i=0; i<animals.length; i++){
        let currentAnimal = animals[i];

        autopsy.push(currentAnimal);

        if (animalsOrder.indexOf(currentAnimal)-1 >=0){
            let previousAnimal = animalsOrder[animalsOrder.indexOf(currentAnimal)-1];
            
            if (autopsy.includes(previousAnimal)){
                let filteredAutopsy= autopsy.filter(function(animal){
                    return animal !== previousAnimal;
                })

                autopsy = filteredAutopsy;
            }
        }

        if(animalsOrder.indexOf(currentAnimal)+1 < animalsOrder.length){
            let nextAnimal = animalsOrder[animalsOrder.indexOf(currentAnimal)+1];

            if (autopsy.includes(nextAnimal)){
                let filteredAutopsy= autopsy.filter(function(animal){
                    return animal !== currentAnimal;  
                })

                autopsy = filteredAutopsy;
            }
        }

        if (currentAnimal === "horse"){
            return autopsy;
        }
    }

    return autopsy;
}

console.log(oldLadySwallows(["fly"]));
console.log(oldLadySwallows(["fly","spider"]));
console.log(oldLadySwallows(["fly","spider","bird"]));
console.log(oldLadySwallows(["bird","fly","spider"]));
console.log(oldLadySwallows(["bird","fly","spider","fly"]));
console.log(oldLadySwallows(["spider","spider","spider","spider","bird"]))
