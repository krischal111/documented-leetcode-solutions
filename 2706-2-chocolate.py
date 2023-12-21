class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        price_lowest, price_lower = sorted(prices[:2])

        # we need the two smallest prices
        for new_price in prices[2:]:
            if new_price < price_lower:
                if new_price < price_lowest:
                    price_lower = price_lowest
                    price_lowest = new_price
                else:
                    price_lower = new_price
        sum_cost = price_lowest + price_lower
        if sum_cost > money:
            return money
        else:
            return money - sum_cost

        