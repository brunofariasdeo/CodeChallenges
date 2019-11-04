function wordsToMarks(string){
    let value = 0;

    for (i=0; i<string.length;i++){
        value += string[i].charCodeAt()-96;
    }

    return value;
}

console.log(wordsToMarks('attitude'));