impl Solution {
    pub fn reduction_operations(mut nums: Vec<i32>) -> i32 {
        use std::cmp::Reverse;
        nums.sort_unstable_by_key(|num| Reverse(*num));
        let mut repeat_elem = 0;
        let mut total = 0;
        for (i, elem) in (0..).zip(nums) {
            if elem == repeat_elem {
            } else {
                repeat_elem = elem;
                total += i;
                // println!("Adding {i} to {total} due to {elem}");
            }
        }
        
        total
    }
}