

class Vue{
    constructor(option){
        this.$option = option;
        this.$data = option.data;
        proxy(this,this.$data)
        observe(this,this.$data)
    }
}

class Observer{
    constructor(obj){
        this.obj = obj;
        this.walk(obj)
    }
    walk(obj){
        Object.keys(obj).forEach(function(key){
            defineReactive(obj,key,obj[key])
        })
    }
}
function proxy(vm,obj){
    Object.keys(obj).forEach((key)=>{
        Object.defineProperty(vm,key,{
            get(){
                return obj[key]
            },
            set(newValue){
                obj[key] = newValue
            }
        })

    })
}



function defineReactive(obj,key,value){
    observe(value)
    Object.defineProperty(obj,key,{
        set:function(newValue){
            if(value!==newValue){
            console.log('set '+ key +':'+newValue);
            observe(newValue)
            value = newValue
            }
            return value
        },
        get:function(){
            console.log('get '+ key +':'+value);
            return value
        }
    })
}
function set (obj,key,value){
    defineReactive(obj,key,value)
}

function observe(obj){
    if(typeof obj!=='object'&&obj===null){
        return 
    }    
    new Observer(obj)
}
