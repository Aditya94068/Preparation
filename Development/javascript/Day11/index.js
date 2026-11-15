const arr = [2,4,6,8]
sum = 0;
arr.forEach((number) =>{
    sum +=number
    console.log(number)
}
)
console.log(sum)

const fruits = ["Apple", "Banana", "Mango", "Orange"];

fruits.forEach((value) => {
    console.log(value)
})

arr.forEach((number)=>{
    console.log(number**2)
})

fruits.forEach((f) =>{

    console.log("greeting",f)
})

arr.forEach((value) =>{
    if(value % 2 == 0)
    {
        console.log(value)
    }
})