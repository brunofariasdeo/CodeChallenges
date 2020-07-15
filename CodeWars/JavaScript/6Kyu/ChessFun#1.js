// URL: https://www.codewars.com/kata/5894134c8afa3618c9000146/train/javascript

function chessBoardCellColor(cell1, cell2) {
    cells = [cell1, cell2]
    colorful = []

    for(let i=0; i<cells.length; i++){
        if(parseInt(cells[i][0].charCodeAt(0)) % 2 === 0){
            if (parseInt(cells[i][1]) % 2 === 0){
                colorful.push(true)
            }
            else{
                colorful.push(false)
            }
        }
        else{
            if (parseInt(cells[i][1]) % 2 === 0){
                colorful.push(false)
            }
            else{
                colorful.push(true)
            }
        }
    }

    if (colorful[0] === colorful[1]){
        return true
    }
    else{
        return false
    }
}

console.log(chessBoardCellColor("A1","A2"))