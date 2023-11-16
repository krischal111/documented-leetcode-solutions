#[inline]
fn my_solution(nums: &[u16]) -> usize {
    let mut my_ans = [false; u16::MAX as usize + 1];
    for num in nums {
        my_ans[*num as usize] = true;
    }
    // dbg!(&my_ans[..10]);
    for i in 0.. {
        if !my_ans[i] {
            return i;
        }
    }
    return 0;
}

impl Solution {
    pub fn find_different_binary_string(nums: Vec<String>) -> String {
        let mut converted_nums : Vec<u16> = nums.iter().map(|s| u16::from_str_radix(s, 2).unwrap()).collect();
        let ans = my_solution(&converted_nums);
        return std::format!("{ans:0l$b}", l = nums.first().unwrap().len());
    }
}


fn main() {
    // let my_test_case = ["0"];
    // let my_test_case = ["01","10"];
    let my_test_case = ["111","011","001"];
    let my_test_case : Vec<String> = my_test_case.iter().map(|s| s.to_string()).collect();
    dbg!(Solution::find_different_binary_string(my_test_case));
}
struct Solution;    