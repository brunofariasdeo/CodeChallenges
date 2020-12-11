// URL: https://www.codewars.com/kata/5727bb0fe81185ae62000ae3/train/javascript

function cleanString(s) {
    stringWithBackspace = "";

	for (let i=0; i<s.length; i++){
        if (s[i] === "#"){
            if(s.length>0){
                stringWithBackspace = stringWithBackspace.substr(0,stringWithBackspace.length-1);
            }
        }
        else{
            stringWithBackspace += s[i];
        }
    }

    return stringWithBackspace;
};

console.log(cleanString('abc#d##c'));