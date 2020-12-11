// URL: https://www.codewars.com/kata/5a25ac6ac5e284cfbe000111/train/javascript

function triangle(row) {
    let combinations = {"GG":"G", "RR":"R", "BB":"B", "BG":"R", "GR":"B", "BR":"G"};

    let colorsList = row.split("");
    let lastCharacterFound = false;

    while (lastCharacterFound == false){
        for (let i=0; i<colorsList.length; i++){

            if ((i+1)>=colorsList.length){
                if (colorsList.length === 1){
                    return colorsList[0];
                }
                else{
                    colorsList.pop();

                    if (colorsList.length === 1){
                        return colorsList[0];
                    }
                }
            }
            else{
                firstColor = colorsList[i];
                secondColor = colorsList[i+1];
                combination = [firstColor, secondColor].sort();
                colorsList[i] = combinations[`${combination[0]}${combination[1]}`];
            }
        }
    }
}

console.log(triangle("RGBG"));