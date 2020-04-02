window.onload = function () {
    //旋转速度
    let initSpeed = 25;
    let speed = initSpeed;
    let luckidNum = 0;
    let num = 0;
    let lotteryNum = 100;
    let lock = true;
    //timeID
    let timer;
    //mock奖品
    let prizeData = [{
            prize_name: '谢谢惠顾',
            id: '0'
        },
        {
            prize_name: '奖品1',
            image: './img/jibi2.png',
            id: '1'
        },
        {
            prize_name: '奖品2',
            image: './img/jibi2.png',
            id: '2'
        },
        {
            prize_name: '奖品3',
            image: './img/jibi2.png',
            id: '3'
        },
        {
            prize_name: '奖品4',
            image: './img/jibi2.png',
            id: '4'
        },
        {
            prize_name: '奖品5',
            image: './img/jibi2.png',
            id: '5'
        },
        {
            prize_name: '奖品6',
            image: './img/jibi2.png',
            id: '6'
        },
        {
            prize_name: '奖品7',
            image: './img/jibi2.png',
            id: '7'
        },

    ]

    let win = document.querySelector('.win')
    let lotteryArea = Array.from(document.querySelectorAll('.lottery-turntable-area'));
    let startBtn = document.getElementById('start-lottery');
    let lose = document.querySelector('.lose')
    let mask = document.querySelector('.mask')
    let loseClose = document.querySelector('.lose-close-btn')
    let winCon = document.querySelector('.win-con')
    let lotteryState;


    function init() {
        document.querySelector('.lottery-num').innerHTML = `剩余${lotteryNum}次数`
        //去除中间元素
        lotteryArea.splice(4, 1);
        //改变顺时针顺序
        lotteryArea = swapArea(lotteryArea);
        //通过数据生成DOM结构
        Array.from(prizeData).forEach(function (item, index) {
            //因为谢谢参与与其他DOM结构不一样，需要单独处理
            if (item['prize_name'] === '谢谢参与') {
                lotteryArea[index].removeChild(lotteryArea[index].querySelector('.lottery-turntable-area-img'))
                lotteryArea[index].getElementsByTagName('span')[0].innerHTML = ` <div class="thanks">
                        <span>谢谢<br>参与</span>
                    </div>`
            } else {
                lotteryArea[index].getElementsByTagName('span')[0].innerHTML = item['prize_name']
            }
        })
    }
    //顺时针顺序
    function swapArea(list) {
        let temp = [];
        temp.push(list[0]);
        temp.push(list[1]);
        temp.push(list[2]);
        temp.push(list[4]);
        temp.push(list[7]);
        temp.push(list[6]);
        temp.push(list[5]);
        temp.push(list[3]);
        return temp
    }
    //获奖判断显示界面
    function openResult(str) {
        if (str === 'win') {
            win.style.display = 'block';
            mask.style.display = 'block'
        } else if (str === 'lose') {
            lose.style.display = 'block';
            mask.style.display = 'block'
        }
    }

    function animate() {
        return function () {
            //每次当前的位置亮起，前一个灭掉，0的时候前一个是7（因为没有中间元素）
            if (num === 0) {
                lotteryArea[num].className = 'lottery-turntable-area select-area';
                lotteryArea[7].className = 'lottery-turntable-area'
            } else {
                lotteryArea[num].className = 'lottery-turntable-area select-area';
                lotteryArea[num - 1].className = 'lottery-turntable-area'
            }
            if (num === 7) {
                //最后一个的时候清零
                num = 0;
            } else {
                num++
            }
        }
    }
    //mock数据也可以从服务器里面拿值
    function mockData() {
        let id = Math.floor(Math.random() * 10 % 8)
        if (id === 0) {
            lotteryState = 0
        } else {
            lotteryState = 1;
        }

        return {
            id: id.toString(),
            lotteryState,
        }
    }

    startBtn.addEventListener('click', async function () {
        if (lotteryNum === 0) {
            alert('没有次数了')
            return
        }
        //防止重复点击
        if (!lock) {
            return
        }
        lock = false;
        lotteryNum--;
        document.querySelector('.lottery-num').innerHTML = `剩余${lotteryNum}次数`
        //设置默认速度等待服务器响应结果，这里面用的mock数据
        timer = setInterval(animate(), speed);
        let resData = mockData()
        console.log(resData);

        //是否获奖
        lotteryState = resData.lotteryState;
        //幸运数字
        luckid = resData.id;
        //找到想要到奖品的位置
        luckidNum = prizeData.findIndex(function (item) {
            return item['id'] === luckid;
        });

        setTimeout(function () {
            //清除等待定时器
            clearInterval(timer)
            
            /**
             * 重新配置速度  确定循环次数到达指定商品
             * 9 - num + luckidNum + 8 * 10（这里的10是可以改动的，控制减慢速度的）
             * 1.配置速度的时候保证每次都是8的倍数，每次都会回到原地
             * 2.使当前位置归为到0点，因为在上面循环中num已经加一了
             *   需要减去保证和DOM的显示一直，但是位置还在之前的显示位置当前一共8个数
             *   8-(num-1)+8*10会回到0点
             * 3.再加上获取到的商品位置，循环完成后就能到指定商品位子
             */
            for (let i = 0; i < 9 - num + luckidNum + 8 * 10; i++) {
                //添加队列，保证时序时间
                speed += initSpeed + i;
                setTimeout(animate(), speed)
            }
            setTimeout(function () {
                openResult(lotteryState === 1 ? 'win' : 'lose');
                //归为值
                lock = true;
                speed = initSpeed
            }, speed + 500)
        }, 1000)
    }, false);

    loseClose.addEventListener('click', function () {
        lose.style.display = 'none';
        mask.style.display = 'none'

    })

    winCon.addEventListener('click', function () {
        win.style.display = 'none';
        mask.style.display = 'none'
    })
    init();
};