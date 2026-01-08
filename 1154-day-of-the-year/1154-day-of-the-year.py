from datetime import datetime
class Solution:
    def dayOfYear(self, date: str) -> int:
        date_list = list(map(int, (date.split("-"))))
        date1 = datetime(date_list[0], date_list[1], date_list[2])
        date2 = datetime(date_list[0], 1, 1)
        
        return (date1 - date2).days + 1


        