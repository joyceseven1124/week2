function func(a){
// 請用你的程式補完這個函式的區塊
    return function (b,c){
        let result = a+(b*c);
        console.log(result);
        return result;
    }
    
}
func(2)(3, 4); // 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5); // 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9); // 你補完的函式能印出 -3+(2*9) 的結果 15
// 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果