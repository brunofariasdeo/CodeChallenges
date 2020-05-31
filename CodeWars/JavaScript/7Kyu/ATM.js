// URL: https://www.codewars.com/kata/5635e7cb49adc7b54500001c/train/javascript

function solve(n) {
    notesAvailable = [10,20,50,100,200,500];

    enoughNotes = false;
    numberOfNotes = 0;
    count = 5;

    while (enoughNotes==false){

        if ((n % notesAvailable[count]) === 0){
            numberOfNotes += n/notesAvailable[count];
            enoughNotes = true;
           
        }
        else{
            numberOfNotes += Math.trunc(n/notesAvailable[count]);
            n = n - ((Math.trunc(n/notesAvailable[count]))*(notesAvailable[count]))
        }

        if(count == 0 && enoughNotes == false){
            return -1;
        }
        
        count -= 1;
    }
    return numberOfNotes;
}

