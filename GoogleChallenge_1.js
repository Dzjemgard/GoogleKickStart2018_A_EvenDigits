// Google Kickstart Challenge
// https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edf/00000000000510ed

// vars
//userInputValue = prompt("Integer: ")
var userInputValue = "1340";
myArray = [];

var U = '';
var O = '';
var L = '';

// Turn the input into an array of numbers
for(i = 0; i < userInputValue.length; i++ ){
    myArray.push(parseInt(userInputValue[i]))
}

// Copies of Arrays that is not coupled to the first one 
upArray = myArray.slice();
downArray = myArray.slice();

// Decreasing option
for(i = 0; i < downArray.length; i++){

    n = downArray[i];
    if (n%2 != 0){
        n--;
        downArray[i] = n; 
    }
 
    // special case when the digit to the left is zeroed out 
    // and all the ones on the right have to be 8

    if ((downArray.length > i > 0) && (downArray[i-1] < myArray[i-1])){
        for(j = i; j < downArray.length; j++){
            downArray[j] = 8;
        }
    }

}

// Increasing option
for(i = 0; i < upArray.length; i++){

    n = upArray[i];
    if (n%2 != 0){
        n++;
        upArray[i] = n; 
    }
 
    // special case when the digit to the left is zeroed out 
    // and all the ones on the right have to be 8

    if ((upArray.length > i > 0) && (upArray[i-1] > myArray[i-1])){
        for(j = i; j < upArray.length; j++){
            upArray[j] = 0;
        }
    }

}

// Formatting and comparison
for (i = 0; i < downArray.length; i++){
    // Lower value Array to string
    if(downArray[i] != 0){
        L = L.concat(downArray[i].toString());
    }
    // Original value Array to string
    if(myArray[0] != 0){
        O = O.concat(myArray[i].toString());
    }
    // Upper value Array to string
    if(upArray[0] != 0){
        U = U.concat(upArray[i].toString());
    }
    
}

L_num = parseInt(L);
O_num = parseInt(O);
U_num = parseInt(U);

// Determining the differences
var UpperDifference = U_num - O_num;
var LowerDifference = O_num - L_num;

UpperDifference < LowerDifference ? console.log(U_num) : console.log(L_num);