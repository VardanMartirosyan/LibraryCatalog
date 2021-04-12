from datetime import date, datetime, timedelta

class DataCalculator:
    def calculateData(self, beforeDays) -> str:
        today = datetime.now()
        dd = today - timedelta(days=beforeDays)
        return dd.date()

    def getSubOfTwoDates(self, bigger, smaller) -> int:
        s_date = date(int(smaller[0]), int(smaller[1]), int(smaller[2]))
        b_date = date(int(bigger[0]), int(bigger[1]), int(bigger[2]))
        delta = b_date - s_date
        return delta.days