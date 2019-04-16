function isArray() {

    this.fun1 = function (arr) {
        return '[object Array]' === Object.prototype.toString.call(arr)
    };

    this.fun2 = function (arr) {
        return Array.isArray(arr)
    };
    //因为数组为引用型 所以在其他的框架地址可能改变
    this.fun3 = function (arr) {
        return arr instanceof Array
    }

}

function isFunction() {

    this.fun1 = function (fn) {
        return '[object Function]' === Object.prototype.toString.call(fn)
    };

    this.fun2 = function (fn) {
        return fn instanceof Function
    }

}

function isPlain(obj) {
    //初始化对象
    if (Object.prototype.toString.call(obj) !== '[object Object]' || !('isPrototypeOf' in obj)) {
        return false
    }

    if (obj.constructor &&
        !Object.prototype.hasOwnProperty.call(obj, 'constructor') &&
        !Object.prototype.hasOwnProperty.call(obj.constructor.prototype, 'isPrototypeOf')
    ) {
        return false
    }
    for (key in obj) {
    }
    return key === undefined || hasOwnProperty.call(obj, key);
}

function cloneObject(obj) {
    let result, i, len
    if (!obj
        || obj instanceof Number
        || obj instanceof String
        || obj instanceof Boolean) {
        return result;
    }
    if (isArray(obj)) {
        result = []
        let resultLen = 0;
        for (i = 0, len = obj.length; i < len; i++) {
            result[resultLen++] = cloneObject(obj[i])
        }
    }
    if (isPlain(obj)) {
        result = {}
        for (i in obj) {
            if (obj.hasOwnProperty(i)) {
                result[i] = cloneObject(obj[i])
            }
        }
    }
    return result
}

let srcObj = {
    a: 1,
    b: {
        b1: ["hello", "hi"],
        b2: "JavaScript"
    }
};

function uniqArray(arr){
    this.fun1 = function (arr) {
        return new Set(arr)
    }
    this.fun2 = function (arr) {
        let len = arr.length,
            result = arr.slice(0),
            i,datum;

        while (--len > 0){
            datum = result[len]
            i = len
            while (i--){
                if (datum === result[i]){
                    result.splice(len,1)
                    console.log(result)
                    break
                }
            }
        }
        return result;
    }
    this.fun3 = function (arr) {
        let obj = {}
        let result = []
        for (let i = 0;i<arr.length;i++) {
            if (!obj[arr[i]]) {
                result.push(arr[i])
                obj[arr[i]] = true
            }
        }
        return result
    }
    this.fun4 = function (arr) {
        let obj = {}
        for (let i = 0;i<arr.length;i++){
            obj[arr[i]] = true
        }
        return Object.keys(obj)
    }
}
var a = [1, 3, 5,5, 7,6, 5, 3];
test = new uniqArray()
console.log(test.fun4(a))
