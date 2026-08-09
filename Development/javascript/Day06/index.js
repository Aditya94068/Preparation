//string
// const str1 ="Aditya";
// const str2 = "Aditya Vaishnav";
// const str3 =  `Strike 
// is
// comming
// soon`;//Ye tarika bhot extensibly use kiya jata hai.
// const day = 18;
// const str3 =  `Strike is comming soon ${day}`;// agar hume ye day ki jo value hai ise agar hume es string ke andar ya sath print krna hai to hume ye sign use karna padega ${variable_name}
// console.log(str3);
// let day = 23;
// console.log(`My College is started ${day} year`)


// const str = "Aditya Vaishnav";
// console.log(str.length);
// str[3] = "T";//string jo hai wo immutable hoti hai 
// console.log(str);
// console.log(str[0]);
// const a = str.toUpperCase();//yha pe hamri string uppar case main bikul new string convert hui aur use humne ek new variable 'a' ke andar store kiya hai isse original string ke andar koi change nhi hoga
// console.log(a);
// console.log(str.toLowerCase());

// const str = `Hello Coder Army`;
// console.log(str.length)
// console.log(str.indexOf("Cod"));
// console.log(str.lastIndexOf("Cod"));//ye piche se hamari sub string ka index count karke return karega
// console.log(str.includes("Cod"));//ye search karega ki hamara sub string , string ke andar present hai ya nhi agar hai toh true otherwise false

// slicing
// positive slicing
// console.log(str.slice(2,7));//slicing main hum (.slice(start , stop)) dete hai per stop include nhi hota hai mtlb 7 include nhi hota hai
// console.log(str.slice(3)); //yha pe 3 aur 3 ke baad saare element slice ho jayenge
//negative slicing
// console.log(str.slice(-13,-1));//yha pe -4 ka mtlb hai string ke piche se string ko slice karna start karo.aur yha pe -1 included nhi hoga

// Substring --> agar kisi string main se particular part chaiye ho 
// const str = `Hello Coder Army`;
// console.log(str.substring(2,8));

// Concatenation of string 
// let a = "Aditya";
// let b = "Vaishnav";
// let c = a+" "+b;
// console.log(c);
// console.log(24+"aditya");
// console.log(24+"aditya" + 10);
// console.log(24 + 45+"aditya" + 10);

//Replace
// const str = `Hello Coder Army  Coder`;
// console.log(str.replace('Cod','Iam'))//agar hame kisi ek ko karna hai replace jha pe hame first time "Cod" milega
// console.log(str.replaceAll('Cod','Iam'))//agar hame ek se jayaga baar kisi jagah per "Cod" mil jata hai wha pe replaceAll kaam ata hai

//trim
// const username = "   Aditya    vaishnav ";
// console.log(username);
// console.log(username.trim() );
// console.log(username.trimStart());
// console.log(username.trimEnd());

//split
// const name = "Aditya@sumit@sunil@nita"; 
// console.log(name.split('@'));// ye ek list generate  kare ke deta 

//Getting the current date and time and UTC (universal time coordinates)
// const now = new Date();
// console.log(now);
// console.log(now.toString());//javascript ye time and date hamare system main se utha rha hai
// console.log(now.toISOString());
// console.log(now.toLocaleString());

//local time wal data dikhayga
// console.log(now.getDay());//yha pe// Mon ->1,
                                  // tue->2,
                                  // wed->3,
                                  // thu->4,
                                  // fri->5,
                                  // sat->6,
                                  // sun->7
// console.log(now.getDate());//yha pe Mon ->1,tue->2,wed->3,thu->4,fri->5,sat->6,sun->7
// console.log(now.getFullYear());
// console.log(now.getHours());
// console.log(now.getMilliseconds());
// console.log(now.getMinutes());
// console.log(now.getMonth());
                           //jan->0,
                           // feb->1,
                           // mar->2,
                           // apr->3,
                           // may->4,
                           // jun->5,
                           // jul->6,
                           // aug->7,
                           // sep->8,
                           // oct->9,
                           // nov->10,
                           // dec->11
// console.log(now.getTime());
// console.log(now.getSeconds());


//Year month date hour minute second milisecond
// const now = new Date(2025,8,20,8,25,16,124);
// const now = new Date(2005,1,16,11,37,12,123);
// console.log(now.toString());



// const now = Date.now();
// 1761494016589
// const date = new Date(1761494016589) // this is the milisecond which is currently running in our system 
// console.log(date.toString(1761494016589)); 
// 1761494016589 this is the timestamp aur ye har jagha same hota hai

// const date = new Date(0);
// console.log(date.toString());

// const date = new Date(245535282728);
// console.log(date.toString(date));

// const now = Date.now();
// const date = new Date(-12546431123);//negative value dena se hum UTC ki help se kei saal piche ja sakte hai 
// console.log(date);
//UTC Wala time pass hota hai server ko means For example India UTC Wale time se 5 gahante aage chal rha hai

// Browse automaticially handle karta hai bass hume ispe jana hai --> browser --> inspect --> console --> put UTC second