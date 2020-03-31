let throttle = function(fn, delay, atleast){
    let timer;
    let previous;
    return function(){
        let now = Date.now()
       !previous&& (previous = now)
        if(now - previous>atleast){
            fn();
            previous = now;
        }else{
            clearTimeout(timer)
            timer = setTimeout(()=>{
                fn();
            },delay)
        }
    }
}


const throttle = function(func, wait, options){

        let context,args,result;
        let timeout = null;
        let previous = 0;
        !options&&(options={})
        let laster = ()=>{
            setTimeout(() => {
                result = func.apply(context,args)
                if(!timeout) context=args=null
            }, wait);
        }
        return function(){
            if (!previous && options.leading === false) previous = now;
            var remaining = wait - (now - previous);
            context = this;
            args = arguments;
        
        }
}


