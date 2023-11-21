impl Solution {
    pub fn garbage_collection(garbage: Vec<String>, mut travel: Vec<i32>) -> i32 {
        let mut c_travel = Vec::with_capacity(travel.len() + 1);
        let mut total = 0;
        c_travel.push(0);
        for t in travel {
            total += t;
            c_travel.push(total);
        }

        let mut M = 0;
        let mut P = 0;
        let mut G = 0;
        let mut total = 0;
        
        for (i, gbg) in (0..).zip(garbage) {
            total += gbg.len() as i32;
            if gbg.contains('M') {
                M = i;
            }
            if gbg.contains('P') {
                P = i;
            }
            if gbg.contains('G') {
                G = i;
            }
        }

        total += c_travel[M] + c_travel[P] + c_travel[G];
        total as _
    }
}

fn main() {}
struct Solution;