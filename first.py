from datetime import datetime

def age_calculator():
    # Prompt user for birth year, month, and day
    birth_year = int(input("Enter your birth year (YYYY): "))
    birth_month = int(input("Enter your birth month (MM): "))
    birth_day = int(input("Enter your birth day (DD): "))
    
    # Get current date
    today = datetime.today()
    birth_date = datetime(birth_year, birth_month, birth_day)
    
    # Compute age
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_month, birth_day):
        age -= 1  # Adjust if birthday hasn't occurred yet this year
    
    # Determine next birthday
    next_birthday = datetime(today.year, birth_month, birth_day)
    if today > next_birthday:
        next_birthday = datetime(today.year + 1, birth_month, birth_day)
    
    # Calculate countdown in days
    days_until_birthday = (next_birthday - today).days
    
    # Display results
    print(f"\nYou are {age} years old.")
    print(f"Your next birthday is on {next_birthday.strftime('%B %d, %Y')}.")
    print(f"Days remaining until your next birthday: {days_until_birthday} days.")

# Run the program
age_calculator()
