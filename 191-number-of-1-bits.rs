impl Solution {
    pub fn hammingWeight (mut n: u32) -> i32 {
        n.count_ones() as _
    }
}

/// other implementations
/// ```
/// impl Solution {
///     pub fn hammingWeight (mut n: u32) -> i32 {
///         let mut i = 0u32;
///         while n != 0 {
///             n &= n - 1;
///             i += 1;
///         }
///         i as _
///     }
/// }
/// ```
/// 
/// 
/// more simplified
/// ```
/// impl Solution {
/// pub fn hammingWeight (mut n: u32) -> i32 {
///     let mut i = 0;
///     while n != 0 {
///         n &= n - 1;
///         i += 1;
///     }
///     i
/// }
/// ```
