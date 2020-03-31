function New(func){
    if(typeof func!=='function'){
        throw TypeError('type err')
    }

    let  res = {}

    func.apply(res,[...arguments])
    return res;
}