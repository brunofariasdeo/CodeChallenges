// URL: https://www.codewars.com/kata/5946a0a64a2c5b596500019a/train/javascript

function splitAndAdd(arr, n) {

    repeatRequired = true;

    while (repeatRequired==true){

        n=n-1;

        firstArray = arr.slice(0,arr.length/2)
        secondArray = arr.slice(arr.length/2,arr.length)

        arr = [];
        if (firstArray.length !== secondArray.length){

            equalLength = false;

            while (equalLength == false){

                if (firstArray.length === secondArray.length){    
                    equalLength = true;
                }

                else{
                    if (firstArray.length>secondArray.length){
                        secondArray.unshift(0);
                    }
                    else{
                        firstArray.unshift(0);
                    }
                }
            }
        }

        for (i=0;i<firstArray.length;i++){
            arr.push(firstArray[i] + secondArray[i]);
        }


        if (n==0){
            repeatRequired = false;
        }
    }

    return arr;

}

console.log(splitAndAdd([4,2,5,3,2,5,7], 2));
console.log(splitAndAdd([3,234,25,345,45,34,234,235,345,34,534,45,645,645,645,4656,45,3], 4));