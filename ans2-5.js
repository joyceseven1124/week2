function twoSum(nums, target){
    // your code here
    for(let i = 0; i <= nums.length; i++){
        if(target-nums[i] in nums){
            data = [i,nums.indexOf(target-nums[i])];
            return data;
        }
    }
    console.log(data);
    
}
let result=twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9