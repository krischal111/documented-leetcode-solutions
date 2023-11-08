impl Solution {
    pub fn is_reachable_at_time(sx: i32, sy: i32, fx: i32, fy: i32, t: i32) -> bool {
        if (sx, sy) == (fx, fy) {
            return t != 1;
        }
        let (xdiff, ydiff) = ((fx - sx).abs(), (fy - sy).abs());
        use std::cmp::max;
        let m = max(xdiff, ydiff);
        return m <= t;
    }
}