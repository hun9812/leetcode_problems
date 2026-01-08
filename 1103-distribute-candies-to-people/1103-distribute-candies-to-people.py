class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        div = [0 for i in range(num_people)]
        k = 0
        for i in range(1, candies+1):
            if candies - i > 0:
                div[k] += i
                candies -= i
                k += 1
                k %= num_people
            else:
                div[k] += candies
                break
        return div
        