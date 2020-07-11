from datetime import datetime,timedelta

current_date = datetime.now()
one_day=timedelta(weeks=1)
error_day=current_date-one_day
print('Today is :' + str(error_day))