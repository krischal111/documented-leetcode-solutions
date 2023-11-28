modulo = 10**9 + 7
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        plant_count_list = []
        seat_true_plant_false = True
        seat_plant_count = 0
        for s in corridor:
            if seat_true_plant_false:
                if s == 'S':
                    # seat case
                    seat_plant_count += 1
                    if seat_plant_count == 2:
                        seat_plant_count -= 1
                        seat_true_plant_false = False
            else:
                if s == 'P':
                    seat_plant_count += 1
                else:
                    seat_true_plant_false = True
                    plant_count_list.append(seat_plant_count)
                    seat_plant_count = 1

        if seat_true_plant_false:
            return 0
        product = 1
        for plant_count in plant_count_list:
            product *= plant_count
            product %= modulo
        return product