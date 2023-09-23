import datetime

current_datetime = datetime.datetime.now()
print("Aktuální datum a čas:", current_datetime)

from dateutil.relativedelta import relativedelta

current_year = datetime.datetime.now().year

for i in range(current_year, current_year + 5):
    easter_date = datetime.datetime(i, 3, 22) + relativedelta(weekday=relativedelta.SU(0))
    print(f"Velikonoční neděle v roce {i}: {easter_date.strftime('%Y-%m-%d')}")

from dateutil.relativedelta import relativedelta

current_year = datetime.datetime.now().year

while True:
    christmas_eve = datetime.datetime(current_year, 12, 24)
    if christmas_eve.weekday() == 6:  # Neděle
        print(f"Štědrý den (Christmas Eve) v neděli bude v roce {current_year}")
        break
    current_year += 1