function maxZeros(nums){
    // 請用你的程式補完這個函式的區塊
    let finalTotal = 0;
    let total = 0;
    for (let i = 0; i <= nums.length; i++){
        if(nums[i] === 0){
            total ++;
        }else{
            if(total > finalTotal){
                finalTotal = total;
            }
            total = 0;
            continue;
        }
    }
    console.log(finalTotal);
}
maxZeros([0, 1, 0, 0]); // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
maxZeros([1, 1, 1, 1, 1]); // 得到 0
maxZeros([0, 0, 0, 1, 1]) // 得到 3
