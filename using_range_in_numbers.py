# - ask the user to input a NUMBER ranges from 1 to 50
         # > Less than or equal to 50 = VALID
         # > Greater than or equal to 51 = INVALID
         # > User input is not limited unless it's invalid
# - ask the user to input again until the user input is invalid
# - when the user input is invalid
         # > Display how many inputted numbers are in the following range:
         # > VALID NUM. = ASK NEXT NUM.
         # > INVALID NUM. = DISPLAY THE TALLY OF INPUTS IN THE RANGES THEY BELONG
         # > ex. 
            # Display should be like this:
              # 1 to 10: 3, 5, 8, 9, 
              # 11 to 20: 11, 15, 18, 20
              # 21 to 30: 24, 26, 28, 30
              # 31 to 40: 35, 38, 39, 
              # 41 to 50: 43, 45, 46, 

def collect_data():
    # This will be the list storage for the information inputted by the user.
    data_entered = []

    # Loop1: This is to ask the user to input a random number.
    while True:
        random_number = int(input("Enter a number: "))
        # This will store the first number.
        data_entered.append(random_number)

        # Check if the last entered `another` number was greater than 50 to exit Loop 1 as well.
        if random_number > 50:
            print("Invalid")
            break # This will stop loop 1.

        # Loop2: To ask for another number.
        while True:
            another = int(input("Enter a number: "))
            
            # This will store the other numbers inputted.
            data_entered.append(another)

            if another > 50:
                print("Invalid")
                break  # This will stop loop 2.

        return data_entered

def categorize(data_entered):
    
# Set of lists that will store the different range of number they belong in.
    one_to_ten = []
    eleven_to_twenty = []
    twentyone_to_thirty = []
    thirtyone_to_forty = []
    fortyone_to_fifty = []
    out_of_range = [] #Added so that out of range inputted number can be stored in.

# This will figure out which range the inputted number belong in.
    for number in data_entered:
        if 1 <= number <= 10:
            one_to_ten.append(number)
        elif 11 <= number <= 20:
            eleven_to_twenty.append(number)
        elif 21 <= number <= 30:
            twentyone_to_thirty.append(number)
        elif 31 <= number <= 40:
            thirtyone_to_forty.append(number)
        elif 41 <= number <= 50:
            fortyone_to_fifty.append(number)
        else:
            out_of_range.append(number)

# After the conditions fulfilled it will be print them accoridingly.
    print("1 to 10:", one_to_ten)
    print("11 to 20:", eleven_to_twenty)
    print("21 to 30:", twentyone_to_thirty)
    print("31 to 40:", thirtyone_to_forty)
    print("41 to 50:", fortyone_to_fifty)
    print("Out of range:", out_of_range)

#To define the whole program collect, print, and categorize.
def main():
    data_entered = collect_data()
    print("\nList of Numbers Entered and Categorized in their own Range:")
    categorize(data_entered)

if __name__ == "__main__":
    main()


    



