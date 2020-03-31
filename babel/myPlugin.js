let babel = require('@babel/core');
let t = require('@babel/types');
let preCalculator={
   visitor: {
       BinaryExpression(path) {
           let node = path.node;
           let left = node.left;
           let operator = node.operator;
           let right = node.right;
           if (!isNaN(left.value) && !isNaN(right.value)) {
               let result = eval(left.value + operator + right.value);
              //生成新节点，然后替换原先的节点
               path.replaceWith(t.numericLiteral(result));
                //递归处理 如果当前节点的父节点配型还是表达式 
                if (path.parent && path.parent.type == 'BinaryExpression') {
                   preCalculator.visitor.BinaryExpression.call(null,path.parentPath);
               }
           }
       }
   }
}

const result = babel.transform('let sum = 1 + 2',{
   plugins:[
       preCalculator
   ]
});
console.log(result);

