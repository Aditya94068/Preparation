// object 
// Object jo hai wo key value pair main data ko store karta hai
//Object creation
//Object ke andar hum CRUD (Create read update delete) operation bhi perform kar sakte hai


//Create Operation
const user = {
    name : "Aditya",
    age : 20,
    emailId : "Aditya@gamil.com",
    amount : 340000,
    "home address" :"khandwa"
}

//Read Operation
// console.log(user["home address"]);
// console.log(user["name"]);//behind the scene name jo hai woh as a string hi store kar rha hai
// console.log(user);//print the object
// console.log(typeof user);//print the object type


//Read operation
//Accessing the particular value
// console.log(user.age);
// console.log(user.amount);

// update operation 
//storing the value or inserting the value
// user.aadhar = 435252155252;
// console.log(user);

//Updating the value of ammount 
//update operation
// user.amount = 5000;
// console.log(user);

//  Delete Operation 
// delete emailid from this example
// delete user.emailId;
// console.log(user);


// const user = {
//     name : "Aditya",
//     age : 20,
//     emailId : "Aditya@gamil.com",
//     amount : 340000,

// }
// const user2 = user;
// user2.age = 43;
// console.log(user); // yhape ye horha hai ki user2 jo hai wo ek hi object ko point kar rahe hai

//print only keys
// console.log(Object.keys(user));//ye jo object hai ek array create karega aur phir uske andar saari keys ko rakh dega

// console.log(Object.values(user));//yha pe bhi same object hai ek array create karega aur phir uske andar saari values ko rakh dega

// console.log(Object.entries(user));//yha pe bhi ye hoga ki jitni bhi key values hai wo print hogi 

//loop on object -->1."for in"loop use kiya hai yha pe 
// for(let keys in user){
//     console.log(keys,user[keys]);//yhape hum user.keys nhi use kar sakte hai kyu ki user.key jo hai wo keys ko dhundta hai agar hume values print karni hai keys ke sath toh iss tarah se likhna padega
// }

// 2.for of loop hum sirf array ke upar lga sakte hai per direct object ke upar lagana is not possible
// const temparr = Object.keys(user); 
// console.log(temparr)//yhape object jo hai wo hame keys ka array return karta hai toh hum kya karnege ki uske andar direct array create hone ke baad for of loop lga denge
// for(let keys of temparr){
//     console.log(keys);
// }

// //values ke liye for of loop
// for(let values of Object.values(user)){//yhape object jo hai wo hame values ka array return karta hai toh hum kya karnege ki uske andar direct array create hone ke baad for of loop lga denge
//     console.log(values);
// }

// // //entries ke liye for loop
// for(let entries of Object.entries(user)){//yhape object jo hai wo hame entries ka array return karta hai toh hum kya karnege ki uske andar direct array create hone ke baad for of loop lga denge
//     console.log(entries);
// }

// const user = {
//     name : "Aditya",
//     age : 20,
//     emailId : "Aditya@gamil.com",
//     amount : 340000,
// }

// const name = user.name;
// const age = user.age;
// console.log(name,age);

// Hum is technique ko bhot kaam use karte hai toh hum kya karenge iss object ki destructuring kar denge do values ko nikalne ke liye


const {name , age,amount} = user;//iss technique ka hum bhot jayada use karenge jab hume object mai destructring karni hogi
console.log(name,age,amount);

// Array ki destructuring
// const arr = [10,20,30,40,50,60];
// const [first,second,third] = arr;
// console.log(first,second,third);

// const {name:username , age:userage} = user; // koi dusre naam ka use kar ke bhi hum destructring kar sakte hai
// console.log(username,userage);



//agar humare pass object hai toh iska andar hum function bhi create kar sakte hai jinko hum methods bolte hai
// const user = {
//     name : "Aditya",
//     age : 20,
//     emailId : "Aditya@gamil.com",
//     amount : 340000,
//     greeting : function(){
//         // console.log("Strike is comming on 18 october");
//         console.log(`Strike is comming on 18 october ${this.name}`);//accessing the value from the object "this" jo hai wo ussi same fuction ko refer karta hai jisne isko call kiya tha this keyword usko refer karta hai jisne aapko call kiya hai
//         // console.log(`Strike is comming on 18 october ${user.name}`);//accessing the value from the object
//         return 20;//value bhi return bhi kar sakta hai
//     }
// }
// //calling the function in the user 
// user.greeting();
//return value ko store kar ke print karne ke liye hum kuch iss tarah se karte hai

// const user2 = {
//     name : "sumit",
//     account : 20004,
// }
// user2.greeting = user.greeting;
// user2.greeting();
// const value = user.greeting();
// console.log(value);


//nested object --> object ke andar object
// const user = {
//     name : "Aditya",
//     age : 20,
//     emailId : "Aditya@gamil.com",
//     amount : 340000,
//     address :{
//         city : "kotdwar",
//         state :"Utterkhand"
//     }
// }
// console.log(user);
// console.log(user.address);
// console.log(user.address.city);

// object ki copy agar hume create karni hai toh hum spread operator ka use karte hai(...)


// shallow copy
// const user2 = {...user};
// // user2.name = "Mohan";
// user2.address.city = "Dwarka";//yhape ye wali line jo hai wo user main bhi change karigi kyu ki spread operator jo hai ek level tak hi object ko copy karta hai
// console.log(user2);
// console.log(user);

//deep copy 
// const user2 = structuredClone(user);//structuredClone jo hai wo is problem ko sahi kar deta hai jo hum upar face kar rahe hai
// user.address.city = "Dwarka";
// console.log(user);
// console.log(user2);

//key ko hum as a number ke form main bhi le sakte hai
// const user = {
//     name : "Rohit",
//     age : 20,
//     0 : 100,
//     2 : "Mohan"
// }
// console.log(user[2]);

// Behind the scene array like this
// const arr = [10,20,30,40] 
// {
//     0 :10,
//     1 :20,
//     2 :30,
//     3 :40

// }