fn next_line(mut line: Vec<i32>) -> Vec<i32> {
    line.push(1);
    for i in (1..line.len()-1).rev() {
        line[i] += line[i-1];
    }
    line
}
impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        let mut this_line = Vec::with_capacity(num_rows as usize);
        this_line.push(1);
        let mut outputs = Vec::with_capacity(num_rows as usize);
        outputs.push(this_line.clone());
        for i in 1..num_rows {
            this_line = next_line(this_line);
            outputs.push(this_line.clone())
        }
        outputs
    }
}


fn main() {
    dbg!(Solution::generate(5));
}
struct Solution;