Buffer.prototype.split = function (bar) {
    let arr = [];

    let cur = 0;

    let n;

    while ((n = bar.indexOf('---')) !== -1) {
        arr.push(bar.slice(cur, n));
        bar = bar.slice(n + 3)
    }
    arr.push(bar.slice(cur, n));
    return arr
}
