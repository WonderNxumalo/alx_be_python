import datetime #from datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")

display_current_datetime()

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    current_date = datetime.date.today()
    days_to_add = datetime.timedelta(days=number_of_days)
    future_date = current_date + days_to_add
    print(f"Future date: {future_date}")

calculate_future_date()