// Operator 
// 1.Arithmetic operator
// Eg :-
// console.log(2 + 5);
// console.log(2 - 5);
// console.log(2 * 5);
// console.log(6 / 3);
// console.log(5 % 2);
// exponentiation
// console.log(5 ** 3); // 5 * 5 * 5 = 125

// 2.Assignment operator
// let x = 20;
// let y = 10;
// x = x + y;
// x = x - y;
// x += y;
// x -= y;
// x /= y;
// console.log(x);

// 3. Comparison operator
// let x = 20;
// let y = 10;
// console.log(x > y); // true
// console.log(x < y); // false;
// console.log(x<=y);//false;
// console.log(x>=y);//true;
// console.log(x==y);//false;
// console.log(x === y);//false -->(Is check ko hum strict check khate hai)phale type check hoga (agar dono same type ke honge toh uske baad wo comparison hoga)

//number and string ko compare karte time string convert ho jati hai number.
//type casting
// let z = '10';
// let a = Number(z);
// console.log(typeof a);


// NaN: Not a number (Type of it is number)
// let a = "121ac";
// let b = Number(a);
// console.log(typeof b);

//Convert number to string

// let a = 10;
// let b = String(a);
// console.log(typeof b,b);

// convert boolean in number
// console.log(Number(true)) // true --> 1
// console.log(Number(false)) // false --> 0
// console.log(Number(null)) // null --> 0
// console.log(Number(undefined)) // undefined --> NaN

// console.log(String(true));
// console.log(String(false));
// console.log(String(undefined));
// console.log(String(null));

// console.log(Boolean(10));// 10 aur -10 jo bhi existing number hai us case main true ayega
// console.log(Boolean(0));// Zero ke case main false dega
// console.log(Boolean("Hello World"));// jo bhi existing string hogi us case main true mark hoga
// console.log(Boolean("")); // jo bhi empty string hogi uss case main false hoga
// console.log(Boolean(null));// null ke case maain bhi false hoga
// console.log(Boolean(undefined));//undefined ke case main bhi false hoga

// computer science challenge
// let a = 0.1;
// let b = 0.2;
// let c = a + b;
// console.log(Number(c.toFixed(1))); 
// console.log(c);

// Rules in javascript
// 1 : null is looosely equal to undefined only

// console.log(null == undefined);
// console.log(null === undefined);
// console.log(null == 0);
// console.log(null == "");
// console.log(null == false);
// console.log(null == true);

//2 : >,<,>=,<= (null --> number  undefined --> NaN)

// console.log(null >= 0);
// console.log(null<=0);
// console.log(null>0);
// console.log(null<0);
// console.log(null >= undefined);
// console.log(undefined >= 0);

// console.log("Rohit" > "Mohit") // ASCII value ke through compare hoga 
// console.log(10 <= true);
// console.log(1 == true); // is case main true ayga kyu ki 1 jo hai wo equal hota hai true ke
// Ek koi bhi type hai, usko agar muje compare karna hai dusre kisi type se 
// dono number main convert honge

// console.log(null>="");
// console.log(NaN ==NaN);

// for loop
// post increment :i++
// for(let i = 0;i<10;i++){
//     console.log(i);
// }
// post decrement :i--
// for(let i = 10 ; i>=0;i--){
//     console.log(i);
// }


//while loop

// let i = 0;
// while (i < 10){
//     console.log(i);
//     i++;
// }

// i = 0;
// do{
//     console.log(i);
//     i++;
// }while(i<10);

// if else condition

// let age = 15;
// if(age >= 18){
//     console.log("Eligible for vote");
// }
// else{
//     console.log("Not Eligible for vote")
// }

// kid young and old
// let age = 20;
// if(age < 18){
//     console.log("You are kid !");
// }
// else if(age >= 60){
//     console.log("You are old");
// }
// else{
//     console.log("You are Young");
// }

// logical operator
//&&,||
// console.log(true && true);
// console.log(true && false);
// console.log(false && true);
// console.log(false && false);


// console.log(true || true);
// console.log(true || false);
// console.log(false || true);
// console.log(false || false);

// Logical &&
// let a = "Rohit";
// let b = "Mohit";
// let c = a && b;
// console.log(c);

// let a = 0;
// let b = 20;
// console.log(a && b);
// && : If first value is false,it will return the first value itself
// If first value is true , it will return the second value itself

// || Logical OR

// let a = 10;
// let b = 20;
// console.log(a || b);
// || : If first value is true,it will return the first value itself
// If first value is false , it will return the second value itself

// != Not equal
// console.log(3!=5);
// console.log(5 | 2);
// console.log(5 & 2);


console.log(2===2);