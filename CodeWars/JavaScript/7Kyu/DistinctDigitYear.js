function distinctDigitYear(year) {
  for (i=year+1;i<=9000;i++){
    yearString = i.toString()
    
    let foundDuplicate = false;
    for (j=0;j<yearString.length-1;j++){
      if (yearString.slice(j+1,yearString.length).includes(yearString[j])){
        foundDuplicate = true;

      }
    }
    
    if (foundDuplicate == false){
      return i;
    }
  }
}

distinctDigitYear(1987)