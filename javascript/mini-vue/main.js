let watchers = [];

let arrPrototype = Array.prototype;
let orginPrototype = Object.create(arrPrototype);
["push"].forEach((method) => {
    orginPrototype[method].apply(this);
});
function set(obj, key, value) {
    defineReactive(obj, key, value);
}

function observe(obj) {
    if (typeof obj !== "object" && obj === null) {
        return;
    }
    new Observer(obj);
}

class Vue {
    constructor(option) {
        this.$option = option;
        this.$data = option.data;
        this.$el = option.el;
        //代理元素
        proxy(this, this.$data);
        proxy(this, this.$option.methods);

        //设置响应式
        observe(this.$data);
        //编译元素
        new Compile(this.$el, this);
    }
}

class Observer {
    constructor(obj) {
        this.obj = obj;
        this.walk(this.obj);
    }
    walk(obj) {
        if(Array.isArray(obj)){
            obj.__proto__ = orginPrototype;
            Object.keys(obj).forEach(function (key) {
                observe(obj[key]);

            });
        }else{
            Object.keys(obj).forEach(function (key) {
                defineReactive(obj, key, obj[key]);
            });
        }
    }
}
function proxy(vm, obj) {
    Object.keys(obj).forEach((key) => {
        Object.defineProperty(vm, key, {
            get() {
                return obj[key];
            },
            set(newValue) {
                obj[key] = newValue;
            },
        });
    });
}

function defineReactive(obj, key, value) {
    const dep = new Dep();
    observe(value);
    Object.defineProperty(obj, key, {
        set: function (newValue) {
            if (value !== newValue) {
                observe(newValue);
                value = newValue;
                dep.notify();
            }
            return value;
        },
        get: function () {
            Dep.target && dep.addDep(Dep.target);
            return value;
        },
    });
}

class Compile {
    constructor(el, vm) {
        this.$el = document.querySelector(el);
        this.$vm = vm;
        //根元素遍历
        if (this.$el) {
            this.compile(this.$el);
        }
    }
    compile(el) {
        const childNodes = el.childNodes;
        Array.from(childNodes).forEach((node) => {
            //判断是元素
            if (this.isElement(node)) {
                this.compileElement(node);
            }
            //分析文本元素
            if (this.isInterpolation(node)) {
                this.compileText(node);
            }
            //递归子元素
            if (node.childNodes && node.childNodes.length > 0) {
                this.compile(node);
            }
        });
    }
    isElement(node) {
        //元素nodeType
        return node.nodeType == 1;
    }
    isInterpolation(node) {
        //判断文本类型
        return node.nodeType == 3 && /\{\{(.*)\}\}/.test(node.textContent);
    }
    isDirective(attr) {
        return attr.indexOf("v-") === 0;
    }
    formatDirectiveParam(attrName) {
        return attrName.split(":")[1];
    }
    compileElement(node) {
        let attrs = node.attributes;
        Array.from(attrs).map((attr) => {
            //处理click
            let attrName = attr.nodeName;
            let attrValue = attr.nodeValue;
            if (this.isDirective(attrName)) {
                let dir = attrName.split(":")[0].substring(2);
                console.log(dir);

                this[dir] &&
                    this[dir](
                        node,
                        attrValue,
                        this.formatDirectiveParam(attrName)
                    );
            }
        });
    }
    compileText(node) {
        let value = RegExp.$1;
        this.update(node, value, "text");
    }
    update(node, exp, dir) {
        const fn = this[dir + "Updater"];
        fn && fn(node, this.$vm[exp]);
        new Watch(this.$vm, exp, function (val) {
            fn && fn(node, val);
        });
    }
    text(node, exp) {
        this.update(node, exp, "text");
    }
    textUpdater(node, val) {
        node.textContent = val;
    }
    //指令
    html(node, value) {
        node.innerHTML = value;
    }
    //绑定属性
    bind(node, value, formatDirectiveParam) {
        this.update(node, exp, "bind");
    }
    bindUpdater(node, value, formatDirectiveParam) {
        if (formatDirectiveParam === "value") {
            node.value = this.$vm[value];
        }
    }
    //绑定事件
    on(node, value, formatDirectiveParam) {
        let fn = this.$vm[value];
        node.addEventListener(formatDirectiveParam, fn.bind(this.$vm));
    }
    //双向数据绑定
    model(node, exp) {
        node.addEventListener(
            "input",
            function (e) {
                this.$vm[exp] = Number.parseInt(e.data);
            }.bind(this)
        );
        this.update(node, exp, "model");
    }
    modelUpdater(node, value) {
        node.value = value;
    }
}

class Watch {
    constructor(vm, key, updateFn) {
        this.vm = vm;
        this.key = key;
        this.updateFn = updateFn;

        Dep.target = this;
        this.vm[this.key];
        Dep.target = null;
    }
    update() {
        this.updateFn.call(this.vm, this.vm[this.key]);
    }
}
class Dep {
    static target;
    constructor() {
        this.deps = [];
    }
    addDep(dep) {
        this.deps.push(dep);
    }
    notify() {
        this.deps.forEach((dep) => dep.update());
    }
}
