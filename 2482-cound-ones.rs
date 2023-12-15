impl Solution {
    pub fn ones_minus_zeros(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();

        let mut ones_col = vec![0;n];
        let mut ones_row = vec![];
        let max_ones = (m + n);
        for row in grid.iter() {
            let mut row_count = 0;
            for (j, &num) in row.iter().enumerate() {
                if num == 1 {
                    row_count += 1;
                    ones_col[j] += 1;
                }
            }
            ones_row.push(row_count);
        }

        let mut output = vec![];
        for i in 0..m {
            let mut row = vec![];
            for j in 0..n {
                let c_ones = ones_col[j];
                let c_zeros = n as i32 - c_ones;
                let r_ones = ones_row[i];
                let r_zeros = m as i32- r_ones;

                row.push(r_ones + c_ones - r_zeros - c_zeros);
            }
            // println!("{:?}", &row);
            output.push(row);
        }
        output
        // vec![]
    }
}