import '../libs/inflate.min.js'
import {
    initLoaderModule,
    actionTwoFun,
    actionOneFun,
    actionFourFun,
    actionThreeFun,
    changeTexture,
    deleteGroup
} from './3dmodule.js'


let actionBtn = document.querySelector('#action');
let actionListBtn = document.querySelector('.float-position-one');
let dispatch = document.querySelector('.dispatch');
let exchange = document.querySelector('.exchange');

let addModel = document.querySelector('.add-model')
let detelModel = document.querySelector('.detel-model')

let bgLeftBtn = document.querySelector('.bg-left');



let bg1 = document.querySelector('#bg1');
let bg2 = document.querySelector('#bg-mining');


let bgList = {
    first: {
        index: 0,
        list: [
            'url(\'./img/bg/background.png\')',
            'url(\'./img/bg/bj1.png\')',
            'url(\'./img/bg/bj2.png\')',
            'url(\'./img/bg/bj3.png\')',
            'url(\'./img/bg/bj4.png\')',
        ]
    },
    second: {
        index: 0,
        list: [
            'url(\'./img/bg/bj8.png\')',
            'url(\'./img/bg/bj5.png\')',
            'url(\'./img/bg/bj9.png\')',
        ]
    }
};

let actionList = [
    actionOneFun,
    actionTwoFun,
    actionThreeFun,
    actionFourFun
];

function init() {
    initLoaderModule(10)
}

window.init = function (Nmtoken, platforms) {
    token = Nmtoken;
    platform = platforms;
    init()
};
window.updateInit = function (Ntoken) {
    token = Ntoken;
    init()
};

function toggleDomDisplay(dom) {
    dom.style.display = dom.style.display === 'none' ? 'block' : 'none';
}

function changeBg() {
    toggleDomDisplay(bg1);
    toggleDomDisplay(bg2);
    bg1.style.backgroundSize = 'cover';
    bg2.style.backgroundSize = 'cover';
}


function checklvl(num) {
    if (15 >= num && num >= 1) {
        return '#04c882';
    }
    if (50 >= num && num >= 16) {
        return '#01A5E1';
    }
    if (80 >= num && num >= 51) {
        return '#9C01E1';
    }
    if (150 >= num && num >= 81) {
        return '#E15C01';
    }
}

actionBtn.addEventListener('click', function (e) {
    toggleDomDisplay(actionListBtn);
    e.stopPropagation()
});


Array.from(actionListBtn.children).map((item, index) => {
    item.addEventListener('click', () => {
        actionList[index]();
    });
});


dispatch.addEventListener('click', function () {
    changeBg()
});

exchange.addEventListener('click', function () {
    changeTexture(90)
});


bgLeftBtn.addEventListener('click', function () {

        bgList.first.index--;
        if (bgList.first.index < 0) {
            bgList.first.index = bgList.first.list.length - 1;
        }
        bg1.style.background = bgList.first.list[bgList.first.index];
        bg1.style.backgroundSize = 'cover';
    
});

addModel.addEventListener('click',function(){
    initLoaderModule(10)
})
detelModel.addEventListener('click',()=>{
    deleteGroup()
})
window.addEventListener('load', function () {
    init();
});