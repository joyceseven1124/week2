function maxProduct(nums){
// 請用你的程式補完這個函式的區塊
    let innerBigNum = 0;
    for(let i = 0; i <= nums.length; i++){
        if(nums.length == 2){
            innerBigNum = nums[0]*nums[1];
            break;
        }
        else{
            x=nums[i];
            for(let a = 0; a <= nums.length; a++){
                if (a !== i){
                    let result = x*nums[a];
                    if(result > innerBigNum){
                        innerBigNum = result; 
                    }
                }   
            }
        }
    }
    console.log(innerBigNum);
}
maxProduct([5, 20, 2, 6]) // 得到 120
maxProduct([10, -20, 0, 3]) // 得到 30
maxProduct([10, -20, 0, -3]) // 得到 60
maxProduct([-1, 2]) // 得到 -2
maxProduct([-1, 0, 2]) // 得到 0 或 -0
maxProduct([5, -1, -2, 0]) // 得到 2
maxProduct([-5, -2]) // 得到 10