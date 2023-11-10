const modulo : i64 = 10_i64.pow(9) + 7;

impl Solution {
    pub fn count_homogenous(s: String) -> i32 {
        if s.is_empty() {
            return 0;
        }
        let mut iterator = s.chars();
        let mut prevchar = iterator.next().unwrap();
        let mut prevcount : i64 = 1;

        let mut total_count = 0;

        while let Some(c) = iterator.next() {
            if prevchar == c {
                prevcount += 1;
                continue;
            }
            total_count += (((prevcount)*(prevcount + 1))/2)% modulo;
            // dbg!(prevcount);
            prevchar = c;
            prevcount = 1;
        }
        total_count += (((prevcount)*(prevcount + 1))/2) % modulo;
        return (total_count % modulo) as i32;
    }
}

fn main() {
    dbg!(Solution::count_homogenous("abbcccaa".to_owned()));
}
struct Solution;