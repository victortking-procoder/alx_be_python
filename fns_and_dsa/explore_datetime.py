from datetime import datetime, timedelta, date

def display_current_datetime():
  current_date = datetime.now()
  formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
  print(f"Current date and time: {formatted}")
display_current_datetime()

def calculate_future_date():
   num_of_days = int(input("Enter the number of days to add to the current date:"))
   
   future_date = date.today() + timedelta(days=num_of_days)
   print(f"Future date: {future_date}")
   
calculate_future_date()
   