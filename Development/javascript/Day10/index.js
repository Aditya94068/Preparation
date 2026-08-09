//Execution Context
//Memory allocation
//a = undefined
//b = undefined
//addNumber = function Code
//sumResult1 = undefined
//sumResult2 = undefined



//Execution phase
// console.log(a);//undefined
// var a = 10;
// // console.log(a);//10
// var b = 20;
// var sumResult1 = addNumber(a,b);//yhape 30 print isliye hoga kyu ki memory phase main addNumber() function ke andar actual code present hai
// console.log(sumResult1);

// function addNumber(num1,num2){
//     var sum = num1 + num2;
//     return sum;
// }
// // var sumResult1 = addNumber(a,b);
// var sumResult2 = addNumber(4,5);
// console.log(sumResult1 , sumResult2);



//Let const 
//Excution Context Create hoga 
// Memory allocation 
// a = <uninitialised>(Temporal dead zone) iska mtlb hai ki jab tak a ke andar koi value nhi chali jaye tab tak hum a ko access nhi kar sakte
// b = <uninitialised>(Temporal dead zone)
//Temporal dead zone ka mtlb hai ki main aapko memory allocate kar rha hu per jab tak aapke andar koi value nhi ajati tab tak main aapko access nhi kar sakta , var ke case main wo undefined rakh deta hai
//add number = <uninitialised>(Temporal dead zone)
//Execution phase
//a = 10
//b = 20
// add number = function Code
// result = 30
// let a = 10;
// const b = 20;
// const addNumber = function(num1,num2){
//     const sum = num1 + num2;
//     return sum;
// }
// const result = addNumber(a,b);
// console.log(result);


const sum = (a , b) => (a + b);

let a = 4;
let b = 5;
console.log(sum(a,b));


















