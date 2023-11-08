// fn queen_line_of_sight()
impl Solution {
    pub fn solve_n_queens(n: i32) -> Vec<Vec<String>> {
        let n = n as usize;
        let mut board = vec![vec![true;n];n];
        // queen_marker(&mut board, 3);
        // dbg!(board);
        let my_boards = board_queen(&board, n);
        return vec![];
    }
}

fn board_queen(board:&[Vec<bool>], n:usize) {
    if n == 0 {
        dbg!(0);
        return;
    }

    let this_line = board.first().unwrap();
    let m = this_line.len();

    for i in 0..m {
        if this_line[i] == false {
            continue;
        }
        let mut new_board = board.to_vec();
        queen_marker(&mut new_board, i);
        let my_boards = board_queen(&new_board[1..], n-1);
        // dbg!(new_board);
    }
    

}
fn queen_marker(board: &mut [Vec<bool>], x:usize) {
    if board.len() == 0 {
        return;
    }
    // vertical and diagonals
    let l = board.len();
    let m = board.first().unwrap().len();
    // dbg!(m);
    for i in 1..l {
        board[i][x] = false;
        let left = (x as isize - i as isize);
        let right = x + i;
        if left >= 0 {
            board[i][left as usize] = false;
        }
        if right < m {
            board[i][right] = false;
        }
    }
}


fn main() {
    Solution::solve_n_queens(4);

}
struct Solution;