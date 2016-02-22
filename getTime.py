__author__ = 'michael'
from datetime import datetime
from WindowsNoticification import WindowsBalloonTip

class ClassTime(object):

    def __init__(self):
        pass

    @classmethod
    def timeDifferance(cls, time):
        current_time =  datetime.now()
        Current_Date_Time = datetime.now().strftime("%A")
        #print Current_Date_Time

        if Current_Date_Time == "Tuesday" or Current_Date_Time == "Thursday" or Current_Date_Time == "Sunday":
            next_time = datetime(current_time.year, current_time.month, current_time.day + 1, 12,20,)
            return next_time - current_time

        elif Current_Date_Time == "Saturday":
            next_time = datetime(current_time.year, current_time.month, current_time.day + 2, 12,20,)
            return next_time - current_time
        else:
            next_time = datetime(current_time.year, current_time.month, current_time.day, 12,20,)
            passed_time = next_time - current_time
            if passed_time.total_seconds() <= 0 and Current_Date_Time == "Monday" or Current_Date_Time == "Wednesday":
                next_time = datetime(current_time.year, current_time.month, current_time.day + 2, 12,20,)
                return next_time - current_time

            elif passed_time.total_seconds() <= 0 and Current_Date_Time == "Friday":
                next_time = datetime(current_time.year, current_time.month, current_time.day + 2, 12,20,)
                return next_time - current_time

            else:
                return next_time - current_time


def balloon_tip(title, msg):
    w = WindowsBalloonTip(title, msg)

if __name__ == "__main__":
    current_time = ClassTime.timeDifferance([0,2,5])
    days, remainder = divmod(current_time.total_seconds(), 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    balloon_tip("Class Time!!!", 'You have %d days, %02d hours, %02d minutes, and %02d seconds til your favorite class!!!' % (days, hours, minutes, seconds))
