from datetime import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        target_date = datetime(year,month,day)
        day_num = target_date.weekday()

        value = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return value[day_num]
        