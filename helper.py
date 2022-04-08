calculation_to_hours = 24
name_of_unit = 'hours'


def days_to_units(num_of_days,conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} {name_of_unit} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} {name_of_unit} minutes"
    else:
        return "unsupported unit"
        
''' Codeblock example '''
def validate_and_execute(days_and_unit_dictionary):
    try:
        # crazy shitt
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_days = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_days)
        elif user_input_number == 0:
            print(f"You entered 0, valid number please")
        else:
            print("you are so negative")
    except ValueError:
        print(f"Bad Input: {user_input_number} ")

user_input_message = "Enter a number of days and a conversion unit!\n"