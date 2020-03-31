const PENDING = 'PENDING'
const FULFILLED = 'FULFILLED'
const REJECTED = 'REJECTED'
/**
 * 同步
 * 1.先处理promise里面的，成功或者失败
 * 2.进入reslove或者reject，改变状态，添加值，因为没有异步队列为空，
 * 3.进入then，进入相应状态判断中，把当前值给对应的函数
 * 异步
 */

function Promise(handle) {
    let self = this;
    self.value = undefined;
    self.reason = undefined;

    self.status = PENDING;
    self.fulfilled = []
    self.rejected = []

    function reslove(val) {
        if (self.status !== PENDING) return;
        self.status = FULFILLED;
        self.value = val;
        self.fulfilled.forEach(fn => fn())
    }

    function reject(err) {
        if (self.status !== PENDING) return;
        self.status = REJECTED;
        self.reason = err;
        self.rejected.forEach(fn => fn())
    }
    try {
        handle(reslove, reject)
    } catch (error) {
        reject(error)
    }
}


Promise.prototype.then = function (onFulfilled, onRejected) {
    onFulfilled = typeof onFulfilled === 'function' ? onFulfilled : val => val;
    onRejected = typeof onRejected === 'function'?onRejected:err=>{throw err};


    let self = this;
    let promise2 = new Promise((reslove, reject) => {

        if (self.status === FULFILLED) {
            setTimeout(() => {
                try {
                    let x = onFulfilled(self.value)
                    resolvePromise(promise2, x, reslove, reject)
                } catch (error) {
                    reject(error)
                }
            },0);

        } else if (self.status === REJECTED) {
            setTimeout(() => {
                try {
                    let x = onRejected(self.reason)
                    resolvePromise(promise2, x, reslove, reject)
                } catch (error) {
                    reject(error)

                }
            },0)
        } else {

            self.fulfilled.push(() => {
                setTimeout(() => {
               
                    try {
                        let x = onFulfilled(self.value)
                        resolvePromise(promise2, x, reslove, reject)
                    } catch (error) {
                        reject(error)
    
                    }
                },0)
             
            })
            self.rejected.push(() => {
                setTimeout(() => {
                    try {
                        let x = onRejected(self.reason)
                        resolvePromise(promise2, x, reslove, reject)
                    } catch (error) {
                        reject(error)

                    }
                },0)
            })

        }


    })
    return promise2;
}

function resolvePromise(promise2, x, reslove, reject) {
    if (promise2 == x) {
        return reject(new TypeError('类型错误'))
    }
    let called;
    if (x !== null && (typeof x === 'function' || typeof x === 'object')) {
        try {
            let then = x.then;
            if (typeof then === 'function') {
                then.call(x,(y)=>{
                    if(called) return;
                    called = true;
                    resolvePromise(x,y,reslove,reject)
                },(err)=>{
                    if(called) return;
                    called = true;
                    reject(err)
                })
            } else {
                reslove(x)
            }
        } catch (error) {
            if(called) return;
            called = true;
            reject(error)
        }
    } else {
        reslove(x)
    }
}
Promise.defer = Promise.deferred = function(){
    let dfd = {};
    dfd.promise = new Promise((resolve, reject)=>{
        dfd.resolve = resolve;
        dfd.reject = reject;
    });
    return dfd;
}
Promise.prototype.catch = function(errFn){
    return this.then(null,errFn);
}


Promise.prototype.finally = function(fn){
    this.then(()=>{
        fn();
    },()=>{
        fn();
    });
    return this;
}
/** 1 直接在构造函数上增加all方法
 *  它返回的也是一个Promise
 *  等待参数数组中所有的promise都执行完毕后
 *  再返回结果
 */
Promise.all = function(values){
    return new Promise((resolve,reject)=>{
        /** 2 定义一个存放最终结果的数组result和一个index */ 
        let results = [];
        let index = 0;
        /** 3 定义一个方法addToArr()  
         *  让index每次执行增加results数组元素的函数的时候都+1
         *  当index === values的长度的时候 说明此时所有promsie都执行完毕并放到的数组中
         *  然后直接resolve(results)就行了
        */
        function addToArr(key,value){
            index++;
            results[key] = value;
            /** 6 当满足条件时 说明所有的promise都执行完毕 直接resolve(results) */
            if(index === values.length){
                resolve(results);
            }
        }
        /** 4 循环values中的每一项promsie */
        for(let i = 0; i < values.length; i++){
            let current = values[i];
            /** 5 判断每一项promise的返回值是不是一个Promsie
             *  是的话就执行该Promise的then方法 拿到返回值 并放到数组results中
             *  是一个普通值的话就直接将该值放到数组results中
             */
            if(current && current.then && typeof current.then === 'function'){
                current.then((value)=>{
                    /** 同5 把返回值放到数组results中*/
                    addToArr(i,value);
                },reject);
            }else{
                /** 同5 把返回值放到数组results中*/
                addToArr(i,current);
            }
        }
    });
}

/** race方法相比较于all方法简单很多
 *  因为race中的promsie成功resolve一个 
 *  整个race就resolve */
Promise.race = function(values){
    return new Promise((resolve,reject)=>{
        /** 同4 */
        for(let i = 0; i < values.length; i++){
            let current = values[i];
            /** 同5 */
            if(current&&current.then&&typeof current.then === 'function'){
                /** 7 直接执行then就好 */
                current.then(resolve,reject);
            }else{
                /** 8 普通值直接resolve */
                resolve(current);
            }
        }
    });
}

// resolve方法
Promise.resolve = function(value){
    return new Promise((resolve,reject)=>{
        resolve(value);
    });
}
// reject方法
Promise.reject = function(reason){
    return new Promise((resolve,reject)=>{
        reject(reason);
    });
}
module.exports = Promise;