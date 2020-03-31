const debounce = (fun, wait = 50) => {
    let timer = null;
    return function (...args) {
        timer && clearTimeout(timer)
        timer = setTimeout(() => {
            fun.apply(this, args)
        }, wait)
    }
}



const debounce = (fun, wait = 50, immediate) => {
    let context, args, timer;
    let lastr = () => setTimeout(() => {
        if (!immediate) {
            fun.apply(context, args)
            context = args = null
        }
    }, wait)

    return function (...params) {
        if (!timer) {
            timer = lastr();
            if (immediate) {
                fun.apply(this, params)

            } else {
                context = this;
                args = params
            }
        } else {
            clearTimeout(timer)
            timer = lastr();
        }
    }
}