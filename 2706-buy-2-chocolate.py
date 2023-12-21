impl Solution {
    pub fn buy_choco(mut prices: Vec<i32>, money: i32) -> i32 {
        prices.sort();
        let sum : i32 = prices[..2].iter().sum();
        if sum > money { money } else { money - sum }
    }
}