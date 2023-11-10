fn next_line(mut line: Vec<i32>) -> Vec<i32> {
    line.push(1);
    for i in (1..line.len()-1).rev() {
        line[i] += line[i-1];
    }
    line
}
impl Solution {
    pub fn get_row(num_rows: i32) -> Vec<i32> {
        let mut this_line = Vec::with_capacity(num_rows as usize);
        this_line.push(1);
        for i in 0..num_rows {
            this_line = next_line(this_line);
        }
        this_line
    }
}


fn main() {
    dbg!(Solution::get_row(3));
}
struct Solution;