impl Solution {
    pub fn reduction_operations(mut nums: Vec<i32>) -> i32 {
        use std::cmp::Reverse;
        nums.sort_unstable_by_key(|num| Reverse(*num));
        
        (0..).zip(nums).fold(
            (0_usize/* total */, 0 /* repeating element */),
            |(total, repeating_element) , (i, number) | if repeating_element != number {
                (total+i, number)
            } else {
                (total, repeating_element)
            }
        ).0 as _
    }
}

fn main() {
    dbg!(Solution::reduction_operations(vec![5,1,3]));
}
struct Solution;