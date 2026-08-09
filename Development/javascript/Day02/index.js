// variable ko kaise banate hai
// method I
// let name = "Aditya"; // let keyword use hota hai variable ko declare karne ke liye 
// console.log(name); //console.log() is used hota hai variable ko print karne ke liye
// let a = 5;
// console.log(a);
// a = 45;
// console.log(a);
// let age = 20;
// age = 30; // let keyword ki value change ho sakti hai
// console.log(name,age);

// let age = 20;
// let name = "Aditya Vaishnav";
// console.log(age,name);

// method II
// const account = 1234;//const keyword bhi use hota hai variable ko declare karne ke liye per iski value change nhi hoti hai
// console.log(account);



// method III
// var a = 10;
// console.log(a)


// DataTypes kya hote hai

// primitive datatype
// number,string,boolean,undefined,null,bigint,symbol


// non primitive datatype
// array,object,function


// primitive datatype

// number
// let a = 10;
// let b = 2.36;
// console.log(a,b);
// console.log(typeof a);

// let a = 20;
// let b = 20.2;
// console.log(typeof(b));
// -------------------------------------------------------------------------------------------------------------------------------------------------------

// string
// let c = "Strike is coming";
// let d = "Aditya";
// console.log(c,d);
// console.log(typeof d);
// let name = "Aditya vaishnav"
// console.log(name)
// console.log(typeof(name));
// --------------------------------------------------------------------------------------------------------------------------------------------------
//boolean -> give true/false
// let login = true;
// let f = false;
// console.log(login,false);
// console.log(typeof f);
// console.log(typeof(true))
// ------------------------------------------------------------------------------------------------------------------------------------------
//undefined -> Abhi is varible ko koi bhi value assign nhi hui hai
// let user;
// console.log(user);
// let user;
// console.log(user);
// -------------------------------------------------------------------------------------------------------------------------------------
//bigint -> iska use hot a hai big number ko store karne ke liye
// let num = 239452535892472498542n;
// console.log(num);
// -----------------------------------------------------------------------------------------------------------------------------------------------
//null -> Null ka mtlb hota hai ki main is variable ke andar kuch nhi dalna chahata Hum yha pe khud value store nhi karna chahate hai
// null ke andar ek bug hai iska type null nhi balki object dikhata hai
// let weather = null;
// console.log(weather);
// ------------------------------------------------------------------------------------------------------------------------
//Symbol
// const id1 = Symbol("id");
// console.log(id1);
// ------------------------------------------------------------------------------------------------------------------

//non primitive datatype

//Array
// let arr =[10,20,11,"Aditya",true];
// console.log(arr);

// let array = [10,20,30,40,50,"ADITYA VAISHNV",true,20.2];
// console.log(array);
// -------------------------------------------------------------------------------------------------------------
//object -> ye key value pair main store hote hai
// let obj = {
//     // key : value
//     name : "Aditya",
//     account : 12312,
//     age:18,
//     category : 'gen'
// }
// console.log(obj);

// object ke andar agar ek value axis karni hai to hum (.) operator ka use karte hai
// console.log(obj.name)
// let data = {
//     "name" : "Aditya",
//     "Age" : 20,
//     "college" : "Sandip University",
//     "Department" : "BTECH",
//      Branch : {
//          "ENGIERRING" :["CSE", "CIVIL","ELECTRICAL","AEROSPACE"]
//     }
// }
// console.log(data);
// ----------------------------------------------------------------------------------------------
//function
// function add(){
//     console.log("hello");    
// }
// add();



// javascript ke anadar hum function ko kisi bhi variable ke andar store kara sakte hai
// EX:-
// let s = function add(){
//     console.log("Hello");
// }
// console.log(s);
// for call that fuction we use this syntax
// s();
// console.log(s());

// let sum = function add(x , y){
    // console.log(x + y);
//     return x + y;
// }
// // add(4 , 5);
// console.log(sum(4,5));

// let sum = function add(a , b){
//     return a + b;
// }
// console.log(sum(4,5));
// ----------------------------------------------------------------------------------------------------
// primitive datatype immutable hote hai 
// let a = 10 ;// iska mtlb hai ki ek a name ki memory bani jiske andar 10 hai 
// a = 20; // or iska mtlb hai ki ek memory hai jisme 20 hai aur uska naam a  hai mtlb humne 'a' ki value change nhi kari hai bass humne ek value li aur memeory ki andar aur usko a ko assign kar diya hai 
// console.log(a);

// same jise string ke sath bhi hoti hai
// let str = "Aditya";
// str = "Vaishnav";
// console.log(str);

// proof
// let str = "Aditya";
// str[0] = 'a'; // yha pe hum string ke 1st index ko change nhi kar sakte means A change nhi ho sakta hai small a ke andar
// console.log(str);
// -----------------------------------------------------------------------------------------------------------------------
// non - primitve datatype mutable hai
// let arr = [10,20,30,40,50,60];
// arr[0] = 100; // yha pe hum dekh sakte hai ki arr[0] = 100 hai mtlb hum array ke andar data  ko change kar sakte hai
// arr[6] = 70;
// console.log(arr);
// -------------------------------------------------------------------------------------------------------------------
// object bhi mutable hote hai
// object , array etc ye sab jo hai immutable hote hoi aur inke karan koi bhi extra copy create nhi hoti hai ye sab memory ke location ko hi point karte hai
// hamesha value pass by reference hi hoti hai non-primitve datatype ke andar
// let obj = {
//     'name':'Aditya',
//     'age': 20
// }
// obj2 = obj
// obj2.name='vaishnav';
// console.log(obj);