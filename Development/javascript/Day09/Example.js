
// function largestNumber(a , b){
//     if (a > b ){
//         return "a";
//     }else{
//         return "b";
//     }
// }
// function largestNumberInArray(arr){
//     let maxi = -1;
//     for(let i = 0;i<arr.length;i++){
//         if(arr[i] > maxi){
//             maxi = arr[i];
//         }
//     }
//     return maxi;
// }
// let a = 100;
// let b = 200;
// let ans = largestNumber(a,b)
// console.log(ans);

// let arr = [10,20,300,740,50];
// let result = largestNumberInArray(arr);
// console.log(result);

// let arr = [1,1,1,1,1,1,1];
// let arr2 = [1,1,1,1,1,1];
// let resultArray = [...arr,...arr2];
// let sum = 0;
// for(let i of resultArray){
//     sum += i;
// }
// console.log(sum);
// console.log(resultArray);

// function AreaOfCircle(radius){
//     return Math.PI * radius * radius;
// }
// console.log(AreaOfCircle(2));

// function additionOFMultiNumbers(...num){
//     let sum = 0;
//     for(let val of num){
//         sum += val;
//     }
//     return sum
// }
// console.log(additionOFMultiNumbers(10,20,30,40,50));

// const add = function additionOFMultiNumbers(...num){
//     let sum = 0;
//     for(let val of num){
//         sum += val;
//     }
//     return sum
// }
// console.log(add(10,20,30,40,50));

// const add = (a,b) => (a + b);
// console.log(add(4,5));

// const largestNumber = (arr,arr2) => {
//     let arr3 = [...arr,...arr2];
//     console.log(arr3);
// }
// let arr = [10,2053,30,22,535,633];
// let arr1 = [25,52,6,66];
// console.log(largestNumber(arr,arr1));


// const greeting = () => {
//     return {
//         name :"Aditya",
//         age :20
//     }
// }
// console.log(greeting());

// const greeting = () => ({
//         name :"Aditya",
//         age :20
// })
// console.log(greeting());

// (function example(num1,num2){
//     console.log(`Hello Aditya , Sum : ${num1 + num2}`);
    
// })(4,55)

function doArithmeticOperation(num1,num2,callBack){
        return callBack(num1,num2);
}
function add(a,b) {
    return a + b;
}
function multipy(a,b){
    return a * b;
}
console.log(doArithmeticOperation(4,5,add));
console.log(doArithmeticOperation(4,5,multipy));