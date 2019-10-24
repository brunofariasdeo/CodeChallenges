// URL: https://www.codewars.com/kata/dna-to-rna-conversion/train/javascript

function DNAtoRNA(dna) {
  RNA = ""
  
  for (i=0;i<dna.length;i++){
    if (dna[i] == "T"){
      RNA+= "U";
    }
    else{
      RNA += dna[i];
    }
  }
  return RNA; 
}