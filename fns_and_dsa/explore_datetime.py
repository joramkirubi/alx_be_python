from datetime import datetime, timedelta

def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()
    # Print in the required format
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    # Prompt user for number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    # Calculate future date
    future_date = datetime.now() + timedelta(days=days_to_add)
    # Print in the required format
    print("Future date:", future_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()

