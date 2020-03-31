function deepClone(obj) {
    let copy = obj instanceof Array ? [] : {}

    for (i in obj) {
        if (obj.hasOwnProperty(i)) {
            copy[i] = typeof obj[i] === 'object' ? deepClone(obj[i]) : obj[i]
        }
    }
    return copy;
}

function vuexDeepCopy(obj, cache = []) {
    if (obj === null && typeof obj !== 'object') {
        return obj;
    }

    const hit = cache.filter(c => c.original === obj)[0]
    if (hit) {
        return hit.copy;
    }
    const copy = Array.isArray(obj) ? [] : {}
    cache.push({
        original: obj,
        copy
    })

    Object.keys(obj).forEach(key => {
        copy[key] = vuexDeepCopy(obj[key], cache)
    })
    return copy;
}