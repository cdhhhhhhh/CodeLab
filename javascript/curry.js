let sum = (a, b, c, d) => {
    return a + b + c + d
  }

function curry(fn,...arr){
    let len = fn.length;
    return (...args)=>{
        if(len<=args.length+arr.length){
            return fn(...arr,...args)
        }else{
            return curry(fn,...arr,...args)
        }
    }
}

var sumPlus = curry(sum)
console.log(sumPlus(1)(2)(3)(4));

console.log(sumPlus(1, 2)(3)(4));

console.log(sumPlus(1, 2, 3)(4));


function su2m(a,b,c){
    return  a+b+c
    
}
console.log(su2m.bind(null,1,2)(3));
