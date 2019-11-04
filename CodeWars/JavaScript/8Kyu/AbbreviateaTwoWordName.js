function abbrevName(name){

    name = name.split(' ');
    let abbrevString = "";

    for (let i=0;i<name.length;i++){
        abbrevString += name[i][0].toUpperCase() + ".";
    }
    
    return abbrevString.slice(0,-1);
}

console.log(abbrevName("Sam Harris"));