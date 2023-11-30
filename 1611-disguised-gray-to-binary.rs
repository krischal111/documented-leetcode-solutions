impl Solution {
    pub fn minimum_one_bit_operations(mut n: i32) -> i32 {
        let mut result = n;
        while n != 0 {
            n >>= 1;
            result ^= n;
        }
        result
    }
}