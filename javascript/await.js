const getData = () => new Promise(resolve => setTimeout(() => resolve("data"), 1000))

function* test() {
    const data = yield getData()
    console.log('data: ', data);
    const data2 = yield getData()
    console.log('data2: ', data2);
    return 'success'
}

function autoGenerator(genFun) {
    return new Promise((resolve, reject) => {
        let result;
        const gen = genFun.apply(this, arguments)

        function step(fun, arg) {
            try {
                result = gen[fun](arg)
            } catch (error) {
                reject(error)
            }
            if (result.done) {
                resolve(result.value)
            } else {
                return Promise.resolve(result.value).then((res) => step('next', res), err => next('throwe', err))

            }
        }
        step('next')
    })

}
autoGenerator(test).then(res=>console.log(res))