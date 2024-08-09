import pandas_market_calendars as mcal
from datetime import datetime
import os  # Import the os module

def is_trading_day():
    # Get the current date
    today = datetime.now().date()

    # Get the NYSE calendar
    nyse = mcal.get_calendar('NYSE')

    # Get the NYSE trading schedule for today
    schedule = nyse.schedule(start_date=today, end_date=today)

    # Check if today is a trading day
    return not schedule.empty

if __name__ == "__main__":
    if is_trading_day():
        with open(os.environ['GITHUB_ENV'], 'a') as env_file:
            env_file.write("IS_HOLIDAY=false\n")
    else:
        with open(os.environ['GITHUB_ENV'], 'a') as env_file:
            env_file.write("IS_HOLIDAY=true\n")
