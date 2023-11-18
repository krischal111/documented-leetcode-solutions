impl Solution {
    pub fn min_pair_sum(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let limit = nums.len() / 2  ;
        nums[..limit].iter().zip(nums.iter().rev()).map(|(a,b)| a+b).max().unwrap()
    }
}