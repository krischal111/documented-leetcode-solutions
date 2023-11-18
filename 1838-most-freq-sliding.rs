impl Solution {
    pub fn max_frequency(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort_unstable();
        let mut max_count : i32 = 0;
        let mut now_count : usize = 0;
        let mut now_num : i32 = nums[0];
        let mut now_sum : i32 = 0;


        for (i, &num) in nums[1..].iter().enumerate() {
            let i = i + 1;
            // dbg!(i, );
            {   // update forward sliding window logic
                now_count += 1;
                let diff = num - now_num;
                now_sum += now_count as i32 * diff;
                now_num = num;
            }

            // fix back window
            while now_sum > k {
                let diff = now_num - nums[i - now_count];
                now_sum -= diff;
                now_count -= 1;
            }
            
            // update the optimal value
            let now_count = now_count as i32;
            if now_count > max_count {
                max_count = now_count;
                let start = i - now_count as usize;
                // eprintln!("Best sliding window is {:?}", &nums[start..=i]);
                // dbg!(now_count, now_num, now_sum);
                // eprintln!();
            }
        }
        max_count + 1
    }
}


fn main() {
    dbg!(Solution::max_frequency(vec![9930,9923,9983,9997,9934,9952,9945,9914,9985,9982,9970,9932,9985,9902,9975,9990,9922,9990,9994,9937,9996,9964,9943,9963,9911,9925,9935,9945,9933,9916,9930,9938,10000,9916,9911,9959,9957,9907,9913,9916,9993,9930,9975,9924,9988,9923,9910,9925,9977,9981,9927,9930,9927,9925,9923,9904,9928,9928,9986,9903,9985,9954,9938,9911,9952,9974,9926,9920,9972,9983,9973,9917,9995,9973,9977,9947,9936,9975,9954,9932,9964,9972,9935,9946,9966], 3056));
    // dbg!(Solution::max_frequency(vec![1,4,8,13], 5));
}
struct Solution;