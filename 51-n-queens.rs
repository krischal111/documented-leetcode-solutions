// fn queen_line_of_sight()
impl Solution {
    pub fn solve_n_queens(n: i32) -> Vec<Vec<String>> {
        let n = n as usize;
        let mut board = vec![vec![true;n];n];
        // queen_marker(&mut board, 3);
        // dbg!(board);
        let my_boards = board_queen(&board, n, n);
        return my_boards;
    }
}

fn board_queen(board:&[Vec<bool>], n:usize, m: usize) -> Vec<Vec<String>> {
    if n == 0 {
        // dbg!(0);
        return vec![Vec::with_capacity(n)];
    }

    let this_line = board.first().unwrap();

    let mut my_boards = vec![];
    for i in 0..m {
        if this_line[i] == false {
            continue;
        }
        let mut my_line = vec![b'.';m];
        my_line[i] = b'Q';
        let my_line = unsafe {String::from_utf8_unchecked(my_line)};

        let mut new_board = board.to_vec();
        queen_marker(&mut new_board, i, m);
        let mut bottom_boards = board_queen(&new_board[1..], n-1, m);

        for mut each_board in bottom_boards {
            each_board.insert(0, my_line.clone());
            my_boards.push(each_board);
        }

        // dbg!(new_board);
    }
    return my_boards;
}
fn queen_marker(board: &mut [Vec<bool>], x:usize, m: usize) {
    if board.len() == 0 {
        return;
    }
    // vertical and diagonals
    let l = board.len();
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
    dbg!(Solution::solve_n_queens(5));

}
struct Solution;