# The algorithmn surrounds around the date of the week the input date fell on, translated to Japanese

from datetime import datetime

def solution_station_2(date):
    date_object = datetime.strptime(date, "%Y-%m-%d")
    day_of_week = date_object.strftime("%A")
    if day_of_week == "Monday":
        return "月曜日"
    if day_of_week == "Tuesday":
        return "火曜日"
    if day_of_week == "Wednesday":
        return "水曜日"
    if day_of_week == "Thursday":
        return "木曜日"
    if day_of_week == "Friday":
        return "金曜日"
    if day_of_week == "Saturday":
        return "土曜日"
    if day_of_week == "Sunday":
        return "日曜日"
