impl Solution {
    pub fn min_pair_sum(mut nums: Vec<i32>) -> i32 {
        nums.sort();
        let mut max = 0;
        let limit = nums.len() / 2  ;
        for (a, b) in nums[..limit].iter().zip(nums.iter().rev()) {
            let sum = a + b;
            if sum > max {
                max = sum;
            }
        }
        max
    }
}