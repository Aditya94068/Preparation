//Function
//METHOD 1 
// function greeting(){
//     console.log("Hello Coder army");
//     return 4;
// }
//Calling Function
// greeting();
// console.log(greeting());


// function addNumber(num1,num2){//parameter
//     const sum = num1 + num2;
//     console.log(sum);
// }

// addNumber naam ka fuction jo hai usse hum flexible bana chahate hai taki future main hum jitne bhi number function ko pass kare wo un sab ka saam return kar de:-
// Hum yhape rest operation ka use karenge (...) ye kya karta hai ki jo bhi number hum funtion ko pass karte wo uun sab number ko array ke andar dal deta hai

// function addNumber(...num1){
//     let num = 0;
//     for(let i of num1){
//         num = num + i;
//     }
//     console.log(num);
   
// }
// addNumber(3,4);//Argument
// addNumber(5,5,5);
// addNumber(14,3,54,7);
// addNumber(1,43,5,6,7,8);
//---------------------------------------------------
//difference between spread and rest operator

// const arr = [10,20,30,40,50];
// const arr2 = [30,70,90,10];

// const [first,second,...num] = arr; // yhape pe spread operator jo hai wo values ko catch kar leta hai arry ke form main
// console.log(first,second,num);

//spread operator jo hai object ke upar apply karte  ya array ke upar apply karte hai taki hum array ke sabhi values ko individually khol deta hai
// const ans = [...arr,...arr2];
// console.log(ans);
//---------------------------------------------------

//METHOD 2:
//function ko hum ek aur tarike se bna sakte hai
// function : expression

// const addNumber = function(...num){
//         let sum = 0;
//         for(let i of num){
//             sum +=i;
//         }
//         return sum;
// }
// console.log(addNumber(3,4,4,5,6,4,100));

//---------------------------------------------------

//METHOD 3:
//arrow function

const addNumber = (num1,num2) =>{
    console.log("Hello");
    return num1 + num2;
}

// addNumber();
console.log(addNumber(3,4));
// const addNumber = (num1,num2) =>num1 + num2;
// console.log(addNumber(3,4));

// let arr = [10,11,19,7,50];
// arr.sort((a,b) =>a-b);
// console.log(arr);

//find the square of the number using arrow function
// const square = (num) => num*num;
// console.log(square(5));

// if we have a single paramete, no need of this bracket ()
// const square = num => num*num;
// console.log(square(5));


// const greeting = () =>{
//     return {
//         name :"Aditya",
//         age : 20
//     }
// }
// console.log(greeting());

//In bracket () ke metlb hai ki main is bracket ke andar jo bi pada hai use return kar rha hu

// const greeting = () =>({ name :"Aditya",age : 20})
// console.log(greeting());

// we can also use this bracket in the find square example
// const square = num => (num * num);
// console.log(square(4));

//---------------------------------------------------

// METHOD 3 :- IIFE (immediatly invoke function)
// (function greeting(){
//     console.log("Hello ji");
// })();

// is function ka mtlb hai ()() ye jo second bracket hai ye uus function ko call karega jo phale wale bracket ke andar pada hai

// (() => {
//     console.log("Hello");
// })();

//---------------------------------------------------

// Call Back Function yhape hum kisi ek function kisi dusre function main pass kar sakte hai
// function greet(){
//     console.log("Hello hi !")
// }
// function dance(){
//     console.log("I am dancing");
// }
// function meet(callback){
//     console.log("I am going to meet Someone")
//     // dance(); this is the hardcode hume ise code ko reuseable banana hai
//     callback();
//     console.log("I have finished meeting");
// }
// meet(greet);
// meet(dance)


// Callback function example
// function blinkitOrderPlace(){
//     console.log("We have start packing your Order");
// }
// function zomatoOrderPlace(){
//     console.log("We Have Creating your food");
// }
// function orderPlace(amount , callback){
//      console.log(`${amount} amount is processing`)
//      console.log("Payment Successfully recieved");
//      callback();
// }
// orderPlace(500,zomatoOrderPlace);
// orderPlace(230,blinkitOrderPlace);