class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = foods
        self.cuisines = cuisines
        self.ratings = ratings

    def changeRating(self, food: str, newRating: int) -> None:
        i = self.foods.index(food)
        self.ratings[i] = newRating

    def highestRated(self, cuisine: str) -> str:
        hrating = -1
        lfood = ""
        for i, thiscuisine in enumerate(self.cuisines):
            if thiscuisine == cuisine:
                rating = self.ratings[i]
                if hrating > rating:
                    continue
                food = self.foods[i]
                if hrating < rating:
                    hrating = rating
                    lfood = food
                else:
                    if lfood > food:
                        lfood = food
        return lfood

        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)