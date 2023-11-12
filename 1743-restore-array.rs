fn find(pair: &[i32], num: i32) -> Option<i32> {
    let (a, b) = (pair[0], pair[1]);
    if a == num {
        Some(b)
    } else if b == num {
        Some(a)
    } else {
        None
    }
}

impl Solution {
    fn restore_array(mut adjacent_pairs: Vec<Vec<i32>>) -> Vec<i32> {
        let mut mylist = adjacent_pairs.pop().unwrap();
        let mut l = mylist[0];
        let mut r = mylist[1];
        let mut i : isize = adjacent_pairs.len() as isize -1;
        while !adjacent_pairs.is_empty() {
            {
                let i = i as usize;
                let mut num = find(&adjacent_pairs[i], l);
                if let Some(num) = num {
                    mylist.insert(0, num);
                    adjacent_pairs.remove(i);
                    l = num;
                } else {
                    let mut num = find(&adjacent_pairs[i], r);
                    if let Some(num) = num {
                        mylist.push(num);
                        adjacent_pairs.remove(i);
                        r = num
                    } 
                }
            }
            i -= 1;
            if i < 0 {
                i += adjacent_pairs.len() as isize ;
                if i < 0 {
                    break;
                }
            }
        }
        mylist
    }
}



fn main() {
    let input: Vec<Vec<i32>> = [[-3,-9],[-5,3],[2,-9],[6,-3],[6,1],[5,3],[8,5],[-5,1],[7,2]]
    .iter()
    .map(|s| s.to_vec())
    .collect();
    dbg!(Solution::restore_array(input));
}

struct Solution;