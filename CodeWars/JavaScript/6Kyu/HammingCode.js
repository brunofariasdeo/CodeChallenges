// URL: https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e/train/javascript

function encode(text) {
    let letters = [];

    for (character of text){
        byte = character.charCodeAt(0).toString(2);
        
        while(byte.length<8){
            byte = '0' + byte;
        }

        for (bit of byte){
            letters.push(bit.repeat(3));
        }
    }

    return letters.join('');
}

function decode(bits) {
    let letters = '';

    for (let i = 0, charsLength = bits.length; i < charsLength; i += 3) {
        const threeCharacters = bits.substring(i, i + 3);
        
        if (threeCharacters.replace(/[^1]/g, "").length > threeCharacters.replace(/[^0]/g, "").length){
            letters += '1';
        }
        else{
            letters += '0';
        }
    }
    
    let asciLetters = [];

    for (let i = 0, charsLength = letters.length; i < charsLength; i += 8) {
        const asciLetter = letters.substring(i, i + 8);
        
        asciLetters.push(String.fromCodePoint(parseInt(asciLetter, 2)));
    }

    return asciLetters.join('');
}

console.log(decode("100111111000111001000010000111111000000111001111000111110110111000010111"));