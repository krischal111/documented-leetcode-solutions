#[inline]
fn sumn(n:i32) -> i32 {
    (n * (n-1))/2
}
impl Solution {
    pub fn total_money(n: i32) -> i32 {
        (0..7).map(|i| {
            let count = (n+i)/7;
            (7-i) * count + sumn(count)
        }).sum()
    }
}
