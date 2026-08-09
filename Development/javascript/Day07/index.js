// let marks = [100,40,70,80,20];//Array ko bnane ka tarika
// console.log(marks);// Array ko print karna 

// // Array jo hai wo haterogeneous hota hai mtlb ya apne andar kisi bhi type ka data store kar sakta hai
// let  arr = [100,30,"Aditya",true];
// console.log(arr);
// Array ko Access karna hai index ka use hota hai
// console.log(arr[2]);
// Changing data in array , array mutuable hote hai
// arr[1] = 70;
// console.log(arr);

// Array ke andar agar kisi data ko dalna hai toh push operation use hota hai
// arr.push(50);// Ya array ke at last main element ko add karta hai
// console.log(arr);

// //Array ke andar hum data ko delete karne ke liye hum pop operation ka use karte hai
// arr.pop();// Ya array ke at last element ko delete karta hai
// console.log(arr);

// Array ke at first mtlb start index ke pe agar hum element ko dalna hai toh hum --> .unshift() operation ka use karte hai
// arr.unshift(400);
// console.log(arr);

// Array ke at index one / Firt pe element ko delete karne ke liye hym is operation ka use karte hai--> .shift() operation ka use karte hai
// let  arr = [100,30,"Aditya",true];
// arr.shift();
// console.log(arr);

// for loop on array
// let arr = [10,20,30,50,90,11];
// for(let i = 0;i<arr.length;i++)
// {
//     console.log(arr[i]);
// }

// for of loop --> for of loop jo hai wo c++ ke for each loop ki tarah hai
// let arr = [10,20,30,50,90,11];
// for(let num of arr){
//     console.log(num);
// }

// Copying array :- array copy by reference hota hai
// let arr = [10,20,30,50,90,11]; 
// let arr2 = arr;
// arr2.push(300);
// console.log(arr);//Yhape  non-primitive datatype pass by reference hota hai isliye arr2 main jo change hua whi change reflect hua arr ke andar bhi

// const arr = [10,20,30,40,50];
// arr = [80,40,20];
// console.log(arr);//yhape error ayega kyu ki array ke andar kke address chane nhi hote hai constant (const) keyword ke karan "const".

// Object (non-primitive) : copy by reference hote hai
// primitive:copy by value hote hai

// Slicing
// const arr = [10,30,50,90,11];
// const arr2 = arr.slice(2,4);
// console.log(arr2);
// console.log(arr);//yhape original array ke andar koi bhi change nhi hoga

// Splicing array :- mere original array main se agar mujhe koi part trim karna hai to ye karna padta hai
// const arr = [10,30,50,90 , 11];
// const arr2 = arr.slice(2,4);
// console.log(arr);//[10,30,50,90,11]
// const arr3 = arr.splice(1,3);//output :[30,50,90]
// console.log(arr);

// const arr3 = arr.splice(1,3,"Rohit",19);//is line ka mtlb hai ki original array main se (30,50,90) ko hta do aur baaki ka "Rohit",19,ko index wise set kar do
// console.log(arr);
// console.log(arr3);

// Merging array with Spread Operator(...)
// const arr =[10,30,50,90,11];
// const arr2 = ["Rohit",11,true];
// const arr4 =[9,4,false];
// arr.push(arr2,arr4);
// const arr3 = arr.concat(arr2,arr4);
// console.log(arr3);
// const arr3 = [arr,arr2,arr4];
// console.log(arr3);
// const arr3 = [...arr,...arr2,...arr4];
// console.log(arr3);

// convert array to string
// const names = ["Alice","Bob","Charlie"];
// console.log(names.toString());
// console.log(names.join("-"));

// Searching index of particular item
// const names = ["Alice","Bob","Charlie","Bob"];
// console.log(names.indexOf("Bob"));
// console.log(names.lastIndexOf("Bob"));
// console.log(names.includes("Bob"))//true ya false ayga agar element exist karta hai karta hai toh true otherwise false

// Sorting array of string
// const names = ["Alice","Rohit","Bob","Mohit","Charli",];
// names.sort();//yhape ASCII Value ke hisab se string array sort hoga
// console.log(names);

// // Reversing array
// names.reverse();
// console.log(names);

// Reverse Sorting -->in dono function ka use karke hum ascending ya descending main sort kar sakte hai
// names.sort();
// names.reverse()
// console.log(names);


// Numbers ke case main
// const a = [101,90,80,32,91];
// a.sort();
// console.log(a);//yhape ASCII table ke hisab se array sort ho rha hai , aisa isliye kyu ki array ke andar saare element chahe wo number ho ya string ho unhe as a string consider kiya jata hai
// So number ko sort karne ke liye hum is method ka use karte hai
// Ascending order main sort karne ka logic
// const arr = [10,40,31,71,5,11];
// arr.sort((a,b) => a-b);
// console.log(arr);

// Descending order main sort karne ka logic
// arr.sort((a,b) => b-a);
// console.log(arr);

// array ke andar ke array ke element ko  access karne ka logic
// const arr = [10,30,50,[40,90,[60,19,99],11],80];
// console.log(arr[3][2][1]);

// flat function -->flat ke andar level hoti hai ki bydefault 1 level ke array ko flat karunga ya aur uske andar ke element ke liye hum level set kar sakte hai
// const a = arr.flat(2);
// console.log(a);
// hum flat ke sath infinite bhi use kar sakte hai
// const a = arr.flat(Infinity);
// console.log(a);

// Arrray ko hum is tarah se bhi access kar sakte hai jisme hum index ko as a charachter use kar sakte hai
// const a = [10,300,"Rohit",903,true];
// console.log(a["1"]);

// a.name = "Mohan";
// // console.log(a);

