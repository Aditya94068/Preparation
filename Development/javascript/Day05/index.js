// In javascript there are some operation :-
// let a = 10;
// let b = 345.6821;
// 1.toFixed(); // Operation
// b.toFixed(4);'b' //jo hai wo immutable hai 
// console.log(b.toFixed(1)); // ya hume ek string return karta hai 
// 2. toPrecision() Operation
// console.log(b.toPrecision(3));//ye function hume string return karta hai per hame kiten number of digit chaiye ye mention karna padta hai
// 3.toString() Operation
// console.log(b.toString());
// console.log(typeof(b.toString()));
// ============================================================================================================================================================
//yha pe second method hoti hai number ko create karne ka
// let a = new Number(20);
// let b = new Number(20);
// let b = a; //is case main true ayega kyu ki hum primitive data copy kar rahe hai.
// console.log(a == b);//is case main false ayega kyu ki a aur b jo hai wo alaga-alag memeory location ko refer kar rhae hai
// solution :- 
// let obj1 = {
//     "name" : "Aditya Vaishnav"
// }
// let obj2 = obj1; // is case main true ayega kyu ki dono object jo hai wo same memeory ko refer kar rahe hai
// console.log(obj2==obj1);
// So most important point ---> Jo hamare primitve data hai usme data copy hota hai aur jo hamare object hai usme reference copy hota hai
// ===================================================================================================================================================================================
// boolean case
// console.log(Boolean({})) // yha pe sirf hamare reference check ho rha hai agar reference hai toh isliye true hai 
// console.log(Boolean({"name" : "Aditya"})) // yha pe sirf hamare reference check ho rha hai agar reference hai toh isliye true hai 
// console.log(Boolean([])) // yha pe sirf hamare reference check ho rha hai agar reference hai toh isliye true hai 
// console.log(Boolean(new Number(0))) // yha pe sirf hamare reference check ho rha hai agar reference hai toh isliye true hai 
// console.log(Boolean(new Number(10))) // yha pe sirf hamare reference check ho rha hai agar reference hai toh isliye true hai 
// console.log(Boolean(null))// Iss case main false hoga
// console.log(Boolean(new Number(null))) // yha pe sirf hamare reference check ho rha hai agar reference hai toh isliye true hai 
// =========================================================================================================================================================================
// Summary:-
// Non Primitive : Reference ke bases pe compare hote hai
// Primitive : Copy by Value
// ex :-
// let a = 10;
// let b = a ;
// console.log (a == b);
// =========================================================================================================================================================================
// Math object and Math Method in javascript
// console.log(Math.E)
// console.log(Math.LN2)
// console.log(Math.PI)
// console.log(Math.LN10)
// console.log(Math.ceil(2.4))
// console.log(Math.floor(2.4))
// console.log(Math.cos(45))
// console.log(Math.log2(45))
// console.log(Math.log10(45))
// console.log(Math.sqrt(81))
// console.log(Math.max(2,3,43,546,652,123,81))
// console.log(Math.min(2,3,43,546,652,123,81))
// console.log(Math.pow(3,2))
// console.log(Math.round(42.77))//43
// console.log(Math.random(1,100))//[0,1) --- >  0 se lekar 1 tak random value generate hogi per 0 included hai per 1 included nhi hai 

//Satebaaji ek game baanate hai:(0-9)
// agar hum chhate hai ki 0 se lekar 9 tak random value mile toh hume Math.random() ko 10 se multiply karna padega
// console.log(Math.random() * 10); 


// agar hame ek single number chaiye mtlb decimal ke baad ek bhi value nhi chaiye toh hame ye karne padega
// console.log(Math.floor(Math.random() * 10));
// agar hume 1 se leakar 10 tak value generate karna hai 
// console.log(Math.floor(Math.random()*10) + 1);
// console.log(Math.floor(Math.random()*10)+1);
// create a range of 1 to 6 for Math.random
// console.log(Math.floor(Math.random() * 6)+1);
// console.log(Math.floor(Math.random()*6) + 1);

// |-------------------------------------------------------|
// |Formula:                                               |
// |Math.floor(Math.random()*totalNumberOfOutComes) + shift|
// |-------------------------------------------------------|

// create a range of 15 to 25 for Math.random
// |-------------------------------------------------------|
// |Formula:                                               |
// |Math.floor(Math.random()*(max - min + 1)) + min        |
// |-------------------------------------------------------|
// console.log(Math.floor(Math.random() *11) + 15);

// console.log(Math.floor(Math.random() *51) + 50);
 
// Generate 4 Digit OTP from 1000 to 9999
// console.log(Math.floor(Math.random()*9000) + 1000);
// Generate 6 Digit OTP From 100000 to 999999
// console.log(Math.floor(Math.random() * 899999)+100000);

// console.log(Math.floor(Math.random() *9000) +1000 );
// console.log(Math.floor(Math.random() * 90000)+10000);