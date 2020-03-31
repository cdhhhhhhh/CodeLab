Function.prototype.myBind = function (context) {
	if (typeof this ==='Function') {
		throw TypeError('Error')
	}
	let _this = this;
	let arg = [...arguments].slice(1)
	return function F(){
		if (this instanceof F ) {
			return new _this(...arg,...arguments)
		}
		return _this.apply(context,arg.concat(...arguments) )
	};
}